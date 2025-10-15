from bot.handler import Handler
import bot.telegram_client

class PhotoEcho(Handler):
    def can_handle(seld, update: dict) -> bool:
        return "message" in update and "photo" in update["message"]

    def handle(seld, update: dict) -> bool:
        bot.telegram_client.sendPhoto(
                        chat_id=update["message"]["chat"]["id"],
                        photo_file_id=update["message"]["photo"][-1]["file_id"],
                    )
        return False
