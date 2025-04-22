from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

TASK_TOGGLE = 'toggle_'


def create_task_inline_kb(task_id: int, is_done: bool) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    button_text = "Bajarildi" if not is_done else "Bekor qilish"
    builder.add(InlineKeyboardButton(
        text=button_text,
        callback_data=f"{TASK_TOGGLE} {task_id}"
        ))
    return builder.as_markup()


