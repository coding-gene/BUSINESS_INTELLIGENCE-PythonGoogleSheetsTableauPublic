import time
from google.oauth2 import service_account
from googleapiclient.discovery import build


class GoogleAuthentication:

    def __init__(self):
        self.scopes = ['https://www.googleapis.com/auth/spreadsheets']
        self.credentials = service_account.Credentials.from_service_account_file(
            r'gsapi/credentials.json',
            scopes=self.scopes)
        self.spreadsheet_service = build('sheets', 'v4', credentials=self.credentials)

    def send_df_to_gsheets(self, df):
        spreadsheet_id = '1wJv40IjpE-8tU_SJJ8y17wX1CL2S2yzwtoqrH0pVR7U'

        body_clear = {}
        self.spreadsheet_service.spreadsheets().values().clear(
            spreadsheetId=spreadsheet_id,
            body=body_clear,
            range='A2:Z').execute()

        time.sleep(0.5)

        body_insert = {'values': df.values.tolist()}
        self.spreadsheet_service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            body=body_insert,
            valueInputOption='USER_ENTERED',
            range='A2:C2').execute()
