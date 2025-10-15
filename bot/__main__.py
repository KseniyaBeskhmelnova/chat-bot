from bot.dispatcher import Dispatcher
from bot.handlers.message_echo import MessageEcho
from bot.handlers.db_logger import DatabaseLogger
from bot.handlers.photo_echo import PhotoEcho
from bot.handlers.sticker_echo import StickerEcho
from bot.long_polling import start_long_polling

if __name__ == "__main__":
    try:
        dispatcher = Dispatcher()
        dispatcher.add_handler(DatabaseLogger())
        dispatcher.add_handler(MessageEcho())
        dispatcher.add_handler(PhotoEcho())
        dispatcher.add_handler(StickerEcho())
        start_long_polling(dispatcher)

    except KeyboardInterrupt:
        print("\nBye!")