from functools import lru_cache
import os

from dotenv import load_dotenv

load_dotenv()


@lru_cache
def get_settings():
    return {
        "gemini_api_key": os.getenv("GEMINI_API_KEY", "").strip(),
        "gemini_model": os.getenv(
            "GEMINI_MODEL",
            "gemini-2.5-flash"
        ).strip(),
        "database_url": os.getenv(
            "DATABASE_URL",
            "sqlite:///./fitbuddy.db"
        ).strip(),
        "demo_mode": os.getenv(
            "DEMO_MODE",
            "true"
        ).lower() in {"1", "true", "yes", "on"},
    }