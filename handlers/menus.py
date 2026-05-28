import asyncio
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, MenuButtonCommands, BotCommand, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from locales.locales import t, get_user_language_cached
from redis.asyncio import Redis


#cache for user language
redis = Redis.from_url("redis://localhost:6379/0")

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
async def show_language_choose_manu(message: Message):
    languages_keyboard = InlineKeyboardBuilder()
    languages_keyboard.button(text='English🇬🇧', callback_data=f'{message.from_user.id}:language_selection_en')
    languages_keyboard.button(text='Русский🇷🇺', callback_data=f'{message.from_user.id}:language_selection_ru')

    await message.answer('Hello!👋 Choose the language you want to use:\nПривет!👋 Выбери язык, который хочешь использовать:'
                            , reply_markup=languages_keyboard.as_markup())


async def show_main_menu(callback: CallbackQuery):
    main_menu_keyboard = InlineKeyboardBuilder()
    main_menu_keyboard.button(text=t())
    