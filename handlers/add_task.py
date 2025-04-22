from aiogram import Router,F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


from States.states import AddTask
from database.db import add_task_db

add_router = Router()


@add_router.message(Command("add"))
async def add_hanler(message: Message, state: FSMContext):
    await message.answer("Vazifangizni kiriting: ")
    await state.set_state(AddTask.task_name)
    

@add_router.message(AddTask.task_name, F.text)
async def task_name_hanler(message: Message, state: FSMContext):
    task_text = message.text
    user_id =  message.from_user.id
    
    if not task_text:
        await message.answer(" ❌ Vazifa matningiz bush bulishi mumkun emas")
        return
    task_id  = add_task_db(user_id,task_text)
    if task_id:
        await message.answer(f"✅ Vazifa Muffaqiyatli qushildi: siz kiritgan vazifangiz --> {task_text}")
    else:
        await message.answer("❌ Vazifa qushishda xatolik bor")

    await state.clear()
    

@add_router.message(AddTask.task_name)
async def invalid_handler(message: Message):
    await message.answer("Kechirasiz vazifaga faqat matn kirita olasiz")
    
    
    

    
    
    