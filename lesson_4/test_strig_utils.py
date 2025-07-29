import pytest
from string_utils import StringUtils


string_utils = StringUtils()


# Замена первой строчной буквы на заглавную(позитивные проверки)
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    # слово латиницей
    ("skypro", "Skypro"),
    # фраза из двух слов латиницей
    ("hello world", "Hello world"),
    # слово кириллицей
    ("тест", "Тест"),
    # одна латинская буква
    ("s", "S")
])
def test_capitalize_positive(input_str, expected):

    assert string_utils.capitalize(input_str) == expected


# Замена первой строчной буквы на заглавную(негативные проверки)
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    # набор цифр
    ("12345", "12345"),
    # пустой ввод
    ("", ""),
    # пробелы
    ("   ", "   "),
    # слово кириллицей, первый символ - пробел
    (" тест", " тест")
])
def test_capitalize_negative(input_str, expected):

    assert string_utils.capitalize(input_str) == expected


# Удаление пробелов в начале текста, если они есть(позитивные проверки)
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    # слово латиницей, несколько пробелов в начале
    ("   skypro", "skypro"),
    # фраза из двух слов латиницей, пробел в начале
    (" hello world", "hello world"),
    # слово кириллицей, пробел в начале
    (" Тест", "Тест"),
    # набор цифр, пробел в начале
    (" 123", "123")
])
def test_trim_positive(input_str, expected):

    assert string_utils.trim(input_str) == expected


# Удаление пробелов в начале текста, если они есть(негативные проверки)
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    # несколько пробелов без текста
    ("      ", ""),
    # слово кириллицей без пробела
    ("тест", "тест"),
    # пустой ввод
    ("", "")
    ])
def test_trim_negative(input_str, expected):

    assert string_utils.trim(input_str) == expected


# Возвращает `True`, если строка содержит искомый символ
# и `False` - если нет(позитивные проверки)
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol_str, expected", [
    # слово латиницей + первая буква слова
    ("skypro", "s", True),
    # фраза из двух слов латиницей + любая буква из фразы
    ("hello world", "d", True),
    # слово латиницей + любая заглавная буква которая отсутствует в слове
    ("python", "X", False)
])
def test_contains_positive(input_str, symbol_str, expected):

    assert string_utils.contains(input_str, symbol_str) == expected


# Возвращает `True`, если строка содержит искомый символ
# и `False` - если нет(негативные проверки)
@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol_str, expected", [
    # пустой ввод + пустое значение
    ("", "", True),
    # пробел + пробел
    (" ", " ", True),
    # набор заглавных датинских букв
    # + набор схожих по написанию букв кириллицей
    ("ABC", "АВС", False),
    # набор циф + пустое значение
    ("123", "", True),
])
def test_contains_negative(input_str, symbol_str, expected):

    assert string_utils.contains(input_str, symbol_str) == expected


# Удаление всей подстроки из переданной строки(позитивные проверки)
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol_str, expected", [
    # слово латиницей + последние три буквы из слова
    ("skypro", "pro", "sky"),
    # фраза их двух слов латиницей + второе слово из фразы
    ("hello world", "world", "hello "),
    # фраза из двух слов кириллицей + второе слово из фразы
    ("Привет мир", "Привет", " мир"),
    # набор цифр + цифры из введенного набора цифр
    ("12345", "2345", "1")
])
def test_delete_symbol(input_str, symbol_str, expected):

    assert string_utils.delete_symbol(input_str, symbol_str) == expected


# Удаление всей подстроки из переданной строки(негативные проверки)
@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol_str, expected", [
    # фраза из двух слов + пробел
    ("sky pro", " ", "skypro"),
    # пустой ввод + пустое значение
    ("", "", ""),
    # пробел + пробел
    (" ", " ", ""),
])
def test_delete_symbol_negative(input_str, symbol_str, expected):

    assert string_utils.delete_symbol(input_str, symbol_str) == expected
