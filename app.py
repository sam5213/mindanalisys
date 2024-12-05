import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

dp = Dispatcher()  
    
@dp.message(CommandStart())
async def command_google_handler(message: Message) -> None:
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Заказать разбор", web_app=WebAppInfo(url="https://mind-analysis.tilda.ws/")),
            ],
        ],
    )
    await message.answer(f"Здравствуйте, {html.bold(message.from_user.full_name)}! 👋" + "\n\n" +
                         "Рада, что вы решили узнать больше о своем соционическом типе, " +
                         "рекомендую посетить наш сайт перейдя по кнопке ниже. Там вы найдете квалифицированных " +
                         "специалистов, которые проведут для вас тестирование и дадут подробные " +
                         "консультации по результатам. 👇" + "\n\n" +
                         "Наши эксперты помогут вам понять свои сильные стороны, предпочтения " +
                         "в общении и работе, а также предложат рекомендации по развитию личных " +
                         "качеств. Записывайтесь на консультацию, чтобы сделать первый шаг к лучшему " + 
                         "пониманию себя и окружающих! " + "\n\n" +
                         "Ждем вас на типировании! 🫶", reply_markup=markup)   


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
