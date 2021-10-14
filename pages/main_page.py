from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
     def go_to_login_page(self):
         login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK) #Один агрумент - пара, которую мы распакуем с помощью звездочки и превратим в два объекта
         login_link.click()                                                   #когда передаем пару со звездочкой, она превращается в эти самые 2 аргумента
   #1ый способ      #return LoginPage(browser=self.browser, url=self.browser.current_url) #в методе, который осуществляет переход к странице логина, проинициализировать новый объект Page и вернуть его


     def should_be_login_link(self):
         assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

         #is_element_present inherit from BasePgae
         #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") - кортеж, содержащий два значения
         #мы его передаем в is_element_present(), который содержит find_element().
         #метод find_element() принимает два значения: как искать? (By.CSS_SELECTOR) и что искать? ("#login_link")