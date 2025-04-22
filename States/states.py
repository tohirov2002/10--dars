from aiogram.fsm.state import State,StatesGroup

class AddTask(StatesGroup):
    task_name = State()

