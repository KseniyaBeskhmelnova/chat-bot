from bot.handler import Handler  # убедитесь, что путь правильный
import bot.database_client  # ваш модуль с persist_updates

class DatabaseLogger(Handler):
    def can_handle(self, update: dict) -> bool:
        return True

    def handle(self, update: dict) -> bool:
        bot.database_client.persist_updates([update])
        return True