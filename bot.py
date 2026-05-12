from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import InputFile

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

# =========================================
# BOT CONFIGURATION
# =========================================

BOT_TOKEN = "8708188945:AAFGF8ut5Ynnaz81K72cEStudZFxjoVR_aE"

OWNER_USERNAME = "@ShirshaDey39"

# =========================================
# PLAN DATA
# =========================================

PLANS = {
    "plan_10": {
        "name": "Demo Plan",
        "price": "₹10",
        "videos": "10 Videos"
    },

    "plan_25": {
        "name": "Starter Plan",
        "price": "₹25",
        "videos": "50 Videos"
    },

    "plan_50": {
        "name": "Premium Plan",
        "price": "₹50",
        "videos": "200 Videos"
    },

    "plan_100": {
        "name": "Ultimate Plan",
        "price": "₹100",
        "videos": "5000+ Videos with Daily Updates"
    }
}

# =========================================
# START COMMAND
# =========================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "₹10 - Demo Plan",
                callback_data="plan_10"
            )
        ],

        [
            InlineKeyboardButton(
                "₹25 - Starter Plan",
                callback_data="plan_25"
            )
        ],

        [
            InlineKeyboardButton(
                "₹50 - Premium Plan",
                callback_data="plan_50"
            )
        ],

        [
            InlineKeyboardButton(
                "₹100 - Ultimate Plan",
                callback_data="plan_100"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    text = (
        "🔥 Welcome to LateNightServices 🔥\n\n"
        "Select your preferred plan below:"
    )

    await update.message.reply_text(
        text=text,
        reply_markup=reply_markup
    )

# =========================================
# PLAN SELECTED
# =========================================

async def plan_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    selected_plan = PLANS[query.data]

    caption = (
        f"✅ Selected Plan: {selected_plan['name']}\n\n"
        f"💰 Amount: {selected_plan['price']}\n"
        f"🎬 Access: {selected_plan['videos']}\n\n"
        "📌 Payment Instructions:\n"
        "1. Scan the QR code below\n"
        "2. Complete payment using UPI / PhonePe\n"
        "3. Take screenshot after payment\n"
        f"4. Send screenshot to owner: {OWNER_USERNAME}\n\n"
        "🔒 After verification, you will receive "
        "private channel access."
    )

    try:

        with open("payment_qr.jpg", "rb") as qr:

            await query.message.reply_photo(
                photo=InputFile(qr),
                caption=caption
            )

    except FileNotFoundError:

        await query.message.reply_text(
            "❌ payment_qr.jpg file not found.\n"
            "Please place your QR image in the same folder."
        )

# =========================================
# MAIN FUNCTION
# =========================================

def main():

    print("🚀 Starting bot...")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CallbackQueryHandler(plan_selected)
    )

    print("✅ Bot is running...")

    app.run_polling()

# =========================================
# RUN BOT
# =========================================

if __name__ == "__main__":
    main()