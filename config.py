import os
import logging

api_id = int(os.environ.get("API_ID", "22132140"))
api_hash = os.environ.get("API_HASH", "326ba61167a7513e85c9d8699b345b75")
bot_token = os.environ.get("BOT_TOKEN", "6985345708:AAGIbUsvwDBBGPHYAJjpWLCq7Oz9cxQ3odo")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://Alexa:alexa@cluster0.h0zqfue.mongodb.net/true?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "telegram")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001935857563"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001869711042"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1002015387015"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "1020381855"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "5"))
batas_talent = int(os.environ.get("BATAS_TALENT", "10"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "25"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "80"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "70"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "60"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "50"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "40"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "30"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#pap | #mas | #mba | #spill | #tanya | #story").replace(" ", "|").lower()
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Kamu harus bergabung di Channel & Group terlebih dahulu untuk mengirim pesan ke channel @JAWAFES. \n\nSilakan Join Ke Channel & Group dulu ⤵️")
start_msg = os.environ.get("START_MSG", """
❏ Haii {mention}

𝗝𝗮𝘄𝗮𝗳𝗲𝘀𝘀 𝗔𝘂𝘁𝗼 𝗽𝗼𝘀𝘁 akan membantumu mengirimkan pesan secara anonim ke channel @JAWAFES.

<b>silahkan baca help dan rules terlebih dahulu</b>""")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
🙅‍♂️Pesanmu gagal terkirim.

<b>silahkan klik /start dan baca help untuk menggunakan bot ini</b>
""")
