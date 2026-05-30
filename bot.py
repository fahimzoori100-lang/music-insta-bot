from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN ="8907532686:AAFXet1xTijW4ssNxOkQ02oL10XnN_Z2K60"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 خوش آمدی!\n\n"
        "لینک اینستاگرام یا اسم آهنگ را بفرست."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "instagram.com" in text:
        await update.message.reply_text("📥 لینک اینستا دریافت شد")
    else:
        await update.message.reply_text(f"🎵 در حال جستجوی موزیک: {text}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot is running...")
app.run_polling()
