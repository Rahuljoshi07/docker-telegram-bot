from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os, signal, sys

BOT_TOKEN = os.getenv("BOT_TOKEN")
app = ApplicationBuilder().token(BOT_TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Hello! I’m running inside Docker!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🛠 Available commands:\n/start - Welcome\n/help - List commands\n/info - About bot")

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📦 Telegram Docker Bot\n👨‍💻 Rahul Joshi\n🔗 github.com/Rahuljoshi07")

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("info", info))

def shutdown(signum, frame):
    print("🛑 Bot is shutting down...")
    sys.exit(0)

signal.signal(signal.SIGINT, shutdown)
signal.signal(signal.SIGTERM, shutdown)

if __name__ == '__main__':
    print("✅ Bot is up and running...")
    app.run_polling()
