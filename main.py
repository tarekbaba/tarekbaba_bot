from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from dotenv import load_dotenv
load_dotenv("config.env")
token = os.getenv("TELEGRAM_TOKEN")
app = ApplicationBuilder().token(token).build()
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
await update.message.reply_text("مرحباً بك في بوت طارق بابا!"
app.add_handler(CommandHandler("start", start))
app.run_polling()
