from __future__ import annotations

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from utils.config import Config


class WebDriverFactory:
    @staticmethod
    def get_driver(cfg: Config) -> webdriver.Remote:

        options = ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"--window-size={cfg.window_width},{cfg.window_height}")

        if cfg.headless:
            options.add_argument("--headless=new")

        if cfg.selenoid_uri:
            return webdriver.Remote(
                command_executor=cfg.selenoid_uri,
                options=options,
            )

        return webdriver.Chrome(options=options)