# QA Automation Assignment – Invitation Nation

## Overview

This project is a Selenium-based QA automation framework developed to validate key user journeys on the **Invitation Nation** website.

The automation covers two functional test cases:

1. **Login and User Dashboard Verification**
2. **Invitation Live Demo and New Window Verification**

The framework is built using **Python, Selenium WebDriver, and Pytest** and follows the **Page Object Model (POM)** design pattern.

The framework also automatically records every test execution in a **Google Sheet**, including:

- Date and time
- Test case name
- PASS/FAIL status
- Execution time
- Failure reason

---

## 1. Website Under Test

**Invitation Nation**

https://invitationnation.in/

---

## 2. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Automation programming language |
| Selenium WebDriver | Browser automation |
| Pytest | Test execution and assertions |
| Page Object Model | Maintainable automation architecture |
| Google Apps Script | Receives test execution results |
| Google Sheets | Stores execution history |
| python-dotenv | Loads environment variables |
| Requests | Sends results to Google Apps Script |
| Google Chrome | Browser used for automation |

---

# 3. Project Structure

```text
QA_Automation_Assignment/
│
├── config/
│   ├── __init__.py
│   └── config.py
│
├── pages/
│   ├── signup_page.py
│   ├── login_page.py
│   └── dashboard_page.py
│
├── tests/
│   └── test_browser.py
│
├── utils/
│   ├── driver_factory.py
│   └── google_sheet_logger.py
│
├── .env
├── .env.example
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md