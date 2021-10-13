# базовая страница от которой будут унаследованы все остальные классы. В ней мы опишем вспомогательные методы для работы с драйверо
# В ней мы опишем вспомогательные методы для работы с драйверомfrom selenium.common.exceptions import
from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout) # добавили команду для неявного ожидания со значением по умолчанию в 10

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True