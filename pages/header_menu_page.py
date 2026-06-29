import allure

from locators.header_menu_locator import HeaderLocators
from locators.main_page_locator import MainLocators
from locators.order_feed_locator import OrderFeed
from pages.base_page import BasePage

class NavigationMenu(BasePage):

    @allure.step("Нажать на лого Конструктор")
    def click_constructor(self):
        self.click_element_js(HeaderLocators.CONSTRUCTOR_BUTTON)
    
    @allure.step("Нажать на лого Лента заказов")
    def click_order_feed(self):
        self.click_element_js(HeaderLocators.ORDER_FEED_BUTTON)

    @allure.step("Нажать на лого Stellar Burger")
    def click_logo_stellar_burger(self):
        self.click_element_js(HeaderLocators.LOGO_STELLAR_BURGER)

    @allure.step("Нажать на кнопку Личный кабинет")
    def click_personal_account(self):
        self.click_element_js(HeaderLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Получить заголовок страницы Конструктор")
    def get_text_heading_constructor(self):
        return self.get_text_from_element(MainLocators.HEADER_CREATE_BURGER)
    
    @allure.step("Получить заголовок страницы Лента заказов")
    def get_text_heading_order_feed(self):
        return self.get_text_from_element(OrderFeed.HEADER_ORDER_FEED)
    
    def get_link(self):
        return self.get_current_url()
