# Sprint_10 - Автотесты для EZ Route

Проект автоматизированного тестирования сервиса маршрутизации [EZ Route](https://ez-route.stand.praktikum-services.ru).

## 📋 Описание проекта

Проект содержит автотесты для проверки функциональности сервиса построения маршрутов с использованием:
- **Selenium WebDriver** - для автоматизации браузера
- **Pytest** - фреймворк для тестирования
- **Allure** - для генерации красивых отчетов

## 🏗️ Структура проекта

```
Sprint_10/
├── base_object/
│   └── base_object.py          # Базовый класс Page Object с общими методами
├── locators/
│   └── main_page_locators.py   # Локаторы элементов главной страницы
├── pages/
│   └── main_page.py            # Page Object главной страницы
├── tests/
│   └── test_route_drawing.py   # Тесты отрисовки маршрутов
├── config.py                    # Конфигурация проекта (URL, секреты)
├── conftest.py                  # Pytest фикстуры
├── requirements.txt             # Зависимости проекта
├── TESTING_GUIDE.md            # Руководство по методам тестирования
└── README.md                    # Этот файл
```

## 🚀 Установка и настройка

### 1. Установка Chrome

Убедитесь, что у вас установлен браузер Google Chrome:

**macOS:**
```bash
# Проверка установки
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version
```

**Linux:**
```bash
google-chrome --version
```

Если Chrome не установлен, скачайте его с [официального сайта](https://www.google.com/chrome/).

### 2. Установка зависимостей

```bash
# Создание виртуального окружения (опционально)
python -m venv venv
source venv/bin/activate  # macOS/Linux
# или
venv\Scripts\activate  # Windows

# Установка зависимостей
pip install -r requirements.txt
```

### 3. Проверка установки

```bash
# Проверка установленных пакетов
pip list | grep -E "selenium|pytest|allure"
```

Должны быть установлены:
- selenium==4.16.0
- pytest==7.4.3
- allure-pytest==2.13.2
- webdriver-manager==4.0.1

## 📝 Тестовые сценарии

### Отрисовка маршрута

**Предустановленные адреса:**
- Хамовнический вал, 34
- Зубовский бульвар, 37

**Что тестируется:**
При вводе двух разных предустановленных адресов в поля "Откуда" и "Куда" на карте отображаются две точки начала и конца маршрута.

## 🧪 Запуск тестов

### Базовый запуск

```bash
# Запуск всех тестов
pytest

# Запуск конкретного файла
pytest tests/test_route_drawing.py

# Запуск с подробным выводом
pytest -v

# Запуск с отображением print statements
pytest -s
```

### Запуск с Allure отчетами

```bash
# Запуск тестов с генерацией Allure данных
pytest --alluredir=allure-results

# Просмотр отчета
allure serve allure-results
```

### Дополнительные опции

```bash
# Запуск конкретного теста по имени
pytest -k "test_route_points_hamovnichesky"

# Запуск с маркерами
pytest -m "smoke"

# Параллельный запуск (требует pytest-xdist)
pytest -n auto
```

## 🔍 Использование изученных методов

### 1. setTimeout в DevTools (для дебага)

Для изучения элементов, которые появляются при hover:

1. Откройте DevTools: `F12` или `Cmd+Option+I` (macOS)
2. Перейдите во вкладку **Console**
3. Выполните команду:
```javascript
setTimeout(function() { debugger; }, 5000);
```
4. Теперь у вас есть 5 секунд, чтобы навести курсор на нужный элемент
5. После остановки можно изучить DOM в Elements

### 2. Метод hover (ActionChains)

Пример использования в тестах:

```python
from selenium.webdriver.common.action_chains import ActionChains

# Через base_object
main_page.hover(locator)

# Напрямую
element = driver.find_element(By.ID, "menu")
ActionChains(driver).move_to_element(element).perform()
```

### 3. Декоратор @pytest.mark.xfail

Для тестов с известными багами:

```python
@pytest.mark.xfail(reason="Баг AAA-001: Кнопка не работает")
def test_known_bug(driver):
    # Тест, который ожидаемо падает
    assert False
```

Подробнее см. [TESTING_GUIDE.md](TESTING_GUIDE.md)

## 📊 Примеры использования

### Базовый тест

```python
def test_route_drawing(driver):
    main_page = MainPage(driver)
    
    # Установка маршрута
    main_page.enter_from_address("Хамовнический вал, 34")
    main_page.enter_to_address("Зубовский бульвар, 37")
    
    # Ожидание отрисовки
    main_page.wait_for_route_to_display()
    
    # Проверка
    markers = main_page.get_map_markers_count()
    assert markers >= 2
```

### С Allure шагами

```python
import allure

@allure.feature('Построение маршрута')
@allure.story('Отрисовка маршрута')
def test_route_with_allure(driver):
    with allure.step('Открыть главную страницу'):
        main_page = MainPage(driver)
    
    with allure.step('Ввести адрес начала'):
        main_page.enter_from_address("Хамовнический вал, 34")
    
    # ... остальные шаги
```

## 🛠️ Полезные команды

```bash
# Очистка кэша pytest
pytest --cache-clear

# Показать доступные фикстуры
pytest --fixtures

# Показать доступные маркеры
pytest --markers

# Сохранение последнего упавшего теста для повторного запуска
pytest --lf

# Остановка на первом упавшем тесте
pytest -x
```

## 📚 Дополнительные ресурсы

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Allure Documentation](https://docs.qameta.io/allure/)
- [Testing Guide](TESTING_GUIDE.md) - подробное руководство по методам

## 🐛 Отладка

### Если тесты не запускаются:

1. Проверьте установку Chrome: `google-chrome --version`
2. Проверьте установку зависимостей: `pip list`
3. Убедитесь, что сайт доступен: https://ez-route.stand.praktikum-services.ru
4. Проверьте логи pytest с флагом `-v`

### Если элементы не находятся:

1. Используйте `setTimeout` в DevTools для изучения DOM
2. Проверьте локаторы в `locators/main_page_locators.py`
3. Добавьте явные ожидания в Page Object
4. Используйте скриншоты: `driver.save_screenshot("debug.png")`

## 📄 Лицензия

Проект создан в учебных целях для Яндекс.Практикум.

