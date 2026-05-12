import asyncio
from aiogram import Router, F
from aiogram.types import CallbackQuery
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from db import set_user_and_language

callback_router = Router()

@callback_router.callback_query(F.data.endswith(':language_selection_en'))
async def language_selection_en(callback: CallbackQuery):
    user_id, language = callback.data.split(':')
    await set_user_and_language(int(user_id), language[-2:])


@callback_router.callback_query(F.data.endswith(':language_selection_ru'))
async def language_selection_ru(callback: CallbackQuery):
    user_id, language = callback.data.split(':')
    await set_user_and_language(int(user_id), language[-2:])



