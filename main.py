from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import dotenv
import os
import asyncio
import counter
dotenv.load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()
chat_id = int(os.getenv('CHAT_ID'))

cc = counter.PallasCounter(start_value=int(os.getenv('START_VALUE')))


@dp.message(Command('manul'))
async def handle_manul(msg: Message):
    if msg.chat.id != chat_id or msg.from_user.is_bot:
        return

    if cc.try_increment(msg.from_user.id):
        await bot.send_message(msg.chat.id, text=f'{str(cc)}')


async def main():
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    asyncio.run(main())
