# Copyright 2021 Satvik Reddy

from __future__ import print_function
from os import read
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def get_messages(service, next_token=""):
    return service.users().messages().list(userId='me', q='is:unread', maxResults=100, pageToken=next_token).execute()

def mark_messages_read(service, message_objs):
    res = service.users().messages().batchModify(userId='me', body={
        'ids': list(map(lambda x: x['id'], message_objs)),
        'addLabelIds': [],
        'removeLabelIds': ['UNREAD']
    }).execute()

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
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
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    next_token = ""
    while True:
        res = get_messages(service, next_token=next_token)

        mark_messages_read(service, res['messages'])
        print("Marking messages as unread...")
        if 'nextPageToken' in res:
            next_token = res['nextPageToken']
        else:
            break


if __name__ == '__main__':
    main()