import allure

from pages.base_page import BasePage
from locators.order_feed_locator import OrderFeed

class OrderPage(BasePage):

    @allure.step("Получить номер заказа в работе")
    def get_order_in_worked(self):
        return self.get_text_from_element(OrderFeed.WORKING_ORDER)

    @allure.step("Получить количество выполненых за все время заказов")
    def get_all_time_value(self):
        return int(self.get_text_from_element(OrderFeed.ALL_TIME_VALUE))

    @allure.step("Получить количество выполненых за сегодня заказов")
    def get_today_value(self):
        return int(self.get_text_from_element(OrderFeed.TODAY_VALUE))
