import telebot
import google.generativeai as genai

BOT_TOKEN = "8550956934:AAFKfQLioynxsFWJQDeREPPtM0Fy8cAj7M4"
GEMINI_API_KEY = "AIzaSyDzlsgt9Vl1oz9f-TbxtjVmwk-q5ReD-8U"

bot = telebot.TeleBot(BOT_TOKEN)

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

SYSTEM_PROMPT = """
You are DERAMA GPT.
You answer confidently, clearly, and helpfully.
You always refer to yourself as DERAMA GPT.
"""

@bot.message_handler(func=lambda message: True)
def reply(message):
    try:
        user_text = message.text

        response = model.generate_content(
            SYSTEM_PROMPT + "\nUser: " + user_text
        )

        bot.reply_to(message, response.text)

    except Exception as e:
        bot.reply_to(message, "DERAMA GPT متعب شوية، جرب تاني.")

bot.infinity_polling()
