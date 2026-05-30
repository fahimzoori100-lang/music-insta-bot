from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8907532686:AAFWf18vL2pPlc2Q0vS4Z2nfffIAZdD54fY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
🔥 خوش آمدی به ربات 🔥

📥 لینک اینستاگرام بفرست تا دانلود کنم
🎵 یا اسم آهنگ بفرست تا موزیک پیدا کنم
"""
    await update.message.reply_text(text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text

    if "instagram.com" in msg:
        await update.message.reply_text("📥 لینک اینستا دریافت شد — دانلود بزودی اضافه میشه 🔥")
    else:
        await update.message.reply_text(f"🎵 در حال جستجوی موزیک: {msg}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot running...")
app.run_polling()
