from aiogram import Bot, Dispatcher, executor, types


TOKEN_API = ""

HELP_COMMAND = """
/help - commands list
/start - work with bot
"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(command=["help"])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)


@dp.message_handler(command=["start"])
async def help_command(message: types.Message):
    await message.answer(text="WEEEEEELCOME!!")
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp)
