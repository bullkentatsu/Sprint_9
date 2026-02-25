from pathlib import Path

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, cfg):
        self.driver = driver
        self.cfg = cfg

    def open(self, url: str) -> None:
        self.driver.get(url)

    def current_url(self) -> str:
        return self.driver.current_url

    def wait_visible(self, locator) -> WebElement:
        return WebDriverWait(self.driver, self.cfg.wait_timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_present(self, locator) -> WebElement:
        return WebDriverWait(self.driver, self.cfg.wait_timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_clickable(self, locator) -> WebElement:
        return WebDriverWait(self.driver, self.cfg.wait_timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_url_contains(self, text: str) -> None:
        WebDriverWait(self.driver, self.cfg.wait_timeout).until(lambda d: text in d.current_url)

    def wait_until_enabled(self, locator) -> WebElement:
        def _enabled(d):
            el = d.find_element(*locator)
            return el if el.is_enabled() else False

        return WebDriverWait(self.driver, self.cfg.wait_timeout).until(_enabled)

    def click(self, locator) -> None:
        self.wait_clickable(locator).click()

    def type(self, locator, text: str) -> None:
        el = self.wait_visible(locator)
        el.clear()
        el.send_keys(text)

    def text_of(self, locator) -> str:
        return self.wait_visible(locator).text

    def is_visible(self, locator) -> bool:
        try:
            self.wait_visible(locator)
            return True
        except Exception:
            return False

    def accept_alert_if_present(self) -> None:
        try:
            WebDriverWait(self.driver, 1).until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()
        except Exception:
            pass

    def scroll_into_view(self, locator) -> None:
        el = self.wait_present(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)

    def upload_file_from_assets(self, file_input_locator, filename: str) -> None:
        project_root = Path(__file__).resolve().parent.parent
        file_path = project_root / "assets" / filename

        if not file_path.exists():
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        file_input = self.wait_present(file_input_locator)
        file_input.send_keys(str(file_path))