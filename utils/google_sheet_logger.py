import requests
from datetime import datetime


GOOGLE_SHEET_WEBHOOK = "https://script.google.com/macros/s/AKfycbyEv3vWQO1tT14tYxlX7JcgEoLQ1CS97CeJhVGDiRNnRhSCKWBAn4UIQqQJKv6ypAgF/exec"


def log_result(test_case, status, execution_time, failure_reason=""):
    data = {
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "test_case": test_case,
        "status": status,
        "execution_time": f"{execution_time:.2f} seconds",
        "failure_reason": failure_reason
    }

    try:
        response = requests.post(
            GOOGLE_SHEET_WEBHOOK,
            json=data,
            timeout=10
        )

        response.raise_for_status()
        print("Google Sheet: result logged successfully")

    except Exception as e:
        print(f"Google Sheet logging failed: {e}")