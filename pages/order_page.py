import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    name_field = OrderPageLocators.input_field_name
    surname_field = OrderPageLocators.input_field_surname
    address_field = OrderPageLocators.input_field_address
    metro_station_field = OrderPageLocators.input_field_metro_station
    metro_station_dropdown_list = OrderPageLocators.dropdown_list_station
    phone_number = OrderPageLocators.input_phone_number
    start_date= OrderPageLocators.input_start_date
    rent_period = OrderPageLocators.input_rent_period
    rent_period_dropdown_list = OrderPageLocators.dropdown_menu_rent_period
    color_checkbox = OrderPageLocators.color_checkbox

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Заполнение поля имя из файла data.py")
    def send_user_name(self, name):
        self.send_user_data(self.name_field, name)

    @allure.step("Заполнение поля фамилия из data.py")
    def send_user_surname(self, surname):
        self.send_user_data(self.surname_field, surname)

    @allure.step("Заполнение поля адрес из data.py")
    def send_user_address(self, address):
        self.send_user_data(self.address_field, address)

    @allure.step("Выбор станции метро")
    def send_user_metro_station(self):
        self.click_element(self.metro_station_field)
        self.click_element(self.metro_station_dropdown_list)

    @allure.step("Заполнение поля номер телефона из data.py")
    def send_user_phone_number(self, phone_number):
        self.send_user_data(self.phone_number, phone_number)

    @allure.step("Выбор даты аренды из data.py")
    def send_user_start_date(self, start_date):
        self.send_user_data(self.start_date, start_date)
        self.confirm_by_pressing_return(self.start_date)

    @allure.step("Заполнение поля периода аренды из data.py")
    def send_user_rent_period(self):
        self.click_element(self.rent_period)
        self.click_element(self.rent_period_dropdown_list)

    @allure.step("Выбор цвета из data.py")
    def choose_color(self):
        self.click_element(self.color_checkbox)

    @allure.step("Заполнение информации о пользователе")
    def fill_user_data_form(self, name, surname, address, phone_number):
        self.send_user_name(name)
        self.send_user_surname(surname)
        self.send_user_address(address)
        self.send_user_metro_station()
        self.send_user_phone_number(phone_number)

    @allure.step("Заполнение информации об аренде")
    def fill_rent_data_form(self, start_date):
        self.send_user_start_date(start_date)
        self.send_user_rent_period()
        self.choose_color()