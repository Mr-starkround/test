import os
import logging

api_id = int(os.environ.get("API_ID", "21484185"))
api_hash = os.environ.get("API_HASH", "42589444b3ee86b1286f01d966989214")
bot_token = os.environ.get("BOT_TOKEN", "6872017467:AAFx_RzH9bGA13iolTAYJNJlDWUfLjQ_C14")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://Alexa:alexa@cluster0.h0zqfue.mongodb.net/true?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "telegram")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1002089195394"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1002098707945"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1002088952110"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "6725628980"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "5"))
batas_talent = int(os.environ.get("BATAS_TALENT", "10"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "10"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "80"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "70"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "60"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "50"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "40"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "30"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#mas #mba #spill #tanya #story").replace(" ", "|").lower()
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Kamu harus bergabung di Channel & Group terlebih dahulu untuk mengirim pesan ke channel @Jawafes. \n\nSilakan Join Ke Channel & Group dulu ⤵️")
start_msg = os.environ.get("START_MSG", """
❏ Haii {mention}

𝗝𝗮𝘄𝗮𝗳𝗲𝘀𝘀 𝗔𝘂𝘁𝗼 𝗽𝗼𝘀𝘁 akan membantumu mengirimkan pesan secara anonim ke channel @JAWAFES.

<b>silahkan baca help dan rules terlebih dahulu</b>""")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
🙅‍♂️Pesanmu gagal terkirim.
<b>silahkan baca help untuk menggunakan bot ini</b>
async def cb_help(client, callback_query):
    user_id = callback_query.from_user.id
    buttons = [
        [
            InlineKeyboardButton(
                "ᴛᴜᴛᴜᴘ", callback_data="ttp"
            ),
            InlineKeyboardButton(
                "ʀᴜʟᴇs", url="https://t.me/jawafes/9"
            ),
        ],
    ]
    await callback_query.edit_message_text(
        f"""
<b>Silahkan kirim pesan anda menggunakan hashtag dibawah ini:</b>

• <code>#mba</code> [ untuk identitas perempuan]
• <code>#mas</code> [ untuk identitas laki-laki ]
• <code>#spill</code> [ untuk spill masalah ]
• <code>#tanya</code> [ untuk bertanya ]
• <code>#story</code> [ untuk berbagi cerita/curhat ]

<b>Contoh pesan:</b> <code>#mas gabut banget gasi? callan yuk </code>
""",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


async def cb_close(client, callback_query):
    await callback_query.message.delete()
""")
