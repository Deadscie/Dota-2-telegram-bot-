from config_data.config import load_config
import asyncio
from aiogram import Bot, Dispatcher
from handlers import user_handlers


async def main():
    config = load_config(None)
    bot: Bot = Bot(token = config.tg_bot.token)
    dp : Dispatcher = Dispatcher()
    dp.include_router(user_handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
