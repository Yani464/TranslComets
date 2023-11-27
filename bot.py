import logging
import os
import asyncio


from aiogram import Bot, Dispatcher,types
from aiogram.filters.command import Command

from config import translit_dict

logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Hello,{user_name},веди свои ФИО через пробел на кириллице'
    logging.info(f'{user_name=} {user_id=} sent message: {message.text}')
    await message.reply(text)


@dp.message()
async def send_reply(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text1 = message.text
    logging.info(f'{user_name=} {user_id=} sent message: {message.text}')
    result = ''
    if len(text1.split())!=3:
        await bot.send_message(user_id,'Неправильные данные,попробуй еще раз')
    else:
        for i in text1.split():
                for j in i:
                    if j.isupper() == True:
                        if len(translit_dict[j.lower()]) > 1:
                            result += (translit_dict[j.lower()])[0].upper()
                            result += (translit_dict[j.lower()])[1:]
                        else:
                            result += (translit_dict[j.lower()]).upper()
                    else:
                        result+= translit_dict[j.lower()]
                result+= ' '
        
        await bot.send_message(user_id,result)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())   




