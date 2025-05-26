import sqlite3
from contextlib import contextmanager


@contextmanager
def conection_db():
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        yield cursor

        cursor.close()

        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        raise e

    finally:
        conn.close()
