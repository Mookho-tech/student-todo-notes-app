# todo_app/calendar_api.py
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

class GoogleCalendarAPI:
    def __init__(self, credentials_file):
        # Load credentials and build the service
        self.credentials = service_account.Credentials.from_service_account_file(
            credentials_file,
            scopes=['https://www.googleapis.com/auth/calendar']
        )
        self.service = build('calendar', 'v3', credentials=self.credentials)

    def create_event(self, calendar_id, event_data):
        # Insert an event into the specified calendar
        event = self.service.events().insert(calendarId=calendar_id, body=event_data).execute()
        return event

    # You can add more methods later like:
    def list_events(self, calendar_id, max_results=10):
        events = self.service.events().list(
            calendarId=calendar_id,
            maxResults=max_results,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        return events.get('items', [])
    
    def delete_event(self, calendar_id, event_id):
        self.service.events().delete(calendarId=calendar_id, eventId=event_id).execute()