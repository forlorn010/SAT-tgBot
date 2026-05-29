from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from locales.locales import t, get_user_language_cached

main_menu_router = Router()

@main_menu_router.callback_query(F.data.endswith('main_menu'))
async def show_main_menu(callback: CallbackQuery):
    main_menu_keyboard = InlineKeyboardBuilder()
    lang = await get_user_language_cached(callback.from_user.id)

    main_menu_keyboard.button(
        text=f"{t(lang, 'random_problem')} 🎲",
        callback_data="menu:random_problem")

    main_menu_keyboard.button(
        text=f"{t(lang, 'customize')} ⚙️",
        callback_data="menu:customize")

    # settings and info side-by-side
    main_menu_keyboard.button(
        text=f"{t(lang, 'settings')} 🛠️",
        callback_data="menu:settings")

    main_menu_keyboard.button(
        text=f"{t(lang, 'info_bot')} ℹ️",
        callback_data="menu:info_bot")

    # layout: one button per row for first two, then two buttons on final row
    main_menu_keyboard.adjust(1, 1, 2)

    await callback.message.answer(t(lang, 'main_menu_text'), reply_markup=main_menu_keyboard.as_markup())
    await callback.answer()