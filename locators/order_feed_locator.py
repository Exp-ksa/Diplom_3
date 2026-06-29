from selenium.webdriver.common.by import By

class OrderFeed:
    #Cтраница "Лента заказов"
    
    # Заголовок "Лента заказов"
    HEADER_ORDER_FEED = (By.XPATH, "//div[contains(@class, 'OrderFeed')]/h1[text()='Лента заказов']")
    # Выполнено за все время
    ALL_TIME_VALUE = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class,'OrderFeed_number')]")
    # Выполнено за сегодня
    TODAY_VALUE = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class,'OrderFeed_number')]")
    # Заказ в работе
    WORKING_ORDER = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class,'text_type_digits')]")