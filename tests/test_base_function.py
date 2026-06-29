import allure
import pytest
import generate_data

from data import INGREDIENT_NAMES

from data_url import Url


@allure.story("Основная функциональность")
class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    def test_click_constructor_button_navigates_to_constructor(self, navigation_menu):
        navigation_menu.click_constructor()
        heading = navigation_menu.get_text_heading_constructor()
        
        assert "Соберите бургер" in heading
        assert navigation_menu.get_link() == Url.BASE_URL

    @allure.title("Переход по клику на «Лента заказов»")
    def test_click_order_feed_button_navigates_to_feed(self, navigation_menu):
        navigation_menu.click_order_feed()
        heading = navigation_menu.get_text_heading_order_feed()
        
        assert "Лента заказов" in heading
        assert navigation_menu.get_link() == Url.ORDER_FEED_URL

    @allure.title("Клик на ингредиент — открытие модалки с деталями")
    @pytest.mark.parametrize("name", generate_data.generate_random_burger_ingredients())
    def test_click_ingredient_opens_modal_with_details(self, main_page, name):
        main_page.click_ingredient(name)

        assert main_page.check_open_modal_ingredient(), "Модалка не открылась"
        assert main_page.get_modal_title() == "Детали ингредиента"
        assert main_page.get_ingredient_name_in_modal() == name

    @allure.title("Закрытие модалки по крестику")
    def test_modal_closes_by_clicking_close_button(self, main_page):
        main_page.click_ingredient(INGREDIENT_NAMES["buns"][0])
        
        main_page.close_modal_window()

        assert not main_page.is_modal_closed(), "Модалка не закрылась"

    @allure.title("Счетчик ингредиента изначально равен 0")
    def test_ingredient_counter_initially_zero(self, main_page):
        name = generate_data.generate_random_ingredient()
        counter_before = main_page.get_counter_for(name)
        
        assert counter_before == 0, \
            f"Начальный счётчик для '{name}': ожидалось 0, получено {counter_before}"

    @allure.title("Добавление ингредиента увеличивает счётчик (булка на 2, остальное на 1)")
    @pytest.mark.parametrize("name, increment", [
                                                (generate_data.generate_random_ingredients_other(), 1),
                                                (generate_data.generate_random_ingredients_bun(), 2)
])
    def test_adding_ingredient_increases_counter(self, main_page, name, increment):
        counter_before = main_page.get_counter_for(name)
    
        main_page.add_ingedient_basket(name)
    
        counter_after = main_page.get_counter_for(name)
        assert counter_after == counter_before + increment, \
            f"Счётчик не увеличился на {increment}: было {counter_before}, стало {counter_after}"    
        