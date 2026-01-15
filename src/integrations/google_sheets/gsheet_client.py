import gspread
from google.oauth2.service_account import Credentials
import os

# Get current file location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Correct path to credentials folder
SERVICE_ACCOUNT_FILE = os.path.join(
    BASE_DIR,
    "../../../credentials/service_account.json"
)

# Google Sheet ID
SPREADSHEET_ID = "16fcG4HvtXo4q8PudxdMy3qzRN6W5F0LcUbQbDEsFsMw"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def get_spreadsheet():
    try:
        # Load credentials
        creds = Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE,
            scopes=SCOPES
        )

        # Authorize client
        client = gspread.authorize(creds)

        # Open spreadsheet using ID
        return client.open_by_key(SPREADSHEET_ID)

    except FileNotFoundError:
        raise Exception(
            f"❌ service_account.json not found at:\n{SERVICE_ACCOUNT_FILE}"
        )

    except gspread.exceptions.SpreadsheetNotFound:
        raise Exception(
            "❌ Spreadsheet not found. "
            "Check Sheet ID or sharing permissions."
        )

    except Exception as e:
        raise Exception(f"❌ Google Sheets connection failed: {e}")


