import sqlite3
import logging


DATABASE_FILE = 'todo_list.db'

def init_db():
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tasks(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        task_text TEXT NOT NULL,
                        is_done INTEGER Default 0 NOT NULL CHECK(is_done in (0, 1))
                    )
                """)
            conn.commit()
            logging.info("Database mufaqqiyatli yaratildi")
    except sqlite3.Error as e:
        logging.error(f"Database initialized error: {e}")
        raise
    

def add_task_db(user_id: int, task_text: str):
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tasks(user_id,task_text) values(?,?)",(user_id,task_text))
            conn.commit()
            logging.info(f"Task muffaqiyatli qushildi {user_id} {task_text}")
            return cursor.lastrowid 
    except sqlite3.Error as e:
        logging.error(f"malumot qushilmadi {user_id} {e}")
        return None
    


def get_task(user_id: int):
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id,task_text,is_done FROM tasks WHERE user_id = ?", (user_id,)
            )
            tasks = cursor.fetchall()
            return [{'id': row[0], 'text': row[1], 'is_done': bool(row[2])} for row in tasks]
    except sqlite3.Error as e:
        logging.error(f"malumot olishda xatolik {user_id} {e}")
        return []
    
    
def update_task(task_id: int, is_done: bool, user_id: int):
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor =  conn.cursor()
            cursor.execute("UPDATE tasks SET is_done = ? WHERE id = ? AND user_id = ? ", (int(is_done),task_id,user_id))
            conn.commit()
            logging.info("Malumotlar muffaqiyatli yangilandi ")
            return cursor.rowcount > 0
    except sqlite3.Error as e:
        logging.error(f"malumot yangilashda xatolik {user_id} {e}")
        return False
    

def get_task_id(task_id: int, user_id: int):
    
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("Select id,task_text,is_done from tasks where id = ? and user_id = ?", (task_id,user_id))
            task_row = cursor.fetchone()
            if task_row:
                return {'id': task_row[0], 'text': task_row[1], 'is_done': bool(task_row[2])}
            else:
                return None
    except sqlite3.Error as e:
        logging.error(f"Xatolik {user_id} {e}")
        return None    
    