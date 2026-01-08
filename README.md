# UI Test Automation Project

Automated UI tests for the Educational Route & Taxi Ordering Service.

## Technology Stack

- Python 3.10+
- pytest
- Selenium WebDriver (Chrome)
- Allure Reporting

## Installation

```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests:
```bash
pytest
```

Run with verbose output:
```bash
pytest -v
```

Run specific test module:
```bash
pytest tests/test_route_drawing.py
```

## Allure Report

Generate and view Allure report:
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Project Structure

```
project/
├── pages/                  # Page Object package
│   ├── __init__.py
│   ├── base_object.py      # Base Page Object
│   ├── main_page.py
│   ├── route_page.py
│   └── order_page.py
│
├── tests/                  # Test modules
│   ├── __init__.py
│   ├── test_route_drawing.py
│   ├── test_route_options_block.py
│   ├── test_prepare_taxi_order.py
│   └── test_taxi_order_flow.py
│
├── test_data/              # Test data
│   ├── __init__.py
│   └── addresses.py
│
├── conftest.py             # Fixtures
├── requirements.txt
└── README.md
```

## Preset Addresses

The application provides two preset addresses:
- Hamovnicheskij Val, 34
- Zubovskij Boulevard, 37
