import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

sehri_time = "4:45 AM"
iftar_time = "6:10 PM"

districts = ["Dhaka","Chittagong","Rajshahi","Khulna","Barisal","Sylhet","Rangpur","Mymensingh",
"Comilla","Feni","Brahmanbaria","Rangamati","Noakhali","Chandpur","Lakshmipur","Cox's Bazar",
"Bandarban","Khagrachari","Sirajganj","Pabna","Bogura","Joypurhat","Naogaon","Natore",
"Chapainawabganj","Jashore","Satkhira","Meherpur","Narail","Chuadanga","Kushtia","Magura",
"Bagerhat","Jhenaidah","Pirojpur","Patuakhali","Bhola","Barguna","Jhalokathi","Habiganj",
"Moulvibazar","Sunamganj","Dinajpur","Gaibandha","Kurigram","Lalmonirhat","Nilphamari",
"Panchagarh","Thakurgaon","Sherpur","Jamalpur","Netrokona","Tangail","Kishoreganj",
"Manikganj","Munshiganj","Narayanganj","Narsingdi","Faridpur","Gopalganj","Madaripur",
"Rajbari","Shariatpur"]

@bot.message_handler(commands=['start'])
def start(message):
    text = """🌙 Ramadan Mubarak!

Available Commands:

/sehri - আজকের সেহরির সময়
/iftar - আজকের ইফতারের সময়
/district - বাংলাদেশের ৬৪ জেলা
/dua - রমজানের দোয়া
"""
    bot.reply_to(message, text)

@bot.message_handler(commands=['sehri'])
def sehri(message):
    bot.reply_to(message, f"🌙 আজকের সেহরির সময়: {sehri_time}")

@bot.message_handler(commands=['iftar'])
def iftar(message):
    bot.reply_to(message, f"🌅 আজকের ইফতারের সময়: {iftar_time}")

@bot.message_handler(commands=['district'])
def district(message):
    text = "🇧🇩 বাংলাদেশের ৬৪ জেলা:\n\n"
    text += "\n".join(districts)
    bot.reply_to(message, text)

@bot.message_handler(commands=['dua'])
def dua(message):
    dua_text = """🤲 রমজানের দোয়া:

اللهم إنك عفو تحب العفو فاعف عني

উচ্চারণ:
আল্লাহুম্মা ইন্নাকা আফুউন তুহিব্বুল আফওয়া ফা'ফু আন্নি
"""
    bot.reply_to(message, dua_text)

print("Bot running successfully...")
bot.infinity_polling()
