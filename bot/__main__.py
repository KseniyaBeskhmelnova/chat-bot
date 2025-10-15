import bot.database_client
import bot.telegram_client
import time

def main() -> None:
    next_update_offset = 0
    try:
        while True:
            updates = bot.telegram_client.getUpdates(offset=next_update_offset)
            bot.database_client.persist_updates(updates)
            for update in updates:
                next_update_offset = max(next_update_offset, update["update_id"] + 1)
                message = update.get("message", {})
                chat_id = message.get("chat", {}).get("id")
                if not chat_id:
                    continue
                if "text" in message:
                    bot.telegram_client.sendMessage(
                        chat_id=update["message"]["chat"]["id"],
                        text=update["message"]["text"],
                    )
                    print("T", end="", flush=True)
                elif "sticker" in message:
                    sticker_file_id = message["sticker"]["file_id"]
                    bot.telegram_client.sendSticker(
                        chat_id=chat_id,
                        sticker_file_id=sticker_file_id
                    )
                    print("S", end="", flush=True)

            time.sleep(1)
    except KeyboardInterrupt:
        print("\nBye!")

if __name__ == "__main__":
    main()