# Тестирования страниц сайтов-тренажеров:
*  https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html Калькулятор
*  https://www.saucedemo.com/ Интернет-магазина
 
## Введение
Директория включает в себя набор автоматизированных тестов охватывающих пользовательский интерфейс (UI). Тесты обеспечивают проверку основных функций и навигации на сайте.

## Основные направления тестирования
Проверка работы различных разделов и кнопок сайтов-тренажеров.

## Окружение
  **Язык программирования:** Python
*   **Фреймворк для тестирования:** Selenium, Pytest, Allure-pytest
*   **Среда выполнения:** локальная установка
*   **Зависимости:** указанны в файле `requirements.txt`

## Установка и настройка
1.  Клонируйте репозиторий: `git clone <URL репозитория>`
2.  Перейдите в директорию проекта: `cd <название директории>`
3.  Установите зависимости:
    *   Для Python: `pip install -r requirements.txt`
    *   Для других языков: [Соответствующие команды]


## Запуск тестов
1.  Для запуска всех тестов (команда для запуска всех тестов): `pytest --alluredir=lesson_10/allure-results`
2.  Для просмотра отчетов Allure: `allure serve allure-results`
