import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage

base_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

x_fail = 7
links = [base_link+str(i) for i in range(10) if i != x_fail]
xlink = pytest.param(base_link+str(x_fail), marks=pytest.mark.xfail(reason="mistake on page"))
links.insert(x_fail, xlink)

@pytest.mark.parametrize('link', links)
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, link):
    browser.delete_all_cookies()
    page = ProductPage(browser, link)       # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                             # Открываем страницу товара
    page.add_to_cart()                      # Нажимаем на кнопку "Добавить в корзину"
    page.solve_quiz_and_get_code()          # Посчитать результат математического выражения и ввести ответ
    page.should_be_the_product_in_cart()    # Название товара в сообщении совпадает с тем товаром, который добавили?
    page.should_be_correct_cost_in_cart()   # Стоимость корзины совпадает с ценой товара?

# 4.3 step 6
@pytest.mark.xfail(reason="mistake on page")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    browser.delete_all_cookies()
    page = ProductPage(browser, link)     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                             # Открываем страницу товара
    page.add_to_cart()                      # Добавляем товар в корзину
    page.should_not_be_success_message()    # Проверяем, что НЕТ сообщения об успехе с помощью is_not_element_present

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    browser.delete_all_cookies()
    page = ProductPage(browser, link)     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                             # Открываем страницу товара
    page.should_not_be_success_message()    # Проверяем, что НЕТ сообщения об успехе с помощью is_not_element_present

@pytest.mark.xfail(reason="mistake on page")
def test_message_disappeared_after_adding_product_to_basket(browser):
    browser.delete_all_cookies()
    page = ProductPage(browser, link)     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                             # Открываем страницу товара
    page.add_to_cart()                      # Добавляем товар в корзину
    page.should_disappear_success_message()    # Проверяем, что НЕТ сообщения об успехе с помощью is_disappeared

# 4.3 step 8
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

