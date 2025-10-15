from bot.handler import Handler
import bot.telegram_client

class StickerEcho(Handler):
    def can_handle(seld, update: dict) -> bool:
        return "message" in update and "sticker" in update["message"]

    def handle(seld, update: dict) -> bool:
        bot.telegram_client.sendSticker(
                        chat_id=update["message"]["chat"]["id"],
                        sticker_file_id=update["message"]["sticker"]["file_id"],
                    )
        return False
