from selenium.webdriver.common.by import By

class MainLocators: 
    #Гланое страница конструктор

    #Кнопка "Войти в аккаунт"
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Заголовок "Соберите бургер"
    HEADER_CREATE_BURGER = (By.XPATH, "//section[contains(@class, 'BurgerIngredients')]/h1[text()='Соберите бургер']")
    #Кнопка "Булки"
    BUNS_BUTTON = (By.XPATH, ".//span[text()='Булки']")
    #Наименование "Булки" в списке булок
    BUNS_TEXT = (By.XPATH, ".//h2[text()= 'Булки']")
    #Кнопка "Соусы"
    SAUCES_BUTTON = (By.XPATH, ".//span[text()='Соусы']")
    #Наименование "Соусы" в списке булок
    SAUCES_TEXT = (By.XPATH, ".//h2[text()= 'Соусы']")
    #Кнопка "Начинки"
    FILLINGS_BUTTON = (By.XPATH, ".//span[text()='Начинки']")
    #Наименование "Начинки" в списке булок
    FILLINGS_TEXT = (By.XPATH, ".//h2[text()= 'Начинки']")
    #Кнопка "Оформить заказ"
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    # Корзина
    BASKET_CONSTRUCTOR = (By.CSS_SELECTOR, "section[class*='BurgerConstructor_basket']")
    # Карточка ингредиента
    INGREDIENT = (By.CSS_SELECTOR, "a.BurgerIngredient_ingredient__1TVf6")
    # Имя карточки ингредиента
    NAME_INGREDIENT = (By.XPATH, "//a[.//p[text()='{}']]")
    # Счётчик карточки ингредиента
    COUNTER_INGREDIENT = (By.CSS_SELECTOR, ".counter_counter__num__3nue1")

class ModalLocators: 
    # Модальные окна

    MODAL_CONTAINER = (By.CSS_SELECTOR, ".Modal_modal__container__Wo2l_")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, ".Modal_modal__close__TnseK")
    MODAL_OVERLAY = (By.CSS_SELECTOR, ".Modal_modal_overlay__x2ZCr")
    
    # Модальное окна ингредиента
    INGREDIENT_MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    INGREDIENT_MODAL_NAME = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]/p[contains(@class, 'mb-8')]")
        
    # Модальное окна заказа
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class,'text_type_digits-large')]")
    ORDER_TICK_IMAGE = (By.CSS_SELECTOR, ".Modal_modal__image__2nh17")
