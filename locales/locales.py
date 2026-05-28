import json
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from db import get_user_language
from redis.asyncio import Redis
from config import REDIS_PASSWORD

redis = Redis.from_url(f"redis://:{REDIS_PASSWORD}@localhost:6379/0")

def load_languages():
    global languages
    languages = {}
    for lang in ['en', 'ru']:
        with open(f'locales/{lang}.json', 'r', encoding='utf-8') as f:
            languages[lang] = json.load(f)


async def cache_user_language(user_id: int, language: str):
    await redis.setex(f"user_language:{user_id}", 86400, language)


# Middleware to get user language from Redis or Database
async def get_user_language_cached(user_id: int) -> str:

    # Try to get from Redis
    cached_language = await redis.get(f"user_language:{user_id}")
    
    if cached_language:
        return cached_language.decode()
    
    # Get from database
    language = await get_user_language(user_id)
    
    # Cache in Redis with 24-hour expiration
    await redis.setex(f"user_language:{user_id}", 86400, language)
    
    return language


# get translated text
def t(lang: str, key: str):
    return languages.get(lang, "en").get(key, key) #en is default language