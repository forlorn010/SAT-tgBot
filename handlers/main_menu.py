from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from locales.locales import t, get_user_language_cached

main_menu_router = Router()

async def show_main_menu(user_id: int):
    main_menu_keyboard = InlineKeyboardBuilder()
    lang = await get_user_language_cached(user_id)
    main_menu_text = t(lang, 'main_menu_text')

    main_menu_keyboard.button(
        text=t(lang, 'random_problem'),
        callback_data="menu:random_problem")

    main_menu_keyboard.button(
        text=t(lang, 'customize'),
        callback_data="menu:customize")

    # settings and info side-by-side
    main_menu_keyboard.button(
        text=t(lang, 'settings'),
        callback_data="menu:settings")

    main_menu_keyboard.button(
        text=t(lang, 'info_bot'),
        callback_data="menu:info_bot")

    # layout: one button per row for first two, then two buttons on final row
    main_menu_keyboard.adjust(1, 1, 2)

    return main_menu_text,main_menu_keyboard.as_markup()