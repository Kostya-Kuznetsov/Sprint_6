import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Ожидание прогрузки кнопки "Заказать" в хэдере')
    def wait_visibility_of_order_button_in_header(self):
        self.wait_visibility_of_element(MainPageLocators.order_button_in_header)

    @allure.step('Клик по кнопке "Заказать" в хэдере')
    def click_on_order_button_in_header(self):
        self.click_on_element(MainPageLocators.order_button_in_header)

    @allure.step('Ожидание прогрузки лого "Самокат" в хэдере')
    def wait_visibility_of_header_logo_scooter(self):
        self.wait_visibility_of_element(MainPageLocators.header_logo_scooter)

    @allure.step('Ожидание прогрузки лого "Яндекс" в хэдере')
    def wait_visibility_of_header_logo_yandex(self):
        self.wait_visibility_of_element(MainPageLocators.header_logo_yandex)

    @allure.step('Клик по части лого с надписью "Самокат" в хэдере')
    def click_on_header_logo_scooter(self):
        self.click_on_element(MainPageLocators.header_logo_scooter)

    @allure.step('Клик по части лого с надписью "Яндекс" в хэдере')
    def click_on_header_logo_yandex(self):
        self.click_on_element(MainPageLocators.header_logo_yandex)

    @allure.step('Ожидание отображения заголовка главной страницы')
    def wait_visibility_of_main_header(self):
        self.wait_visibility_of_element(MainPageLocators.main_header)

    @allure.step('Получение текущего URL')
    def get_page_url(self):
        return self.get_current_url()

    @allure.step("Ожидание загрузки URL")
    def wait_for_url_change(self):
        self.wait.until_not(EC.url_to_be("about:blank"))

    @allure.step('Проверка отображения заголовка главной страницы')
    def check_displaying_of_main_header(self):
        return self.check_displaying_of_element(MainPageLocators.main_header)

    @allure.step('Скролл до секции "Вопросы о важном"')
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.faq_section)

    @allure.step('Ожидание прогрузки номера вопроса в "Вопросы о важнoм"')
    def wait_visibility_of_faq_questions(self, data):
        locator = MainPageLocators.faq_questions.get(data)
        if locator:
            self.wait_visibility_of_element(locator)

    @allure.step('Клик на номер вопроса в разделе "Вопросы о важнoм"')
    def click_on_faq_question(self, data):
        locator = MainPageLocators.faq_questions.get(data)
        if locator:
            self.click_on_element(locator)

    @allure.step('Ожидание прогрузки номера ответа в "Вопросы о важнoм"')
    def wait_visibility_of_faq_answer(self, data):
        locator = MainPageLocators.faq_answers.get(data)
        if locator:
            self.wait_visibility_of_element(locator)

    @allure.step('Получение текста нужного номера ответа в "Вопросы о важнoм"')
    def get_displayed_text_from_faq_answer(self, data):
        locator = MainPageLocators.faq_answers.get(data)
        if locator:
            return self.get_text_on_element(locator)