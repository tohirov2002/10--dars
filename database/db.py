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
    
    
    