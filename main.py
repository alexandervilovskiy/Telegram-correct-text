import telebot
import language_tool_python

API_TOKEN = "Твой токен бота"

bot = telebot.TeleBot(API_TOKEN)

def correct_text(text):
    tool = language_tool_python.LanguageTool("ru")
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text 

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привет! Скинь текст который нужно исправить, я помогу тебе его исправить")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    corrected_text = correct_text(text)
    bot.reply_to(message, f"Исходный текст: {text}\nИсправленный текст: {corrected_text}")

bot.polling()
