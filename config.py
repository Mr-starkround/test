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
biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "25"))

# =========================================================== #

hastag = os.environ.get("HASTAG", "#pap #mas | #mba #spill #tanya #story")
hastag = os.environ.get("HASTAG", "#mba #tanya")
hastag = os.environ.get("HASTAG", "#story #spill")
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Kamu harus bergabung di Channel & Group terlebih dahulu untuk mengirim pesan ke channel @JAWAFES. \n\nSilakan Join Ke Channel & Group dulu ⤵️")
start_msg = os.environ.get("START_MSG", """
❏ Haii {mention}

𝗝𝗮𝘄𝗮𝗳𝗲𝘀𝘀 𝗔𝘂𝘁𝗼 𝗽𝗼𝘀𝘁 akan membantumu mengirimkan pesan secara anonim ke channel @JAWAFES.

<b>silahkan baca help dan rules terlebih dahulu</b>""")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
pesan anda gagal terkirim. <b>silahkan klik button help bila butuh bantuan</b>
""")
