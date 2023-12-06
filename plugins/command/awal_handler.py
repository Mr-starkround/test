import config

from pyrogram.errors import *
from pyrogram.types import *

from pyrogram import Client, types, enums
from plugins import Helper, Database


async def start_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    first = msg.from_user.first_name
    last = msg.from_user.last_name
    fullname = f'{first} {last}' if last else first
    username = (
        f'@{msg.from_user.username}'
        if msg.from_user.username
        else '@vxnjul'
    )
    mention = msg.from_user.mention
    buttons = [
        [
            InlineKeyboardButton(
                "ʜᴇʟᴘ", callback_data="nsj"
            ),
            InlineKeyboardButton(
                "ʀᴜʟᴇs", url="https://t.me/jawafes/9"
            ),
        ],
    ]
    await msg.reply_text(
        text=config.start_msg.format(
            id=msg.from_user.id,
            mention=mention,
            username=username,
            first_name=await helper.escapeHTML(first),
            last_name=await helper.escapeHTML(last),
            fullname=await helper.escapeHTML(fullname),
        ),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True
    )

async def status_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    db = Database(msg.from_user.id).get_data_pelanggan()
    pesan = '<b>🏷Info user</b>\n'
    pesan += f'├ID : <code>{db.id}</code>\n'
    pesan += f'├Nama : {db.mention}\n'
    pesan += f'└Status : {db.status}\n\n'
    pesan += '<b>📝Lainnya</b>\n'
    pesan += f'├Coin : {helper.formatrupiah(db.coin)}💰\n'
    pesan += f'├Menfess : {db.menfess}/{config.batas_kirim}\n'
    pesan += f'├Semua Menfess : {db.all_menfess}\n'
    pesan += f'└Bergabung : {db.sign_up}'
    await msg.reply(pesan, True, enums.ParseMode.HTML)

async def statistik_handler(client: Helper, id_bot: int):
    db = Database(client.user_id)
    bot = db.get_data_bot(id_bot)
    pesan = "<b>📊 STATISTIK BOT\n\n"
    pesan += f"▪️Pelanggan: {db.get_pelanggan().total_pelanggan}\n"
    pesan += f"▪️Admin: {len(bot.admin)}\n"
    pesan += f"▪️Talent: {len(bot.talent)}\n"
    pesan += f"▪️Daddy sugar: {len(bot.daddy_sugar)}\n"
    pesan += f"▪️Moans girl: {len(bot.moansgirl)}\n"
    pesan += f"▪️Moans boy: {len(bot.moansboy)}\n"
    pesan += f"▪️Girlfriend rent: {len(bot.gfrent)}\n"
    pesan += f"▪️Boyfriend rent: {len(bot.bfrent)}\n"
    pesan += f"▪️Banned: {len(bot.ban)}\n\n"
    pesan += f"🔰Status bot: {'AKTIF' if bot.bot_status else 'TIDAK AKTIF'}</b>"
    await client.message.reply_text(pesan, True, enums.ParseMode.HTML)

async def list_admin_handler(helper: Helper, id_bot: int):
    db = Database(helper.user_id).get_data_bot(id_bot)
    pesan = "<b>Owner bot</b>\n"
    pesan += "• ID: " + str(config.id_admin) + " | <a href='tg://user?id=" + str(config.id_admin) + "'>Owner bot</a>\n\n"
    if len(db.admin) > 0:
        pesan += "<b>Daftar Admin bot</b>\n"
        ind = 1
        for i in db.admin:
            pesan += "• ID: " + str(i) + " | <a href='tg://user?id=" + str(i) + "'>Admin " + str(ind) + "</a>\n"
            ind += 1
    await helper.message.reply_text(pesan, True, enums.ParseMode.HTML)

async def list_ban_handler(helper: Helper, id_bot: int):
    db = Database(helper.user_id).get_data_bot(id_bot)
    if len(db.ban) == 0:
        return await helper.message.reply_text('<i>Tidak ada user dibanned saat ini</i>', True, enums.ParseMode.HTML)
    else:
        pesan = "<b>Daftar banned</b>\n"
        ind = 1
        for i in db.ban:
            pesan += "• ID: " + str(i) + " | <a href='tg://openmessage?user_id=" + str(i) + "'>( " + str(ind) + " )</a>\n"
            ind += 1
    await helper.message.reply_text(pesan, True, enums.ParseMode.HTML)

async def gagal_kirim_handler(client: Client, msg: types.Message):
    anu = Helper(client, msg)
    first_name = msg.from_user.first_name
    last_name = msg.from_user.last_name
    fullname = first_name if not last_name else first_name + ' ' + last_name
    username = '@vxnjul' if not msg.from_user.username else '@' + msg.from_user.username
    mention = msg.from_user.mention
    return await msg.reply(config.gagalkirim_msg.format(
        id = msg.from_user.id,
        mention = mention,
        username = username,
        first_name = await anu.escapeHTML(first_name),
        last_name = await anu.escapeHTML(last_name),
        fullname = await anu.escapeHTML(fullname)
    ), True, enums.ParseMode.HTML, disable_web_page_preview=True)

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
📝Cara mengirim menfess di 𝗝𝗮𝘄𝗮𝗳𝗲𝘀𝘀 𝗔𝘂𝘁𝗼 𝗣𝗼𝘀𝘁?

1. Wajib subscribe @JAWA_GRUP dan @JAWAFES.
2. Gunakan #hashtag dalam daftar di bawah ini :
• #mba [ untuk identitas perempuan]
• #mas [ untuk identitas laki-laki ]
• #spill [ untuk spill masalah ]
• #tanya [ untuk bertanya ]
• #story [ untuk berbagi cerita/curhat ]
3. Kirim pesan anda di @JAWAFESSBOT minimal 3 kata.
4. Sekarang anda telah berhasil mengirim pesan di @JAWAFES.

<b>Contoh pesan:</b> <code>yang dari jogja. meet yuk #mba</code>

<b>CATATAN PENTING:</b> Semua postingan di channel @JAWAFES adalah postingan dari para member yang menggunakan @JAWAFESSBOT. Jika ada yang melanggar rules atau merugikan kalian di channel ini, silahkan chat @vxnjul untuk membantu menghapus dan membanned orang yang melakukannya.

<b>👮‍♂️ADMIN MEMILIKI HAK UNTUK BLOCK SENDER/TAKEDOWN MENFESS/SPILL SENDER.</b>
""",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


async def cb_close(client, callback_query):
    await callback_query.message.delete()
