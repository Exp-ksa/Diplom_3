from selenium.webdriver.common.by import By

class HeaderLocators: #Гланое страница конструктор
    #Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//a[@href='/account']/p[contains(text(), 'Кабинет')]")
    #Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//a[@href='/']/p[contains(text(), 'Конструктор')]")
    #Кнопка "Лента заказов"
    ORDER_FEED_BUTTON = (By.XPATH, ".//a[@href='/feed']/p[contains(text(), 'Лента')]")
    #Лого "Stellar Burger"
    LOGO_STELLAR_BURGER = (By.CSS_SELECTOR, 'div.AppHeader_header__logo__2D0X2') 
