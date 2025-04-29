from aiogram import Router,types,F
import logging


from database.db import update_task,get_task_id
from keyboards.keyboar_button import create_task_inline_kb, TASK_TOGGLE

button_router = Router()

@button_router.callback_query(F.data.startswith(TASK_TOGGLE))
async def button_hanler(callback: types.CallbackQuery):
    try:
        task_id_str = callback.data.split(TASK_TOGGLE)[1]
        task_id = int(task_id_str)
    except (IndexError,ValueError):
        await callback.answer("Xatolik notug'ri tugma malumoti",show_alert=True)
        logging.warning(f"Xatolik keldi {callback.data}")
        return
    user_id = callback.from_user.id
    
    current_task =  get_task_id(task_id,user_id)
    
    if not current_task:
        await callback.answer("Xatolik vazifa topuilmadi yoki sizda vazifa yuq",show_alert=True)
        try:
            await callback.message.edit_text("Bu vazifa uchirilgan yoki sizga tegishli emas")
        except Exception as e:
            logging.error("malumot uzgartirishda xatolik")
            return
    
    new_status = not current_task['is_done']
    
    javob =  update_task(task_id,new_status,user_id)
    
    if javob:
        status_icon = "✅" if new_status else "⏳"    
        new_text = f"{status_icon} {current_task['text']}" 
        new_keyboard =  create_task_inline_kb(task_id,new_status)
        try:
            await callback.message.edit_text(new_text,reply_markup=new_keyboard)
            await callback.answer(f"Vazifa holati {'bajarildi' if new_status else 'bekor qilindi'} ga o'zgardi")

        except Exception as e:
            logging.error(f"o'zgartirishda xatolik {e}")   
            await callback.answer("Tahrirlashda xatolik yuz berdi", show_alert=True)
    
    else:
        await callback.answer("Xatolik vazifa holatini yangilashda", show_alert=True)

