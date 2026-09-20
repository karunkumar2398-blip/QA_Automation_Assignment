\# QA Automation Assignment



\## Overview



This project automates functional testing of the Invitation Nation website using Selenium WebDriver and Python.



The automation covers:



1\. User login and dashboard verification.

2\. Invitation category navigation and Live Demo verification.

3\. Automatic test-result logging to Google Sheets.



\## Technologies Used



\- Python 3.11

\- Selenium WebDriver

\- Pytest

\- Google Apps Script Web App

\- Google Sheets

\- python-dotenv

\- Requests

\- Chrome WebDriver



\## Project Structure



```text

QA\_Automation\_Assignment/

│

├── config/

│   ├── \_\_init\_\_.py

│   └── config.py

│

├── pages/

│   ├── signup\_page.py

│   ├── login\_page.py

│   └── dashboard\_page.py

│

├── tests/

│   └── test\_browser.py

│

├── utils/

│   ├── driver\_factory.py

│   └── google\_sheet\_logger.py

│

├── .env

├── .gitignore

├── requirements.txt

└── README.md

