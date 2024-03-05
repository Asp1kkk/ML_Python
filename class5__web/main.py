import requests
from bs4 import BeautifulSoup

def GetFirstParagraph(url: str) -> str:
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	return soup.find("p").get_text()

i = 0
result = []
def getFirstParagraphsFromPage(url):
	global result
	global i
	if i == 4:
		return

	INIT_ENDPOINT = "https://habr.com"


	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')

	for link in soup.find_all("a", {"class": "tm-title__link"}):
		result.append(GetFirstParagraph(f'{INIT_ENDPOINT}{link["href"]}'))

	i += 1
	GetFirstParagraph(f'{INIT_ENDPOINT}{soup.find("a", {"class": "tm-pagination__page"})["href"]}')

print(getFirstParagraphsFromPage("https://habr.com/ru"))
print(result)

	