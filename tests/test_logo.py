import allure
from tests.data import Urls
from pages.home_page import HomePage
from locators.base_page_locators import BasePageLocators
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators


class TestsLogo:

    @allure.title("Яндекс logo")
    @allure.description("При клике на Яндекс происходит переход на Дзен")
    def test_yandex(self, driver):
        home_page = HomePage(driver)
        home_page.click_element(BasePageLocators.yandex_logo_header)
        home_page.switch_to_tab()
        current_url = home_page.get_current_page_url()
        assert current_url == Urls.dzen_url, f"Failed to redirect to {Urls.dzen_url}"

    @allure.title("Самокат logo")
    @allure.description("При клики на лого Самоката происходит переход на главную страницу Самоката")
    def test_samokat(self, driver):
        home_page = HomePage(driver)
        home_page.click_element(BasePageLocators.order_button_header)
        order_page = OrderPage(driver)
        order_page.check_element_is_visible(OrderPageLocators.user_form_header)
        order_page.click_element(BasePageLocators.samokat_logo_header)
        home_page_url = home_page.get_current_page_url()
        assert home_page_url == Urls.main_url, f"Failed to return"
