# Automated test suite for [Yandex Scooter](https://qa-scooter.praktikum-services.ru/) service

## Стек

- Python 3.11.1  
- Pytest — фреймворк для тестирования  
- Selenium WebDriver — автоматизация браузера  
- Allure — генерация отчетов о тестах  
- Webdriver-manager — управление драйверами браузеров  


## Installation and Running Tests

```bash
pip install -r requirements.txt
pytest tests/ --alluredir=allure_results
allure serve allure_results

