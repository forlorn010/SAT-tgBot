import aiosqlite

DB_NAME = "bot_data_base.db"

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


async def get_user_language(user_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT user_language FROM users WHERE user_id = ?", (user_id,)) as cursor:
            row = await cursor.fetchone()
            if row:
                return row[0]
            else:
                return 'en' 