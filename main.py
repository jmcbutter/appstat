#!/usr/bin/env python3
import argparse
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/docs", "https://www.googleapis.com/auth/documents", "https://www.googleapis.com/auth/spreadsheets"]


def create_google_api_service():
    """
    Handles the google drive API calls
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("drive", "v3", credentials=creds)
        return service
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f"An error occurred: {error}")


def create_new_application(args):
    service = create_google_api_service()
    # TODO: Update so that the folder can be selected or can be placed in a config file
    folder_id = '1uQLtAnUWl__FTCJ0qJcRghmSc-NGLAXr'

    file_metadata = {"name": args.company + ' ' + args.position, "parents": [folder_id]}
    # Call the Drive v3 API
    file = (
        service.files()
        .create(body=file_metadata, fields="id, name")
        .execute()
    )
    print(file.get("name"))


def main():
    parser = argparse.ArgumentParser(prog='PROG')

    command_parsers = parser.add_subparsers()

    # New Application
    new_parser = command_parsers.add_parser('new')
    new_parser.add_argument('-c', '--company', required=True)
    new_parser.add_argument('-p', '--position', required=True)
    new_parser.set_defaults(func=create_new_application)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
