from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import openai
import random
import os

# --- Load keys from environment variables ---
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

def ai_fun_reply(user_text):
    # Random chance for edgy/18+ reply
    edgy_chance = random.randint(1, 10)
    if edgy_chance <= 2:
        prompt = f"""
        তুমি একজন মজার এবং একটু হট / 18+ ব্যক্তি। 
        শুধু ফানি এবং ফ্রি স্টাইল মেসেজ পাঠাও। 
        বাংলা ভাষায় মজার, একটু 18+ ধরনের উত্তর দাও। 
        ব্যবহারকারীর মেসেজ: "{user_text}"
        """
    else:
        prompt = f"""
        তুমি একজন মজার বন্ধু। 
        শুধু ফানি মেসেজ পাঠাবে। 
        বাংলা ভাষায় মজার, প্লে-ফুল উত্তর দাও। 
        ব্যবহারকারীর মেসেজ: "{user_text}"
        """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=120
    )
    return response.choices[0].message['content']

def handle_message(update: Update, context: CallbackContext):
    user_text = update.message.text
    reply = ai_fun_reply(user_text)
    update.message.reply_text(reply)

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    print("@Tisha_Reply_Bot is running...")
    updater.idle()

if __name__ == "__main__":
    main()