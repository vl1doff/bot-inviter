import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("8813390776:AAEoJI23IalTELd5P5DIkhfUEmWC1G3mRjY")
CHAT_ID = -1003122424251

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Бот активен. Используй /invite")

async def invite(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != CHAT_ID:
        await update.message.reply_text("❌ Не та группа")
        return
    url = f"https://api.telegram.org/bot{TOKEN}/exportChatInviteLink"
    resp = requests.post(url, data={"chat_id": CHAT_ID})
    data = resp.json()
    if data.get("ok"):
        await update.message.reply_text(f"✅ Ссылка:\n{data['result']}")
    else:
        await update.message.reply_text(f"❌ Ошибка: {data.get('description')}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("invite", invite))
    app.run_polling()

if __name__ == "__main__":
    main()
