import bs4
import requests
from bs4 import BeautifulSoup
from typing import List, Dict
import pandas as pd
import time
from tqdm import tqdm

# Новости Иркутска

class Article:
	title: str = ""
	tags: Dict[str, str] = {}
	paragraphs: List[str] = []
	date: time.struct_time

	def __init__(self, tag: bs4.element.Tag) -> None:
		self.tag = tag
	
	def setTitle(self) -> None:
		self.title = self.tag.find("h2").get_text()

	def __extractTime(self, date: str) -> time.struct_time:
		return time.strptime(date, '%Y-%m-%dT%H:%M:%S')

	def setDate(self) -> None:
		self.date = self.__extractTime(self.tag.find("time", {"slot": "date"})['datetime'])
	
	def setTags(self) -> None:
		self.tags["rubrics"] = self.tag.find("div", {"data-test": "archive-record-rubrics"}).get_text()
		self.tags["theme"] = self.tag.find("div", {"data-test": "archive-record-theme"}).get_text()
		self.tags["format"] = self.tag.find("div", {"data-test": "archive-record-format"}).get_text()
	
	def setParagraphs(self) -> None:
		link = self.tag.find("a")

		session = requests.session()
		response = session.get(BASE_URL + link['href'].replace("/text/", ""))
		soup = BeautifulSoup(response.text, 'html.parser')

		self.paragraphs = self.__extractParagraphs(soup)

	def __extractParagraphs(self, soup) -> List[str]:
		result: List[str] = []

		for item in soup.find("div", {"id": "articleBody"}).find_all("div", {"class": "uiArticleBlockText_i9h2o"}):
			result.append(item.get_text())

		return result

def findArticle() -> List[bs4.element.Tag]:
	return soup.find_all("article", {"data-test": "archive-record-item"})

BASE_URL = "https://ircity.ru/text/"
session = requests.session()

data = {
	'time': [],
	'titles': [],
	'tags': []
}

for i in tqdm(range(25)): # 1000 требующихся статей / 40 статец на странице = 25 страниц
	response = session.get(BASE_URL + f"?page={i+1}")
	soup = BeautifulSoup(response.text, 'html.parser')

	for item in tqdm(findArticle()):
		article = Article(item)

		article.setTitle()
		article.setTags()
		article.setDate() # Помимо заголовка и тегов получил еще дату написания
		article.setParagraphs() # И абзацы с инфой

		data['time'].append(article.date)
		data['titles'].append(article.title)
		data['tags'].append(article.tags)

df = pd.DataFrame(data)
df.to_csv("./data.csv", index=False)