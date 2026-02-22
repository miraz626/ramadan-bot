import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import requests
import datetime
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# ৬৪ জেলা
districts = [
"Dhaka","Tangail","Chattogram","Khulna","Rajshahi",
"Barishal","Sylhet","Rangpur","Mymensingh"
]

# Ramadan 2026 start date (Bangladesh approx)
ramadan_start = datetime.date(2026, 2, 18)

# START
@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for d in districts:
        markup.add(KeyboardButton(d))

    bot.send_message(
        message.chat.id,
        "🌙 RAMADAN SEHRI & IFTAR TIME BOT\n\n"
        "👑 Developer: MIRAZ BHAI\n"
        "🚀 TEAM BCS\n\n"
        "আপনার জেলা নির্বাচন করুন:",
        reply_markup=markup
    )

# জেলা সিলেক্ট করলে
@bot.message_handler(func=lambda message: message.text in districts)
def send_time(message):
    district = message.text

    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    roza_no = (tomorrow - ramadan_start).days + 1

    url = f"http://api.aladhan.com/v1/timingsByCity?city={district}&country=Bangladesh&method=1"
    response = requests.get(url).json()

    fajr = response['data']['timings']['Fajr']
    maghrib = response['data']['timings']['Maghrib']

    bot.send_message(
        message.chat.id,
        f"📅 আগামীকাল: {tomorrow.strftime('%d %B %Y')}\n"
        f"🌙 রোজা নং: {roza_no}\n\n"
        f"🌄 সেহেরি শেষ: {fajr}\n"
        f"🌇 ইফতার: {maghrib}\n\n"
        f"👑 Developer: MIRAZ BHAI\n"
        f"🚀 TEAM BCS"
    )

bot.polling()
