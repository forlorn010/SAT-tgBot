from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import BotCommand, CallbackQuery, MenuButtonCommands, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from db import set_user_and_language
from locales.locales import cache_user_language
start_router = Router()

# Commands' menu setup
async def set_menu(bot):
    await bot.set_chat_menu_button(menu_button=MenuButtonCommands(type='commands'))


async def set_commands(bot):
    await bot.set_my_commands([
        BotCommand(command='start', description='Start the bot - Запустить бота'),
    ])

    
# /start handler - language selection
@start_router.message(CommandStart())
async def show_language_choose_manu(message: Message):
    languages_keyboard = InlineKeyboardBuilder()
    languages_keyboard.button(text='English🇬🇧', callback_data=f'{message.from_user.id}:language_selection_en')
    languages_keyboard.button(text='Русский🇷🇺', callback_data=f'{message.from_user.id}:language_selection_ru')

    await message.answer('Hello!👋 Choose the language you want to use:\nПривет!👋 Выбери язык, который хочешь использовать:'
                            , reply_markup=languages_keyboard.as_markup())
    

@start_router.callback_query(F.data.endswith(':language_selection_en'))
async def language_selection_en(callback: CallbackQuery):
    user_id, language = callback.data.split(':')
    user_id = int(user_id)
    lang_code = language[-2:]  # 'en' or 'ru'
    
    # Save to database
    await set_user_and_language(user_id, lang_code)
    
    # Cache in Redis
    await cache_user_language(user_id, lang_code)


@start_router.callback_query(F.data.endswith(':language_selection_ru'))
async def language_selection_ru(callback: CallbackQuery):
    user_id, language = callback.data.split(':')
    user_id = int(user_id)
    lang_code = language[-2:]  # 'en' or 'ru'
    
    # Save to database
    await set_user_and_language(user_id, lang_code)
    
    # Cache in Redis
    await cache_user_language(user_id, lang_code)