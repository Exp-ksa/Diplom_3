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
        assert main_page.check_open_modal_ingredient()
        main_page.close_modal_window()

        assert not main_page.is_modal_closed(), "Модалка не закрылась"

    @allure.title("Добавление ингредиента увеличивает счётчик")
    @pytest.mark.parametrize("name", generate_data.generate_random_burger_ingredients())
    def test_adding_ingredient_increases_counter(self, main_page, name):
        counter_before = main_page.get_counter_for(name)
        assert counter_before == 0, \
            f"Начальный счётчик для '{name}': ожидалось 0, получено {counter_before}"

        main_page.add_ingedient_basket(name)
        
        counter_after = main_page.get_counter_for(name)
        if name in INGREDIENT_NAMES["buns"]:
            assert counter_after == counter_before + 2, f"Счётчик не увеличился: было {counter_before}, стало {counter_after}"
        else:
            assert counter_after == counter_before + 1, f"Счётчик не увеличился: было {counter_before}, стало {counter_after}"