import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "fitbuddy.db"


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            user_id TEXT NOT NULL,
            age INTEGER NOT NULL,
            weight REAL NOT NULL,
            goal TEXT NOT NULL,
            intensity TEXT NOT NULL,
            original_plan TEXT,
            updated_plan TEXT
        )
    """)

    connection.commit()
    connection.close()


def add_user(
    name,
    user_id,
    age,
    weight,
    goal,
    intensity,
    original_plan
):
    connection = get_connection()

    cursor = connection.execute("""
        INSERT INTO users
        (
            name,
            user_id,
            age,
            weight,
            goal,
            intensity,
            original_plan
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        name,
        user_id,
        age,
        weight,
        goal,
        intensity,
        original_plan
    ))

    connection.commit()

    new_id = cursor.lastrowid

    connection.close()

    return new_id


def get_user(user_id):
    connection = get_connection()

    user = connection.execute(
        """
        SELECT * FROM users
        WHERE user_id = ?
        """,
        (user_id,)
    ).fetchone()

    connection.close()

    return user


def get_all_users():
    connection = get_connection()

    users = connection.execute(
        """
        SELECT * FROM users
        ORDER BY id DESC
        """
    ).fetchall()

    connection.close()

    return users


def update_user_plan(user_id, updated_plan):
    connection = get_connection()

    connection.execute(
        """
        UPDATE users
        SET updated_plan = ?
        WHERE user_id = ?
        """,
        (updated_plan, user_id)
    )

    connection.commit()
    connection.close()