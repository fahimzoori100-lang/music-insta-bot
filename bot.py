from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8907532686:AAFWf18vL2pPlc2Q0vS4Z2nfffIAZdD54fY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 خوش آمدی!\n\n📥 لینک اینستاگرام بفرست\n🎵 یا اسم آهنگ بفرست"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "instagram.com" in text:
        await update.message.reply_text("📥 لینک اینستا دریافت شد — دانلود مرحله بعد وصل میشه")
    else:
        await update.message.reply_text(
            f"🎵 آهنگ «{text}» پیدا نشد یا موزیک‌یاب هنوز وصل نشده"
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot running...")
app.run_polling()
