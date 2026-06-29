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
    
    @allure.step("Ожидание невидимости элемента")
    def wait_for_element_invisible(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
    
    @allure.step("Поиск элемента")
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    @allure.step("Клик по элементу")
    def click_element(self, locator):
        element = self.wait_for_element_visible(locator)
        element.click()

    @allure.step("Клик по элементу через JavaScript")
    def click_element_js(self, locator):
        element = self.wait_for_element_visible(locator)
        self.driver.execute_script("arguments[0].click();", element)
    
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
        element = self.wait_for_element_visible(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    @allure.step("Ожидание изменения текста элемента {locator}")
    def wait_for_text_change(self, locator, old_text, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_element(*locator).text != old_text
            )

    @allure.step("Взять элемент {source_locator} и переместить в {target_locator}")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)

        self.driver.execute_script("""
            function simulateDragAndDrop(source, target) {
                const dataTransfer = new DataTransfer();
                source.dispatchEvent(new DragEvent('dragstart', {
                    bubbles: true, cancelable: true, dataTransfer: dataTransfer
                }));
                target.dispatchEvent(new DragEvent('dragenter', {
                    bubbles: true, cancelable: true, dataTransfer: dataTransfer
                }));
                target.dispatchEvent(new DragEvent('dragover', {
                    bubbles: true, cancelable: true, dataTransfer: dataTransfer
                }));
                target.dispatchEvent(new DragEvent('drop', {
                    bubbles: true, cancelable: true, dataTransfer: dataTransfer
                }));
                source.dispatchEvent(new DragEvent('dragend', {
                    bubbles: true, cancelable: true, dataTransfer: dataTransfer
                }));
            }
            simulateDragAndDrop(arguments[0], arguments[1]);
        """, source, target)

    @allure.step("Проверка отображения элемента")
    def is_element_displayed(self, locator, timeout=TIMEOUT):
        try:
            self.wait_for_element_visible(locator, timeout)
            return True
        except:
            return False
    