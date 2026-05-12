import asyncio
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, MenuButtonCommands, BotCommand
from aiogram.utils.keyboard import InlineKeyboardBuilder

command_router = Router()

# Commands' menu setup
async def set_menu(bot):
    await bot.set_chat_menu_button(menu_button=MenuButtonCommands(type='commands'))


async def set_commands(bot):
    await bot.set_my_commands([
        BotCommand(command='start', description='Start the bot - Запустить бота'),
    ])


# /start handler - language selection
@command_router.message(Command('start'))
async def start(message: Message):
    languages_keyboard = InlineKeyboardBuilder()
    languages_keyboard.button(text='English🇬🇧', callback_data=f'{message.from_user.id}:language_selection_en')
    languages_keyboard.button(text='Русский🇷🇺', callback_data=f'{message.from_user.id}:language_selection_ru')

    await message.answer('Hello!👋 Choose the language you want to use:\nПривет!👋 Выбери язык, который хочешь использовать:'
                            , reply_markup=languages_keyboard.as_markup())
                         