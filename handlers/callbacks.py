import asyncio
from aiogram import Router, F
from aiogram.types import CallbackQuery
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from db import set_user_and_language
from locales.locales import cache_user_language

callback_router = Router()

@callback_router.callback_query(F.data.endswith(':language_selection_en'))
async def language_selection_en(callback: CallbackQuery):
    user_id, language = callback.data.split(':')
    user_id = int(user_id)
    lang_code = language[-2:]  # 'en' or 'ru'
    
    # Save to database
    await set_user_and_language(user_id, lang_code)
    
    # Cache in Redis
    await cache_user_language(user_id, lang_code)


@callback_router.callback_query(F.data.endswith(':language_selection_ru'))
async def language_selection_ru(callback: CallbackQuery):
    user_id, language = callback.data.split(':')
    user_id = int(user_id)
    lang_code = language[-2:]  # 'en' or 'ru'
    
    # Save to database
    await set_user_and_language(user_id, lang_code)
    
    # Cache in Redis
    await cache_user_language(user_id, lang_code)



