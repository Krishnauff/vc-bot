from pyrogram.types import InlineKeyboardButton

import config

from AnonX.utils import time_to_sec

def stream_markup_timer(_, videoid, chat_id, played, dur):

    played_sec = time_to_sec(played)

    total_sec = time_to_sec(dur)

    x, y = str(round(played_sec/total_sec,1)).split(".")

    pos = int(y)

    line = "╌"

    circle = "✯"

    bar = line*(pos-1)

    bar += circle

    bar += line*(10-len(bar))

    buttons = [

        [

            InlineKeyboardButton(

                text=f"{played} {bar} {dur}",

                callback_data="GetTimer",

            )

        ],

        [

            InlineKeyboardButton(

                text="▷",

                callback_data=f"ADMIN Resume|{chat_id}",

            ),

            InlineKeyboardButton(

                text="II", callback_data=f"ADMIN Pause|{chat_id}"

            ),

            InlineKeyboardButton(

                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"

            ),

            InlineKeyboardButton(

                text="▢", callback_data=f"ADMIN Stop|{chat_id}"

            ),

        ],

        [

            InlineKeyboardButton(

                text="➕ ✨ ᴩʟᴀʏʟɪsᴛ ✨ ➕",

                callback_data=f"add_playlist {videoid}",

            ),

            InlineKeyboardButton(

                text="🥀 sᴜᴩᴩᴏʀᴛ🥀", url=config.SUPPORT_GROUP

            ),

        ],

        [

           InlineKeyboardButton(

                text="💝ᴏᴡɴᴇʀ💝", url=f"https://t.me/NO_LOVE_I_HATE_LOVE",

            ),

           InlineKeyboardButton(

                text="🌚𝐉𝐀𝐀𝐍🌝", url=f"https://t.me/Ajanabee_Duniya",

            ),

        ],

        [

            InlineKeyboardButton(

                text="✯ᴄʟᴏsᴇ ✯", callback_data="close"

            )

        ],

    ]

    return buttons

def telegram_markup_timer(_, chat_id, played, dur):

    played_sec = time_to_sec(played)

    total_sec = time_to_sec(dur)

    x, y = str(round(played_sec/total_sec,1)).split(".")

    pos = int(y)

    line = "—"

    circle = "◉"

    bar = line*(pos-1)

    bar += circle

    bar += line*(10-len(bar))

    

    buttons = [

        [

            InlineKeyboardButton(

                text=f"{played} {bar} {dur}",

                callback_data="GetTimer",

            )

        ],

        [

            InlineKeyboardButton(

                text="▷",

                callback_data=f"ADMIN Resume|{chat_id}",

            ),

            InlineKeyboardButton(

                text="II", callback_data=f"ADMIN Pause|{chat_id}"

            ),

            InlineKeyboardButton(

                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"

            ),

            InlineKeyboardButton(

             text="▢", callback_data=f"ADMIN Stop|{chat_id}"

            ),

        ],

        [

           InlineKeyboardButton(

                text="💝ᴏᴡɴᴇʀ💝", url=f"https://t.me/NO_LOVE_I_HATE_LOVE ",

            ),

           InlineKeyboardButton(

                text="🌚𝐉𝐀𝐀𝐍🌝", url=f"https://t.me/Ajanabee_Duniya",

            ),

        ],

        [

            InlineKeyboardButton(

                text="🥀 sᴜᴩᴩᴏʀᴛ🥀", url=config.SUPPORT_GROUP

            ),

            InlineKeyboardButton(

                text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"

            )

        ],

    ]

    return buttons

def track_markup(_, videoid, user_id, channel, fplay):

    buttons = [

        [

            InlineKeyboardButton(

                text=_["P_B_1"],

                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",

            ),

            InlineKeyboardButton(

                text=_["P_B_2"],

                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",

            ),

        ],




