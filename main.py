import telebot
from function import number_to_words

# Создание экземпляра бота с указанием токена
bot = telebot.TeleBot("yor token")

# Обработчик команды start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Привет! Я бот, готовый принять твои сообщения.")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text

    try:
        # Преобразование числа в слова с помощью функции number_to_words
        result = number_to_words(int(text))
        bot.reply_to(message, result)
    except ValueError:
        bot.reply_to(message, "Ошибка! Введите число.")

# Запуск бота
bot.polling()

