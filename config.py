import os
import logging

api_id = int(os.environ.get("API_ID", "21484185"))
api_hash = os.environ.get("API_HASH", "42589444b3ee86b1286f01d966989214")
bot_token = os.environ.get("BOT_TOKEN", "6872017467:AAEQAC59qKPm-6ML27z44DjLwZeCzx-wpVk")
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

hastag = os.environ.get("HASTAG", "#mas #mba #spill #tanya #story #pap").replace(" ", "|").lower()
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Kamu harus bergabung di Channel & Group terlebih dahulu untuk mengirim pesan ke channel @Jawafes. \n\nSilakan Join Ke Channel & Group dulu ⤵️")
start_msg = os.environ.get("START_MSG", "Haii {mention}
<b>silahkan kirim pesan anda menggunakan hashtag:</b>

• #mba [ untuk identitas perempuan]
• #mas [ untuk identitas laki-laki ]
• #spill [ untuk spill masalah ]
• #tanya [ untuk bertanya ]
• #story [ untuk berbagi cerita/curhat ]
• #pap [ khusus media foto/video ]

<b>Contoh pesan:</b> <code>#mas yang dari jogja. meet yuk {username} </code>

<b>pastikan kamu sudah baca <a href="https://t.me/JAWAFES/9">rules</a> dan <a href="https://t.me/JAWAFES/10">help</a> terlebih dahulu</b>")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
❌ Pesanmu gagal terkirim {mention}, silahkan baca <a href="https://t.me/JAWAFES/10">help</a> untuk menggunakan bot ini
""")
