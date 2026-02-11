import aiosqlite

database_path = "data/bot_users.db" #Path to db file

init_db_sql_script = """
CREATE TABLE IF NOT EXISTS bot_users (
userid INTEGER PRIMARY KEY,
username TEXT
)
"""

async def init_database() -> bool: #Init database
    async with aiosqlite.connect(database_path) as db:
        try:
            await db.execute(init_db_sql_script) #Execute script
            await db.commit() #Save
            return True
        except aiosqlite.Error as e:
            print(f"database init error: {e}")
            return False

async def create_user(userdata: tuple) -> bool: #Create user func
    async with aiosqlite.connect(database_path) as db:
        try:
            await db.execute("INSERT INTO bot_users (userid, username) VALUES (?, ?)", userdata) #Exec script
            await db.commit() #Save
            return True
        except aiosqlite.IntegrityError:
            print("user already exists")
            return False
        except aiosqlite.Error as e:
            print(f"create user error: {e}")
            return False

async def get_total_users_count() -> int: #Total users func
    async with aiosqlite.connect(database_path) as db:
        try:
            async with db.execute("SELECT COUNT(*) FROM bot_users") as cursor:
                result = await cursor.fetchone()
                return result[0] if result else 0
        except aiosqlite.Error as e:
            print(f"get users count error: {e}")
            return 0