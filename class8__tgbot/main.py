import telebot
from openai import OpenAI
from config import TGtoken, OPENAItoken

bot = telebot.TeleBot(TGtoken)
client = OpenAI(api_key=OPENAItoken)

@bot.message_handler(commands=['start'])
def start_hander(message):
	bot.send_message(message.chat.id, "Привет! Welcome! Buenos dias! Это бот-хостер для языковой модели GPT-3. For more type: /help")

@bot.message_handler(content_types=['text'])
def text_handler(message):
	print('here!')
	completion = client.chat.completions.create(
  		model="gpt-3.5-turbo",
  		messages=[
    		{"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    		{"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  	]
	)
	print(completion)
	bot.send_message(message.chat.id, completion.choices[0].message)

if __name__ == "__main__":
	bot.infinity_polling()