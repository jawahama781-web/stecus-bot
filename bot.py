from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8849350053:AAGEYSKeI-MvHK3o_bdVNCzVUIEBo_cHErw"
ADMIN = "@stecussssssss"
DANA = "0859-2796-9387"

HARGA = {
    "5": "Rp 2.000",
    "11": "Rp 4.000",
    "27": "Rp 8.000",
    "86": "Rp 21.000",
    "172": "Rp 41.000",
    "257": "Rp 61.000",
    "344": "Rp 81.000",
    "429": "Rp 101.000",
    "514": "Rp 121.000",
    "706": "Rp 162.000",
    "878": "Rp 201.000",
    "1049": "Rp 242.000",
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💎 Diamond ML", callback_data="menu_diamond")],
        [InlineKeyboardButton("💳 Metode Pembayaran", callback_data="bayar")],
        [InlineKeyboardButton("📞 Hubungi Admin", callback_data="admin")],
    ]
    await update.message.reply_text(
        "👋 Selamat datang di *STECUS STORE*!\n\nTop Up Diamond ML Murah, Cepat & Aman 💎\n\nSilahkan pilih menu di bawah:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "menu_diamond":
        keyboard = []
        for dm, harga in HARGA.items():
            keyboard.append([InlineKeyboardButton(f"💎 {dm} Diamond - {harga}", callback_data=f"beli_{dm}")])
        keyboard.append([InlineKeyboardButton("⬅️ Kembali", callback_data="back")])
        await query.edit_message_text("💎 *DAFTAR HARGA DIAMOND ML*\n\nPilih nominal yang mau kamu beli:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
    elif query.data == "back":
        keyboard = [
            [InlineKeyboardButton("💎 Diamond ML", callback_data="menu_diamond")],
            [InlineKeyboardButton("💳 Metode Pembayaran", callback_data="bayar")],
            [InlineKeyboardButton("📞 Hubungi Admin", callback_data="admin")],
        ]
        await query.edit_message_text("👋 Selamat datang di *STECUS STORE*!\n\nTop Up Diamond ML Murah, Cepat & Aman 💎\n\nSilahkan pilih menu di bawah:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
    elif query.data == "bayar":
        keyboard = [[InlineKeyboardButton("⬅️ Kembali", callback_data="back")]]
        await query.edit_message_text(f"💳 *METODE PEMBAYARAN*\n\n• DANA: `{DANA}`\nAtas nama: STECUS STORE\n\nSetelah transfer, kirim bukti ke {ADMIN} ya!", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
    elif query.data == "admin":
        keyboard = [[InlineKeyboardButton("⬅️ Kembali", callback_data="back")]]
        await query.edit_message_text(f"📞 *HUBUNGI ADMIN*\n\nChat admin di sini: {ADMIN}\n\nAdmin fast respon ya!", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
    elif query.data.startswith("beli_"):
        dm = query.data.replace("beli_", "")
        harga = HARGA[dm]
        keyboard = [[InlineKeyboardButton("✅ Saya Mau Beli", callback_data=f"order_{dm}")], [InlineKeyboardButton("⬅️ Kembali ke Daftar Harga", callback_data="menu_diamond")]]
        await query.edit_message_text(f"💎 *{dm} Diamond ML*\n\nHarga: *{harga}*\nProses: 1-5 Menit\n\nCara order:\n1. Transfer ke DANA `{DANA}`\n2. Kirim ID + bukti ke admin", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
    elif query.data.startswith("order_"):
        dm = query.data.replace("order_", "")
        harga = HARGA[dm]
        keyboard = [[InlineKeyboardButton("⬅️ Kembali", callback_data="menu_diamond")]]
        await query.edit_message_text(f"✅ *ORDER BERHASIL DIBUAT!*\n\nPesanan: *{dm} Diamond - {harga}*\n\n1. Transfer ke DANA: `{DANA}`\n2. Kirim format ini ke admin {ADMIN}:\n\n`ORDER {dm} Diamond\nID: \nServer: \nNama di Game: `\n\nJangan lupa kirim bukti transfer!", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("Bot jalan...")
    app.run_polling(close_loop=False)

if __name__ == "__main__":
    main()
