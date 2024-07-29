import os.path
import re
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Import unwanted_senders list from external file
from unwanted_senders import unwanted_senders

# If modifying these SCOPES, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
SCOPES = ['https://mail.google.com/']

def main():
    deleted_count = 0
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
            creds = flow.run_local_server(port=5000)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    # Initialize variables for pagination
    messages = []
    page_token = None
    fetch_count = 0
    max_results_per_request = 1000
    max_total_results = 15000

    try:
        while fetch_count < max_total_results:
            # Fetch messages with maxResults and pageToken
            results = service.users().messages().list(
                userId='me', labelIds=['INBOX'], maxResults=max_results_per_request, pageToken=page_token
            ).execute()
            
            # Extend messages list with the current batch of messages
            new_messages = results.get('messages', [])
            messages.extend(new_messages)
            
            # Update the count of fetched messages
            fetch_count += len(new_messages)
            
            # Get the nextPageToken from the current response
            page_token = results.get('nextPageToken')
            print(page_token)
            
            # Break the loop if there's no nextPageToken (no more messages to fetch)
            if not page_token:
                break

        print(f'{len(messages)} Messages found:')
        
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()

            # Extract relevant data from the message
            headers = msg.get('payload', {}).get('headers', [])
            from_header = next((header['value'] for header in headers if header['name'] == 'From'), "")

            labels = msg.get('labelIds', [])

            is_starred = 'STARRED' in labels
            is_unread = 'UNREAD' in labels
            is_replied = 'ANSWERED' in labels
            # print(from_header, any(unwanted_sender in from_header for unwanted_sender in unwanted_senders), not is_starred and is_unread and not is_replied)

            # Check if the sender is unwanted
            if any(unwanted_sender in from_header for unwanted_sender in unwanted_senders):
            # if not is_starred and is_unread and not is_replied:
                # Attempt to delete the message
                try:
                    service.users().messages().delete(userId='me', id=message['id']).execute()
                    deleted_count += 1
                    print(f"{deleted_count}) Deleted message ID: {message['id']} from {from_header}")
                except HttpError as delete_error:
                    print(f"Error deleting message ID {message['id']}: {delete_error}")
                    # Handle specific error cases or log them for further investigation
            # else:
            #     print(f"-------------- {message['id']} from {from_header}")

    except HttpError as error:
        print(f"An error occurred: {error}")
        # Handle specific error cases
        if error.resp.status == 403:
            print("The request had insufficient authentication scopes. Please re-run the script after updating scopes.")
        # Handle other errors as needed

if __name__ == '__main__':
    main()
