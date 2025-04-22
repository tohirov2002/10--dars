from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from database.db import get_task
from keyboards.keyboar_button import create_task_inline_kb

list_router = Router()

@list_router.message(Command("list"))
async def list_hanler(message: Message):
    user_id = message.from_user.id
    tasks = get_task(user_id)
    
    if not tasks:
        await message.answer("Sizda hali vazifa matnlari yo'q \n yangi vazifa qushish uchun /add buyrug'ini bosing")
        return
    await message.answer("Sizning vazifalaringiz: ")
    for  task in tasks:
          task_id = task['id']
          task_text = task['text']  
          is_done = task['is_done']
          
          status_icon = "✅" if is_done else "⏳"
          message_text =  f"{status_icon} {task_text}"
          keyboard = create_task_inline_kb(task_id,is_done)
          await message.answer(message_text,reply_markup=keyboard)
