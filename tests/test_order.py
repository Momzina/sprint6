import allure
import pytest
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from tests.data import Data


class TestOrder:

    @allure.title("Тест успешного оформления заказа через кнопки Заказать в шапке сайта и на главной")
    @allure.description("Всплывающее сообщение об успешном заказе")
    @pytest.mark.parametrize("order_button_locator, button_description", Data.order_buttons)
    def test_order(self, driver, order_button_locator, button_description):
        home_page = HomePage(driver)
        home_page.click_element(BasePageLocators.cookie_button)
        home_page.click_element(order_button_locator)
        order_page = OrderPage(driver)
        order_page.fill_user_data_form(Data.name, Data.surname, Data.address, Data.phone_number)
        order_page.click_element(OrderPageLocators.next_button)
        order_page.fill_rent_data_form(Data.start_date)
        order_page.click_element(OrderPageLocators.order_button_finish)
        order_page.check_element_is_visible(OrderPageLocators.confirm_order_header)
        order_page.click_element(OrderPageLocators.confirm_order_button)
        assert order_page.check_element_is_visible(
            OrderPageLocators.confirmation_header), f"Failed to place order using {button_description}"
