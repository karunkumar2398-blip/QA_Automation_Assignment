# QA Automation Assignment – Invitation Nation

## 1. Project Overview

This project is a Selenium WebDriver automation framework developed for the QA Automation Internship Assignment.

The automation validates two important user flows on the Invitation Nation website:

1. Login and User Dashboard verification
2. Invitation template Live Demo and browser window handling

The framework is implemented using Python, Selenium WebDriver, and Pytest.

Test execution results are automatically recorded in a Google Sheet using a Google Apps Script Web App.

---

## 2. Website Under Test

**Website:** Invitation Nation

**URL:** https://invitationnation.in/

The automation interacts with the website through Selenium WebDriver and verifies the expected behavior using explicit waits and assertions.

---

# 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.11.9 | Programming language |
| Selenium 4.49.0 | Browser automation |
| Pytest 9.1.1 | Test execution framework |
| Google Sheets | Test result reporting |
| Google Apps Script | Receives test results |
| Requests | Sends results to Google Apps Script |
| python-dotenv | Loads environment variables |
| Google Chrome | Browser used for automation |
| Git | Version control |
| GitHub | Source code repository |

---

# 4. Project Structure

```
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
```

Folder Responsibilities
config/
Contains configuration values such as:

Website URLs
Login credentials loaded from environment variables
pages/
Contains Page Object Model classes and page-specific locators.

tests/
Contains the actual Pytest test cases.

utils/
Contains reusable utilities such as:

Chrome WebDriver creation
Google Sheets result logging
.env
Contains local credentials.
This file is intentionally excluded from GitHub.
.env.example

Provides an example of the environment variables required to run the project.

5. Framework Architecture
```
The project follows the Page Object Model (POM) approach.
                    Pytest Test Cases
                           |
                           v
                  tests/test_browser.py
                           |
          +----------------+----------------+
          |                                 |
          v                                 v
   Page Object Classes                Utility Classes
          |                                 |
          v                                 v
   Login / Dashboard                 Driver / Logger
          |                                 |
          +---------------+-----------------+
                          |
                          v
                  Selenium WebDriver
                          |
                          v
                 Invitation Nation
                          |
                          v
                  Test Result Logger
                          |
                          v
                 Google Apps Script
                          |
                          v
                    Google Sheet
```
Test Case 1 – Login and User Dashboard Verification
Objective

Verify that a user can access the Sign In / Sign Up flow, enter valid credentials, successfully log in, and reach the User Dashboard.

Open Invitation Nation
        |
        v
Click Sign In / Sign Up
        |
        v
Switch to Login Window
        |
        v
Enter Email
        |
        v
Enter Password
        |
        v
Click Login
        |
        v
Wait for Dashboard
        |
        v
Verify Dashboard
        |
        v
PASS / FAIL

Test Case 2 – Invitation Live Demo Verification
Objective

Verify the invitation navigation flow and confirm that the Live Demo opens in a new browser window.

Test Flow
Open Invitation Nation
        |
        v
Click Invitations
        |
        v
Open Commercial Category
        |
        v
Open "The Abstract Edge"
        |
        v
Find Live Demo
        |
        v
Click Live Demo
        |
        v
Verify New Window
        |
        v
Switch to New Window
        |
        v
Verify Page
        |
        v
Close New Window
        |
        v
Return to Original Window
        |
        v
PASS / FAIL

Installation
Prerequisites

Before running the project locally, install:

Python 3.11 or compatible Python version
Google Chrome
Git

The project dependencies are listed in:
requirements.txt

step 1 – Clone Repository
git clone https://github.com/karunkumar2398-blip/QA_Automation_Assignment.git

Enter the project:
cd QA_Automation_Assignment

Step 2 – Create Virtual Environment
Windows
python -m venv venv

Activate:
venv\Scripts\activate

Linux / macOS
python3 -m venv venv

Activate:
source venv/bin/activate

Step 3 – Install Dependencies
pip install -r requirements.txt
Step 4 – Configure Credentials

Create:
.env

in the project root.
Add:
INVITATION_EMAIL=your_email@example.com
INVITATION_PASSWORD=your_password

Do not commit the .env file.

Step 5 – Configure Google Sheets

Configure the Google Apps Script Web App URL in:
utils/google_sheet_logger.py

Running the Tests

Run the complete suite:
pytest -v

The suite contains two tests:
tests/test_browser.py::test_login_and_dashboard
tests/test_browser.py::test_invitation_live_demo

Running Individual Tests
Test Case 1
pytest tests/test_browser.py::test_login_and_dashboard -v
Test Case 2
pytest tests/test_browser.py::test_invitation_live_demo -v

Expected Successful Output
A successful local execution should show:

collected 2 items
tests/test_browser.py::test_login_and_dashboard PASSED
tests/test_browser.py::test_invitation_live_demo PASSED

2 passed

GitHub Codespaces Validation
The repository was also tested in GitHub Codespaces to verify the project setup and Pytest test discovery.

Pytest successfully discovered both tests:
collected 2 items
However, Selenium browser initialization failed in the Codespaces environment.

The error was:
selenium.common.exceptions.SessionNotCreatedException:
Message: session not created: Chrome instance exited

The failure occurred at:
driver = webdriver.Chrome(options=options)
before either test reached the Invitation Nation website or executed its test steps.

Codespaces Result
tests/test_browser.py::test_login_and_dashboard FAILED
tests/test_browser.py::test_invitation_live_demo FAILED

Reason

The Codespaces environment could not successfully start the Chrome browser instance required by Selenium.
Therefore, the Selenium test flows were validated using the local Windows environment where Chrome was installed and available.
This is an environment/browser-runtime limitation of the Codespaces setup rather than a failure occurring inside the individual website test flows.

Assignment Requirement Coverage
| Assignment Requirement   | Implementation |
| ------------------------ | -------------- |
| Selenium WebDriver       | Implemented    |
| Test Case 1              | Implemented    |
| Test Case 2              | Implemented    |
| Valid login flow         | Implemented    |
| Dashboard verification   | Implemented    |
| Invitation navigation    | Implemented    |
| Live Demo verification   | Implemented    |
| New window handling      | Implemented    |
| Explicit waits           | Implemented    |
| Element identification   | Implemented    |
| Assertions               | Implemented    |
| Exception handling       | Implemented    |
| Failure screenshots      | Implemented    |
| Execution time           | Implemented    |
| Google Sheets logging    | Implemented    |
| Page Object Model        | Implemented    |
| Environment variables    | Implemented    |
| Pytest                   | Implemented    |
| README documentation     | Implemented    |
| Public GitHub repository | Implemented    |

Final Validation Summary
The automation framework was successfully executed locally on Windows.

Test Case 1: PASS
Test Case 2: PASS

Overall Result: 2 PASSED

The project also includes Google Sheets reporting, Page Object Model architecture, explicit waits, exception handling, failure screenshots, execution-time tracking, and environment-based credential management
GitHub Codespaces was tested separately. Pytest successfully discovered the tests, but Chrome could not be started by Selenium in that environment. The resulting SessionNotCreatedException occurred during browser initialization before the actual test flows executed.
The repository README documents the setup process, framework architecture, test cases, reporting integration, validation results, Codespaces limitation, assumptions, and troubleshooting information.
