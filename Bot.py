from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# 🔐 Tokenni Railway'dan olamiz
TOKEN = os.getenv("TOKEN")

# 🟢 /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛏️ Surilarni rasm va narxlari bilan ko‘rish", url="https://yusufhorunov4-code.github.io/Marketplace-app/")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Xush kelibsiz!")
    await update.message.reply_text("Surilarni ko‘rish uchun quyidagi tugmani bosing 👇", reply_markup=reply_markup)

# 🔧 Botni ishga tushirish
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling(poll_interval=1)
