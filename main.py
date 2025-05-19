from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("مرحبًا بك في بوت طارق بابا!")

app = ApplicationBuilder().token("8199590505:AAGxPvaO1O8TZHsdsZ5TcYiRkmNnP4s8dME").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
