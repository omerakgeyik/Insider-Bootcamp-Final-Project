# <p align="center">Amazon Product Cart Automation</p>
<div align="center">
  <img src="https://github.com/user-attachments/assets/c9a64bf3-4745-4595-875b-5ae8288ad53d" alt="Description of GIF" />
</div>

Selenium-Python test automation framework for verifying product search, cart operations, and navigation on Amazon.tr. Follows Page Object Model (POM) design pattern.

## Features
- Page Object Model implementation
- Dynamic test configuration
- Explicit waits and JavaScript interactions
- Cart operations validation
- Error handling for dynamic elements
- Cross-page navigation verification

## Prerequisites
- Python 3.7+(Used = 3.13.1)
- Chrome browser
- ChromeDriver (match your Chrome version! Used = 134.0.6998.89)
- Selenium package

## Setup
1. Clone repository
2. Install dependencies:
   ```bash
   pip install selenium
3. Download ChromeDriver and add to system(or project) PATH
4. Configure test parameters in "utilities/config.py"

## Folder Structure(POM)
```
project/
├── tests/
├── pages/
└── utilities/
```

## Running Test
Execute from project root(in terminal):
```bash
python -m unittest tests/test_amazon.py
```

## Key Components
- BaseTest: Handles browser setup/teardown
- Page Classes: Contains locators and page-specific operations
- Config: Centralized test configuration
- Waits: Explicit waits for element interactions


## Test Flow
1. Home page verification
2. Product search
3. Search results validation
4. Pagination handling
5. Product selection
6. Cart operations (add/remove)
7. Navigation verification


## Notes
- Adjust locators in page classes if Amazon UI changes
- ChromeDriver version must match local Chrome browser
- Implicit wait set to 10 seconds (configurable in BaseTest)


```
Let me know if you need any modifications or additional details! :)
```
