import allure

from selenium.webdriver import ActionChains 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

TIMEOUT = 10

class BasePage:
    
    def __init__(self, driver):
            self.driver = driver

    @allure.step("Ожидание видимости элемента")
    def wait_for_element_visible(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    @allure.step("Клик по элементу")
    def click_element(self, locator):
        element = self.wait_for_element_visible(locator)
        element.click()
    
    @allure.step("Ожидание загрузки вкладки")
    def wait_for_window_contains(self, number, timeout=TIMEOUT):
        """Ожидает, пока URL страницы не будет содержать указанный текст"""
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(number))

    @allure.step("Переключение на вкладку")
    def switch_to_window(self):
        windows_after = self.driver.window_handles    
        self.driver.switch_to.window(windows_after[-1])

    @allure.step("Проверка видимости элемента")
    def popup_displayed(self, locator):
        element = self.wait_for_element_visible(locator)
        return element.is_displayed()

    @allure.step("Возврат текущей строки")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Ввод текста в поле")
    def send_keys_to_element(self, locator, text):
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста элемента")
    def get_text_from_element(self, locator):
        element = self.wait_for_element_visible(locator)
        return element.text
    
    @allure.step("Скролл к элементу")
    def scroll_to_element(self, locator):
        element = self.wait_for_element_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Навести курсор на элемент {locator}")
    def hover_over_element(self, locator):
        element = self.wait_for_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()