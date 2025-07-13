from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Форма "Для кого самокат"
    title_page_personal_info = (By.XPATH, "//div[text()='Для кого самокат' and contains(@class, 'Order_Header')]")
    field_name = (By.XPATH, "//input[@placeholder='* Имя']")
    field_lastname = (By.XPATH, "//input[@placeholder='* Фамилия']")
    field_address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    field_metro = (By.XPATH, "//input[@placeholder='* Станция метро']")
    select_item_in_dropdown_metro = (By.XPATH, ".//li[@class='select-search__row']")
    field_phone = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    button_next = (By.XPATH, "//button[text()='Далее']")

    # Форма "Про аренду"
    title_page_rent_info = (By.XPATH, "//div[text()='Про аренду' and contains(@class, 'Order_Header')]")
    field_date = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    calendar = (By.XPATH, "//div[@class='react-datepicker-popper']")
    calendar_date = (By.XPATH, "//div[contains(@class, 'react-datepicker') and contains(@tabindex, '0')]")
    field_rental_period = (By.XPATH, ".//div[text()='* Срок аренды']")
    dropdown_item_rental_period = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='трое суток']")
    checkbox_grey_color_scooter = (By.XPATH, "//input[@id='grey']")
    field_comment = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    button_make_order = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")

    # Подтверждение заказа (Хотите оформить заказ?)
    button_confirm_order = (By.XPATH, "//button[text()='Да']")
    button_check_status_of_order = (By.XPATH, ".//*[text()='Посмотреть статус']")

    # Принять куки
    accept_cookie = (By.ID, "rcc-confirm-button")