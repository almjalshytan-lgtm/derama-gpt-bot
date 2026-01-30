import telebot
import google.generativeai as genai
import os
import sys

# قراءة المفاتيح من Environment Variables
BOT_TOKEN = os.environ.get("BOT_TOKEN")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if not BOT_TOKEN or not GEMINI_API_KEY:
    print("❌ Missing environment variables")
    sys.exit(1)

# تهيئة البوت
bot = telebot.TeleBot(8550956934:AAFKfQLioynxsFWJQDeREPPtM0Fy8cAj7M4)

# تهيئة Gemini
genai.configure(AIzaSyDzlsgt9Vl1oz9f-TbxtjVmwk-q5ReD-8U)

model = genai.GenerativeModel(
    model_name="models/gemini-1.5-flash",
    generation_config={
        "temperature": 0.7,
        "max_output_tokens": 500
    }
)

SYSTEM_PROMPT = (
    "You are DERAMA GPT. "
    "You must always say that your name is DERAMA GPT. "
    "You answer clearly and helpfully in Arabic."
)

@bot.message_handler(func=lambda message: True)
def reply(message):
    try:
        prompt = SYSTEM_PROMPT + "\nUser: " + message.text
        response = model.generate_content(prompt)
        bot.reply_to(message, response.text)

    except Exception as e:
        print("❌ ERROR:", e)
        bot.reply_to(message, "DERAMA GPT واجه مشكلة تقنية.")

# تشغيل البوت
print("✅ DERAMA GPT is running...")
bot.infinity_polling(timeout=60, long_polling_timeout=60)
