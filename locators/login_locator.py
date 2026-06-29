from selenium.webdriver.common.by import By

class LoginLocators: 
    #Страница "Личный кабинет" авторизация

    #Поле Email
    EMAIL_FIELD = (By.XPATH, ".//div[contains(@class,'input_type_text') and .//label[text()='Email']]//input")
    #Поле пароль
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password']")
    #Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, ".//button[text() ='Войти']")
    #Ссылка на страницу "Регистрации" 
    LINK_REGISTRATION = (By.XPATH, ".//a[@href='/register']")
    #Ссылка на страницу "Восстановления пароля"
    LINK_FOGOT_PASSWORD = (By.XPATH, ".//a[@href='/forgot-password']")