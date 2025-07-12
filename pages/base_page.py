import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step('Нахождение элемента по локатору')
    def find(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.find(locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Ожидание прогрузки элемента')
    def wait_visibility_of_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        self.find(locator).click()

    @allure.step('Ввод значения в поле ввода')
    def send_keys_to_field(self, locator, keys):
        self.find(locator).send_keys(keys)

    @allure.step('Получение текста элемента')
    def get_text_on_element(self, locator):
        return self.find(locator).text

    @allure.step('Переход на другую вкладку')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Проверка отображения элемента')
    def check_displaying_of_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.is_displayed()

    @allure.step('Проверка текущего URL')
    def get_current_url(self):
        return self.driver.current_url