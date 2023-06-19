import telebot
import requests

class HttpCatBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.keyboard = telebot.types.InlineKeyboardMarkup()
        self.keyboard.row(
            telebot.types.InlineKeyboardButton("100", callback_data="100"),
            telebot.types.InlineKeyboardButton("101", callback_data="101"),
            telebot.types.InlineKeyboardButton("102", callback_data="102"),
            telebot.types.InlineKeyboardButton("103", callback_data="103"),
        )
        self.keyboard.row(
            telebot.types.InlineKeyboardButton("200", callback_data="200"),
            telebot.types.InlineKeyboardButton("201", callback_data="201"),
            telebot.types.InlineKeyboardButton("202", callback_data="202"),
            telebot.types.InlineKeyboardButton("203", callback_data="203"),
            telebot.types.InlineKeyboardButton("204", callback_data="204"),
            telebot.types.InlineKeyboardButton("205", callback_data="205"),
            telebot.types.InlineKeyboardButton("206", callback_data="206"),
            telebot.types.InlineKeyboardButton("207", callback_data="207"),
        )
        self.keyboard.row(
            telebot.types.InlineKeyboardButton("300", callback_data="300"),
            telebot.types.InlineKeyboardButton("301", callback_data="301"),
            telebot.types.InlineKeyboardButton("302", callback_data="302"),
            telebot.types.InlineKeyboardButton("303", callback_data="303"),
            telebot.types.InlineKeyboardButton("304", callback_data="304"),
            telebot.types.InlineKeyboardButton("305", callback_data="305"),
            telebot.types.InlineKeyboardButton("307", callback_data="307"),
            telebot.types.InlineKeyboardButton("308", callback_data="308"),
        )
        self.keyboard.row(
            telebot.types.InlineKeyboardButton("400", callback_data="400"),
            telebot.types.InlineKeyboardButton("401", callback_data="401"),
            telebot.types.InlineKeyboardButton("402", callback_data="402"),
            telebot.types.InlineKeyboardButton("403", callback_data="403"),
            telebot.types.InlineKeyboardButton("404", callback_data="404"),
            telebot.types.InlineKeyboardButton("405", callback_data="405"),
            telebot.types.InlineKeyboardButton("406", callback_data="406"),
            telebot.types.InlineKeyboardButton("407", callback_data="407"),
            telebot.types.InlineKeyboardButton("408", callback_data="408"),
            telebot.types.InlineKeyboardButton("409", callback_data="409"),
            telebot.types.InlineKeyboardButton("410", callback_data="410"),
            telebot.types.InlineKeyboardButton("411", callback_data="411"),
            telebot.types.InlineKeyboardButton("412", callback_data="412"),
            telebot.types.InlineKeyboardButton("413", callback_data="413"),
            telebot.types.InlineKeyboardButton("414", callback_data="414"),
            telebot.types.InlineKeyboardButton("415", callback_data="415"),
            telebot.types.InlineKeyboardButton("416", callback_data="416"),
            telebot.types.InlineKeyboardButton("417", callback_data="417"),
            telebot.types.InlineKeyboardButton("418", callback_data="418"),
            telebot.types.InlineKeyboardButton("419", callback_data="419"),
            telebot.types.InlineKeyboardButton("421", callback_data="421"),
            telebot.types.InlineKeyboardButton("422", callback_data="422"),
            telebot.types.InlineKeyboardButton("423", callback_data="423"),
            telebot.types.InlineKeyboardButton("424", callback_data="424"),
            telebot.types.InlineKeyboardButton("425", callback_data="425"),
            telebot.types.InlineKeyboardButton("426", callback_data="426"),
            telebot.types.InlineKeyboardButton("427", callback_data="427"),
            telebot.types.InlineKeyboardButton("428", callback_data="428"),
            telebot.types.InlineKeyboardButton("429", callback_data="429"),
            telebot.types.InlineKeyboardButton("431", callback_data="431"),
            telebot.types.InlineKeyboardButton("451", callback_data="451"),
            telebot.types.InlineKeyboardButton("499", callback_data="499"),
        )
        self.keyboard.row(
            telebot.types.InlineKeyboardButton("500", callback_data="500"),
            telebot.types.InlineKeyboardButton("501", callback_data="501"),
            telebot.types.InlineKeyboardButton("502", callback_data="502"),
            telebot.types.InlineKeyboardButton("503", callback_data="503"),
            telebot.types.InlineKeyboardButton("504", callback_data="504"),
            telebot.types.InlineKeyboardButton("505", callback_data="505"),
            telebot.types.InlineKeyboardButton("506", callback_data="506"),
            telebot.types.InlineKeyboardButton("507", callback_data="507"),
            telebot.types.InlineKeyboardButton("508", callback_data="508"),
            telebot.types.InlineKeyboardButton("509", callback_data="509"),
            telebot.types.InlineKeyboardButton("510", callback_data="510"),
            telebot.types.InlineKeyboardButton("511", callback_data="511"),
            telebot.types.InlineKeyboardButton("521", callback_data="521"),
            telebot.types.InlineKeyboardButton("522", callback_data="522"),
            telebot.types.InlineKeyboardButton("523", callback_data="523"),
            telebot.types.InlineKeyboardButton("525", callback_data="525"),
        )
    
    def run(self):
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_query(call):
            try:
                response = requests.get(f"https://http.cat/{call.data}")
                self.bot.send_photo(call.message.chat.id, response.content, reply_markup=self.keyboard)
            except:
                self.bot.send_message(call.message.chat.id, "Error")
        
        @self.bot.message_handler(commands=["start"])
        def start_message(message):
            self.bot.send_message(message.chat.id, "Здраввствуйте!")
            self.bot.send_message(message.chat.id, "Выберите статус код:", reply_markup=self.keyboard)
        
        self.bot.polling()


if __name__ == "__main__":
    http_cat_bot = HttpCatBot("6082280795:AAEWGRwKjTey8htQhOqFeaZZkcNo9PTkDMk")
    http_cat_bot.run()