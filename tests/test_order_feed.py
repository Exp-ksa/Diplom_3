import allure
import pytest

from data import INGREDIENT_NAMES
from data_url import Url


@allure.story("Лента заказов")
class TestOrderFeed:

    @allure.title("Создание заказа увеличивает счётчик «Выполнено за всё время»")
    def test_create_order_increases_all_time_counter(self, authorization_main_page, order_feed_page):
        all_time_before = order_feed_page.get_all_time_value()

        main_page = authorization_main_page
        main_page.driver.get(Url.BASE_URL)

        main_page.add_ingedient_basket(INGREDIENT_NAMES["buns"][0])
        main_page.add_ingedient_basket(INGREDIENT_NAMES["sauces"][0])
        main_page.add_ingedient_basket(INGREDIENT_NAMES["fillings"][0])
        main_page.place_order()
        main_page.wait_for_order_modal_completely_loaded()
        
        order_feed_page.driver.get(Url.ORDER_FEED_URL)
        all_time_after = order_feed_page.get_all_time_value()
        
        assert all_time_after > all_time_before, \
            f"Счётчик за всё время не увеличился: было {all_time_before}, стало {all_time_after}"

    @allure.title("Создание заказа увеличивает счётчик «Выполнено за сегодня»")
    def test_create_order_increases_today_counter(self, authorization_main_page, order_feed_page):
        today_before = order_feed_page.get_today_value()

        main_page = authorization_main_page
        main_page.driver.get(Url.BASE_URL)

        main_page.add_ingedient_basket(INGREDIENT_NAMES["buns"][0])
        main_page.add_ingedient_basket(INGREDIENT_NAMES["sauces"][1])
        main_page.add_ingedient_basket(INGREDIENT_NAMES["fillings"][8])
        main_page.add_ingedient_basket(INGREDIENT_NAMES["fillings"][2])
        main_page.place_order()
        main_page.wait_for_order_modal_completely_loaded()
        
        order_feed_page.driver.get(Url.ORDER_FEED_URL)
        today_after = order_feed_page.get_today_value()
        
        assert today_after > today_before, \
            f"Счётчик за сегодня не увеличился: было {today_before}, стало {today_after}"

    @allure.title("Номер заказа появляется в разделе «В работе»")
    def test_order_number_appears_in_work_section(self, authorization_main_page, order_feed_page):
        main_page = authorization_main_page
        main_page.driver.get(Url.BASE_URL)

        main_page.add_ingedient_basket(INGREDIENT_NAMES["buns"][1])
        main_page.add_ingedient_basket(INGREDIENT_NAMES["sauces"][3])
        main_page.add_ingedient_basket(INGREDIENT_NAMES["fillings"][4])
        main_page.place_order()
        order_number = main_page.wait_for_order_modal_completely_loaded()
                
        order_feed_page.driver.get(Url.ORDER_FEED_URL)
        
        working_order = order_feed_page.get_order_in_worked()
        
        assert order_number in working_order, \
            f"Номер заказа {order_number} не найден в разделе «В работе»: {working_order}"