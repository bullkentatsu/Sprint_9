import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    base_url: str = os.getenv("BASE_URL", "https://foodgram-frontend-1.prakticum-team.ru")
    implicit_wait: int = 0 
    wait_timeout: int = int(os.getenv("WAIT_TIMEOUT", "10"))

    selenoid_uri: str | None = os.getenv("SELENOID_URI")

    browser_name: str = os.getenv("BROWSER", "chrome")
    window_width: int = int(os.getenv("WINDOW_WIDTH", "1920"))
    window_height: int = int(os.getenv("WINDOW_HEIGHT", "1080"))

    headless: bool = os.getenv("HEADLESS", "false").lower() == "true"