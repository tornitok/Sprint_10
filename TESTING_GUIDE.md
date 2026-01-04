# Руководство по тестированию

## 1. setTimeout в консоли DevTools

### Описание
Метод `setTimeout` позволяет остановить выполнение скриптов на странице на указанный временной промежуток. Это полезно для дебага элементов, которые появляются при определенных условиях (например, при наведении мыши).

### Синтаксис
```javascript
setTimeout(function() {
    debugger;
}, 5000);
```

### Применение в тестировании
1. Откройте DevTools (F12)
2. Перейдите во вкладку Console
3. Выполните команду:
```javascript
setTimeout(function() {
    debugger;
}, 5000);
```
4. Теперь у вас есть 5 секунд, чтобы навести курсор на нужный элемент
5. После истечения времени выполнение остановится, и вы сможете изучить элемент в Elements

### Пример для поиска элементов при hover
```javascript
// Остановка на 5 секунд для наведения на элемент
setTimeout(function() {
    debugger;
}, 5000);
```

**Подробнее:** https://doka.guide/js/settimeout/

---

## 2. Метод hover в Selenium (ActionChains)

### Описание
Метод `move_to_element` позволяет выполнить наведение курсора на конкретный элемент. Применяется для эмуляции действий пользователя.

### Синтаксис
```python
from selenium.webdriver.common.action_chains import ActionChains

action = ActionChains(driver).move_to_element(element)
action.perform()
```

### Пример использования в тестах
```python
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Найти элемент
element = driver.find_element(By.ID, "menu-item")

# Навести курсор на элемент
action = ActionChains(driver)
action.move_to_element(element).perform()
```

### Расширенные возможности
```python
# Навести курсор и кликнуть
ActionChains(driver).move_to_element(element).click().perform()

# Навести курсор на первый элемент, затем на второй
menu = driver.find_element(By.ID, "menu")
submenu = driver.find_element(By.ID, "submenu")
ActionChains(driver).move_to_element(menu).move_to_element(submenu).click().perform()

# Навести курсор с паузой
ActionChains(driver).move_to_element(element).pause(1).click().perform()
```

**Подробнее:**
- https://www.selenium.dev/documentation/webdriver/actions_api/mouse/
- https://stackoverflow.com/questions/8252558/is-there-a-way-to-perform-a-mouseover-hover-over-an-element-using-selenium-and

---

## 3. Декоратор @pytest.mark.xfail

### Описание
Декоратор `@pytest.mark.xfail` устанавливается над тестовыми методами, падения которых мы ожидаем (например, известный баг).

### Синтаксис
```python
@pytest.mark.xfail(reason="Описание причины")
def test_example():
    assert False
```

### Поведение
- ✓ Если тест **падает** → в отчете будет символ `x` (expected fail) - не учитывается как провал
- ✓ Если тест **проходит** → в отчете будет символ `X` (unexpectedly passing) - учитывается как пройденный

### Примеры использования

#### Пример 1: Известный баг
```python
@pytest.mark.xfail(reason="Баг AAA-001: Кнопка не работает в Chrome")
def test_button_click():
    # Тест, который падает из-за известного бага
    button.click()
    assert result == expected
```

#### Пример 2: С условием
```python
import sys

@pytest.mark.xfail(sys.platform == "win32", reason="Не работает на Windows")
def test_windows_issue():
    assert some_function()
```

#### Пример 3: Strict режим
```python
@pytest.mark.xfail(reason="Ожидаемая ошибка", strict=True)
def test_strict_fail():
    # Если тест пройдет - будет ошибка
    assert False
```

### Параметры
- `reason` - строка с описанием, почему тест падает
- `strict` - если `True`, то неожиданный успех теста будет считаться провалом
- `raises` - ожидаемое исключение
- `run` - если `False`, тест не будет запущен

**Подробнее:** https://docs.pytest.org/en/stable/how-to/skipping.html

---

## Полезные команды

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Запуск тестов
```bash
# Все тесты
pytest

# Конкретный файл
pytest tests/test_example.py

# С отчетом Allure
pytest --alluredir=allure-results

# Просмотр отчета Allure
allure serve allure-results
```

### Проверка установки Chrome
```bash
google-chrome --version  # Linux
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version  # macOS
```

