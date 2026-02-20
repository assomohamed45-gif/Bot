import telebot

# ضع التوكن الخاص ببوتك هنا
TOKEN = "8535032509:AAFQ3V_RKYval-EmUoNtj9x6xt0WX6zhtTg"  # استبدل هذا النص بالتوكن الخاص بك

# تهيئة البوت
bot = telebot.TeleBot(TOKEN)

# معالج أمر /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "اهلا وسهلا")

# تشغيل البوت
if __name__ == "__main__":
    print("البوت يعمل بنجاح...")
    bot.infinity_polling()