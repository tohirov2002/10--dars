from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

start_router = Router()

@start_router.message(CommandStart())
async def start_hanler(message: Message):
    username = message.from_user.full_name
    await message.answer(
        f"Assalomu alaykum {username} Botimizga xush kelibsiz\n\n"
        f"Hurmatli foydalanuvchi sizga men kunlik vazifalaringizni tartiblash haqida urgataman \n"
        f"/add yani bu buyruq vazifa kiritish uchun \n"
        f"/list yani bu buyruq vazifani ro'yxatini kurish uchun"
    )