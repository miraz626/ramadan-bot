import telebot

TOKEN = "8209701585:AAHkEXTt5_Fzcbi4wEu0eq7OJo9kUeDNOyI"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot Running Successfully ✅")

print("Bot Started...")
bot.infinity_polling()