# Aiogram Bot Template

A clean and minimal template for building Telegram bots with **aiogram 3.x** and **SQLite** database.

## Features

- Built with **aiogram 3.x** (latest async framework)
- **SQLite** database with async support (aiosqlite)
- User registration system
- Admin commands with access control
- Clean project structure
- Easy to customize and extend

## Project Structure
```
bot_template/
├── data/
│   └── database.py          # Database operations
├── handlers/
│   ├── user_handlers.py     # User command handlers
│   └── admin_handlers.py    # Admin command handlers
├── bot.py                   # Main bot file
├── config.py                # Configuration & environment variables
├── .env                     # Environment variables (create this)
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/juipe/aiogram-minimal-template.git
cd bot_template
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create `.env` file
Create a `.env` file in the root directory:
```env
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
ADMIN_ID=123456789
```

**How to get your credentials:**
- `BOT_TOKEN`: Get it from [@BotFather](https://t.me/BotFather)

### 4. Run the bot
```bash
python bot.py
```

## Available Commands

### User Commands
- `/start` - Start the bot and register user
- `/help` - Show help message

### Admin Commands
- `/users` - Get total users count (admin only)

## Customization

### Adding new user commands
Edit `handlers/user_handlers.py`:
```python
@user_router.message(Command("mycommand"))
async def my_command_handler(message: Message):
    await message.answer("My custom response")
```

### Adding new admin commands
Edit `handlers/admin_handlers.py`:
```python
@admin_router.message(Command("myadmin"))
async def my_admin_handler(message: Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("Admin response")
```

### Modifying database schema
Edit `data/database.py` and update the `init_db_sql_script`:
```python
init_db_sql_script = """
CREATE TABLE IF NOT EXISTS bot_users (
    userid INTEGER PRIMARY KEY,
    username TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""
```

## Dependencies

- **aiogram** (3.25.0) - Telegram Bot API framework
- **aiosqlite** (0.22.1) - Async SQLite database
- **python-dotenv** (1.2.1) - Environment variables management

## Database

The bot uses SQLite database (`data/bot_users.db`) with the following schema:

**bot_users table:**
- `userid` (INTEGER PRIMARY KEY) - Telegram user ID
- `username` (TEXT) - Telegram username

## Security Notes

- Never commit your `.env` file to version control
- Keep your `BOT_TOKEN` secret
- Make sure to add `.env` and `data/*.db` to `.gitignore`

## Contributing

Feel free to fork this project and customize it for your needs!
