import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from data import TestData


class OrderPage(BasePage):

    @allure.step('Нажатие на кнопку Принять Куки')
    def click_cookie(self):
        self.click_on_element(OrderPageLocators.accept_cookie)


    @allure.step('Клик по предлагаемому варианту в выпадающем списке станций метро')
    def select_station(self):
        self.click_on_element(OrderPageLocators.select_item_in_dropdown_metro)

    @allure.step('Ввод даты заказа в поле "Когда привезти самокат"')
    def send_keys_date_by_keyboard_input(self, date_value):
        self.send_keys_to_field(OrderPageLocators.field_date, date_value)

    @allure.step('Клик по выбранной дате в выпадающем календаре начала аренды')
    def click_date_in_calendar(self):
        self.click_on_element(OrderPageLocators.calendar_date)

    @allure.step('Проверка отображения кнопки "Посмотреть статус" после создания заказа')
    def check_displaying_of_button_check_status_of_order(self):
        return self.check_displaying_of_element(OrderPageLocators.button_check_status_of_order)

    @allure.step('Заполнение первой части формы и нажатие кнопки "Далее"')
    def data_entry_first_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.field_name)
        self.click_on_element(OrderPageLocators.field_name)
        self.send_keys_to_field(OrderPageLocators.field_name, test_data[0])
        self.click_on_element(OrderPageLocators.field_lastname)
        self.send_keys_to_field(OrderPageLocators.field_lastname, test_data[1])
        self.click_on_element(OrderPageLocators.field_address)
        self.send_keys_to_field(OrderPageLocators.field_address, test_data[2])
        self.click_on_element(OrderPageLocators.field_metro)
        self.send_keys_to_field(OrderPageLocators.field_metro, test_data[3])
        self.click_on_element(OrderPageLocators.select_item_in_dropdown_metro)
        self.click_on_element(OrderPageLocators.field_phone)
        self.send_keys_to_field(OrderPageLocators.field_phone, test_data[4])
        self.click_cookie()
        self.click_on_element(OrderPageLocators.button_next)

    @allure.step('Заполнение второй части формы и окно подтверждения')
    def data_entry_second_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.field_date)
        self.click_on_element(OrderPageLocators.field_date)
        self.send_keys_date_by_keyboard_input(test_data[5])
        self.click_on_element(OrderPageLocators.checkbox_grey_color_scooter)
        self.click_on_element(OrderPageLocators.field_rental_period)
        self.click_on_element(OrderPageLocators.dropdown_item_rental_period)
        self.click_on_element(OrderPageLocators.field_comment)
        self.send_keys_to_field(OrderPageLocators.field_comment, test_data[6])
        self.click_on_element(OrderPageLocators.button_make_order)
        self.wait_visibility_of_element(OrderPageLocators.button_confirm_order)
        self.click_on_element(OrderPageLocators.button_confirm_order)