import telebot
import requests
import json

bot = telebot.TeleBot('6082280795:AAEWGRwKjTey8htQhOqFeaZZkcNo9PTkDMk')

class HttpCatBot:
    def __init__(self):
        self.error_code = None
    
    def set_error_code(self, code):
        self.error_code = code
    
    def get_error_image(self):
        if self.error_code is None:
            return None
        
        url = f'https://http.cat/{self.error_code}.jpg'
        response = requests.get(url)
        
        if response.status_code != 200:
            return None
        
        return response.content

http_cat_bot = HttpCatBot()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Введите код ошибки:")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        http_cat_bot.set_error_code(int(message.text))
        image = http_cat_bot.get_error_image()
        if image is not None:
            bot.send_photo(message.chat.id, image)
        else:
            bot.send_message(message.chat.id, "Изображение не найдено.")
    except ValueError:
        bot.send_message(message.chat.id, "Неправильный формат кода ошибки.")

bot.polling()