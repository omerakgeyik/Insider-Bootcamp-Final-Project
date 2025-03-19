# Amazon Product Cart Automation

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
```bash
project/
├── tests/
├── pages/
└── utilities/
