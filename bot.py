Enterimport requests
import time
from telegram import Bot

TOKEN = "7810387520:AAGrVilsofjdGXxLGVRe5LRibuTHGfIgJc0"
CHAT_ID = 7105436949
API_URL = "http://127.0.0.1:5000/sms"  # غيّر لو الـ endpoint مختلف

bot = Bot(token=TOKEN)
last_id = None

print("البوت شغال...")

while True:
    try:
        r = requests.get(API_URL)
        data = r.json()
        sms = data.get("sms", []) if "sms" in data else []
        for msg in sms:
            mid = msg.get("id")
            if mid and (last_id is None or mid > last_id):
                num = msg.get("number", "?")
                txt = msg.get("text", "?")
                bot.send_message(CHAT_ID, f"🆕 OTP جديد!\nرقم: {num}\nرسالة: {txt}")
                last_id = mid
    except Exception as e:
        print("خطأ:", e)
    time.sleep(10)
