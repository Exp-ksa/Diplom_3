import allure

from pages.base_page import BasePage
from locators.main_page_locator import MainLocators, ModalLocators

class MainPage(BasePage):

    @allure.step("Получить карточку ингредиента по имени {name}")
    def get_ingredient_by_name(self, name):
        locator = (MainLocators.NAME_INGREDIENT[0], MainLocators.NAME_INGREDIENT[1].format(name))
        self.scroll_to_element(locator)
        return self.wait_for_element_visible(locator)
    
    @allure.step("Кликнуть по ингредиенту {name}")
    def click_ingredient(self, name):
        locator = (MainLocators.NAME_INGREDIENT[0], MainLocators.NAME_INGREDIENT[1].format(name))
        self.scroll_to_element(locator)
        self.click_element_js(locator)

    @allure.step("Получить значение счётчика для ингредиента {name}")
    def get_counter_for(self, name):
        card = self.get_ingredient_by_name(name)
        try:
            counter = card.find_element(*MainLocators. COUNTER_INGREDIENT)
            return int(counter.text.strip())
        except:
            return 0
        
    @allure.step("Проверить, что модальное окно открыто")
    def check_open_modal_ingredient(self):
        return self.popup_displayed(ModalLocators.MODAL_CONTAINER)
    
    @allure.step("Получить заголовок модального окна")
    def get_modal_title(self):
        return self.get_text_from_element(ModalLocators.INGREDIENT_MODAL_TITLE)

    @allure.step("Получить название ингредиента в модальном окне")
    def get_ingredient_name_in_modal(self):
        return self.get_text_from_element(ModalLocators.INGREDIENT_MODAL_NAME)
    
    @allure.step("Закрыть модальное окно")
    def close_modal_window(self):
        self.wait_for_element_visible(ModalLocators.MODAL_CONTAINER)
        self.click_element_js(ModalLocators.MODAL_CLOSE_BUTTON)
        #self.wait_for_element_invisible(ModalLocators.MODAL_OVERLAY)
        

    @allure.step("Проверить, что модальное окно закрыто")
    def is_modal_closed(self, timeout=5):
        return not self.is_element_displayed(ModalLocators.MODAL_CONTAINER, timeout)

    @allure.step("Добавить ингредиент {name} в корзину")
    def add_ingedient_basket(self, name):
        source = (MainLocators.NAME_INGREDIENT[0], MainLocators.NAME_INGREDIENT[1].format(name))
        self.drag_and_drop(source, MainLocators.BASKET_CONSTRUCTOR)

    @allure.step("Оформить заказ")
    def place_order(self):
        self.click_element_js(MainLocators.ORDER_BUTTON)

    @allure.step("Ожидание полной загрузки модального окна заказа")
    def wait_for_order_modal_completely_loaded(self):
        self.wait_for_element_visible(ModalLocators.MODAL_CONTAINER)
        self.wait_for_element_visible(ModalLocators.ORDER_TICK_IMAGE)
        self.wait_for_text_change(ModalLocators.ORDER_NUMBER, "9999")
        return self.get_text_from_element(ModalLocators.ORDER_NUMBER)
    