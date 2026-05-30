from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import requests

TOKEN = "8907532686:AAFXbyH9BRi83JHCnX78iGB6b1tTueSc0Ow"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 خوش آمدی\n\n📥 لینک اینستا یا 🎵 اسم آهنگ بفرست"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "instagram.com" in text:
        await update.message.reply_text("📥 دانلود اینستا مرحله بعد وصل میشه")

    else:
        url = f"https://itunes.apple.com/search?term={text}&limit=1"
        r = requests.get(url).json()

        if r["resultCount"] > 0:
            song = r["results"][0]["trackName"]
            artist = r["results"][0]["artistName"]
            await update.message.reply_text(
                f"🎵 پیدا شد!\n\n🎤 {artist}\n🎶 {song}"
            )
        else:
            await update.message.reply_text("❌ آهنگ پیدا نشد")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
