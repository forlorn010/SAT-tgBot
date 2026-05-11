import aiosqlite

DB_NAME = "bot_data_base.sql"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
                        CREATE TABLE IF NOT EXISTS users ( Id INTEGER PRIMARY KEY,
                            user_id INTEGER UNIQUE,
                            user_language TEXT )
                         """)
        await db.commit()


async def set_user_and_language(user_id: int, language: str):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("INSERT OR REPLACE INTO users (user_id, user_language) VALUES (?, ?)", (user_id, language))
        await db.commit()

