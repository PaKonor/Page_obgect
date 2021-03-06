# def test_guest_can_go_to_login_page(fixt):
#     link = "http://selenium1py.pythonanywhere.com/"
#     fixt.get(link)
#     login_link = fixt.find_element_by_css_selector("#login_link")
#     login_link.click()

from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(fixt):

    page = MainPage(fixt, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера(fixt) и url адрес
    page.open()                      # открываем страницу(переходит по сссылке с попощью метода .get)
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(fixt, fixt.current_url) # Инициализируем LoginPage в теле теста
    login_page.should_be_login_page()
 #1ый способ   login_page = page.go_to_login_page()
 # 1ый способ   login_page.should_be_login_page()

def test_guest_should_see_login_link(fixt):

    page = MainPage(fixt, link)
    page.open()
    page.should_be_login_link()