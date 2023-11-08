import allure
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Виден указанный элемент")
    def check_element_is_visible(self, locator):
        return WebDriverWait(self.driver, timeout=15).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Клик по элементу")
    def click_element(self, locator):
        WebDriverWait(self.driver, timeout=15).until(expected_conditions.visibility_of_element_located(locator)).click()

    @allure.step("Заполнение поля данными")
    def send_user_data(self, locator, data):
        WebDriverWait(self.driver, timeout=15).until(expected_conditions.visibility_of_element_located(locator)).send_keys(data)

    @allure.step("Отправить при помощи RETURN")
    def confirm_by_pressing_return(self, locator):
        WebDriverWait(self.driver, timeout=15).until(expected_conditions.visibility_of_element_located(locator)).send_keys(Keys.RETURN)

    @allure.step("Возвращается текст")
    def get_text_element(self, locator):
        return WebDriverWait(self.driver, timeout=15).until(expected_conditions.visibility_of_element_located(locator)).text

    @allure.step("Скролл до конкретного элемента")
    def go_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Переход на другую вкладку")
    def switch_to_tab(self):
        handles = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        next_handle = handles[(handles.index(current_handle) + 1) % len(handles)]
        self.driver.switch_to.window(next_handle)
        time.sleep(10)

    @allure.step("Возврат на текущую страницу")
    def get_current_page_url(self):
        return self.driver.current_url