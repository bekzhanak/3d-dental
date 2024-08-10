import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials

SERVICE_ACCOUNT_KEY_FILE = 'd-dental-430907-5edcc53c43c7.json'

def get_credential():
    """Creates a Credential object with the correct OAuth2 authorization.

    Uses the service account key stored in SERVICE_ACCOUNT_KEY_FILE.

    Returns:
    Credentials, the user's credential.
    """
    credential = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_KEY_FILE)

    if not credential or credential.invalid:
        print('Unable to authenticate using service account key.')
        sys.exit()
    return credential


def append_data_to_sheet(data):
    client = gspread.authorize(get_credential())
    sheet = client.open(title="New one").sheet1
    sheet.append_rows(data)

