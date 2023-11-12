from selenium.webdriver.common.by import By


class BasePageLocators:
    yandex_logo_header = [By.XPATH, ".//img[@alt = 'Yandex']"]   # логотип "Яндекс"
    samokat_logo_header = [By.XPATH, ".//img[@alt = 'Scooter']"]  # логотип "Самокат"
    order_button_header = [By.XPATH, ".//div[@class = 'Header_Nav__AGCXC']/button[text() = 'Заказать']"]  # кнопка "Заказать"
    cookie_button = [By.XPATH, ".//button[@id='rcc-confirm-button']"]   # кнопка "да все привыкли"