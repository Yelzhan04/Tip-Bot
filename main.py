import telebot
import time

bot = telebot.TeleBot('1086226951:AAHdSi1xheA_Y1oxCNGkhB_u_wneH3nrm4w')


@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, "✌👋Hi,guys i will help you to find helpful information about Python.🤗")
    bot.send_message(message.chat.id, 'Click to /help for more information ',time.sleep(2))


@bot.message_handler(commands=['help'])
def help_bot(message):
    bot.send_message(
        message.chat.id,
        'Bot Commands\n' +
        '🐍 /AboutPython 🐍\n' +
        '👨‍🏫 ‍/Courses - list of courses 👩‍🏫\n' +
        '📚 /Books - show the channel about Python books 📚\n' +
        '👨‍💻 /Community - Python community in Telegram 👩‍💻\n' +
        '🔥 /Frameworks - Python Frameworks 🔥'
    )


@bot.message_handler(commands=['AboutPython'])
def about_python(message):
    bot.send_message(
        message.chat.id,
        "WHAT IS PYTHON⁉🐍"
    )
    bot.send_message(
        message.chat.id,
        "Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a "
        "simple but effective approach to object-oriented programming. Python's elegant syntax and dynamic typing, "
        "together with its interpreted nature, make it an ideal language for scripting and rapid application "
        "development in many areas on most platforms.", time.sleep(2))
    bot.send_message(
        message.chat.id,
        "Official page - https://www.python.org\n" +
        "Documentation - https://www.python.org/doc/\n" +
        "Download - https://www.python.org/downloads/\n" +
        "Forum - https://python-forum.io/", time.sleep(2))


@bot.message_handler(commands=['Courses'])
def send_courses(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton(
            "Codeacademy", url="https://www.codecademy.com/catalog/language/python",
        ),
        telebot.types.InlineKeyboardButton(
            "Coursera", url="https://www.coursera.org/specializations/python",
        )
    )
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Udacity", url="https://www.udacity.com/course/intro-to-programming-nanodegree--nd000"
        ),
        telebot.types.InlineKeyboardButton(
            "Udemy",
            url="https://www.udemy.com/course/pythonforbeginnersintro/?LSNPUBID=JVFxdTr9V80&ranEAID=JVFxdTr9V80&ranMID=39197&ranSiteID=JVFxdTr9V80-Gi4FgDADsNWKBhjiF0rrRw&utm_medium=udemyads&utm_source=aff-campaign")
    )

    bot.send_message(message.chat.id, reply_markup=keyboard, text="THERE'S MOST USEFUL COURSE FOR BASIC")


@bot.message_handler(commands=["Books"])
def send_books(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Python Textbook', url="https://t.me/python_textbooks"
        )
    )
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Python Books', url="https://t.me/pythonbooks"
        )
    )
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Books about Python', url="https://t.me/pythonknigi"
        )
    )
    bot.send_message(message.chat.id, "You can find any book here.(Frameworks,ML,II,DL,Basic and etc)",
                     reply_markup=keyboard)


@bot.message_handler(commands=['Community'])
def com(message):
    bot.send_message(message.chat.id, "SOON!!!")


@bot.message_handler(commands=["Frameworks"])
def com(message):
    bot.send_message(message.chat.id, "SOON!!!"
                     )


if __name__ == '__main__':
    bot.polling(none_stop=True)
