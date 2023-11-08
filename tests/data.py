import datetime
from datetime import date
from locators.home_page_locators import HomePageLocators
from locators.base_page_locators import BasePageLocators


class Urls:
    main_url = 'https://qa-scooter.praktikum-services.ru/'
    dzen_url = 'https://dzen.ru/?yredirect=true'


class Answers:
    test_data = [
        (HomePageLocators.question_0, HomePageLocators.answer_0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (HomePageLocators.question_1, HomePageLocators.answer_1, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        (HomePageLocators.question_2, HomePageLocators.answer_2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (HomePageLocators.question_3, HomePageLocators.answer_3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (HomePageLocators.question_4, HomePageLocators.answer_4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (HomePageLocators.question_5, HomePageLocators.answer_5, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        (HomePageLocators.question_6, HomePageLocators.answer_6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (HomePageLocators.question_7, HomePageLocators.answer_7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'),
    ]


class Data:
    name = 'Валерия'
    surname = 'Ройбуш'
    address = 'ул. Фарнаваз Мепе, д 11, кв 4'
    phone_number = '+79991112233'
    start_date = (date.today() + datetime.timedelta(days=1)).strftime("%d.%m.%Y")
    rent_period = 1
    color = 'black'
    order_buttons = [
        (BasePageLocators.order_button_header, "Заказать в шапке страницы"),
        (HomePageLocators.order_button, "Заказать внизу страницы"),
    ]


print(Answers.test_data[1])