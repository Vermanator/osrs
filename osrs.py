from __future__ import print_function
import os.path
import json
import sys
import js2py
import subprocess
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1kP6s6aQWRRGFJUHLUx7QEkzrPuunP9SM1dsmtKrj68I'
SAMPLE_RANGE_NAME = 'cbk diddldum!B3:G10'

def main():
    subprocess.call(["node","test.js"])

    names =['cbk diddldum', 'cbk kcaps','cbk zip']
    svdata = {}
    ksdata = {}
    rmdata = {}
    with open("cbk diddldum.json") as f:
        svdata = json.load(f)
    with open("cbk kcaps.json") as f:
        ksdata = json.load(f)
    with open("cbk zip.json") as f:
        rmdata = json.load(f)
    
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
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    
    for i in range(3):
        print("writing" + names[i])
        ldata = {}
        filename = names[i] + ".json"
        with open(filename) as f:
            ldata = json.load(f)
        range1 = names[i] + '!B3:C10'
        range2 = names[i] + '!D3:E10'
        range3 = names[i] + '!F3:G10'
        ranges = [range1,range2,range3]
        for r in ranges:
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range=r).execute()
            values = result.get('values', [])

            if not values:
                print('No data found.')
            else:
                svbuild = []
                values = (
                    tuple([r[0] for r in values]),tuple([ldata['skills'][r[0].lower()]['level'] for r in values])
                    )
                print(values)
                body = {
                    'majorDimension':'COLUMNS',
                    'values': values
                }
                result = service.spreadsheets().values().update(
                    spreadsheetId=SAMPLE_SPREADSHEET_ID, range=r,
                    valueInputOption='USER_ENTERED', body=body).execute()
            

if __name__ == '__main__':
    main()