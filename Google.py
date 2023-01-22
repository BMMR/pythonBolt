from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import google.auth
from read_excel import create_file_with_incoming_information


def test_drive_connection():

    # If modifying these scopes, delete the file token.json.
    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/drive']

    # The ID and range of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1P0iPFgKK4M_kiqTUgAHTa4X9NlGWmeZf5DKDPMvweI8'
    SAMPLE_RANGE_NAME = 'orders'


    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials/client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:

        values=get_values_from_sheets(creds, SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME)

        return values

    except HttpError as err:
        print(err)

def get_values_from_sheets(creds,SAMPLE_SPREADSHEET_ID,SAMPLE_RANGE_NAME):
    service = build('sheets', 'v4', credentials=creds)
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('-->> No data found on file <<--')
        return

    return values

def update_google_file(location_file):
    # Send orders to the file
    values = test_drive_connection()
    create_file_with_incoming_information(location_file, values)
