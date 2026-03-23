import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from co import router

bot = Bot(token="7462015059:AAHvril2N88_zmQ15_Prv93o_rzgGH1PhpY")
dp = Dispatcher()
dp.include_router(router)

async def main():
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
from co_functions import _session        if _session and not _session.closed:
            await _session.close()

if __name__ == "__main__":
    asyncio.run(main())
