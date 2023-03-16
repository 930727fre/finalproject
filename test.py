import requests
import json
import time
import os
import google.auth
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Calculate the Unix timestamp for 10 days from now
ten_days_from_now = int(time.time()) + (10 * 24 * 60 * 60)

# Send a GET request to the Codeforces API to retrieve the list of upcoming contests
response = requests.get("https://codeforces.com/api/contest.list?gym=false")

# Convert the response from JSON to a Python dictionary
data = response.json()

# Check if the response was successful
if data["status"] == "OK":

    # Create a list to store the contest data
    contests = []

    # Loop through the list of contests and add the ones that will start within the next 10 days to the list
    for contest in data["result"]:
        start_time = contest["startTimeSeconds"]
        if start_time <= ten_days_from_now:
            contest_data = {"name": contest["name"], "start_time": start_time}
            contests.append(contest_data)

    # Write the list of contests to a JSON file
    with open("codeforce.json", "w") as outfile:
        json.dump(contests, outfile)

    # Use Google Calendar API to create events for each contest
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/calendar'])

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = google.auth.default(scopes=['https://www.googleapis.com/auth/calendar'])
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)
    calendar_id = 'primary'
    for contest in contests:
        start_time = contest["start_time"]
        event = {
            'summary': contest["name"],
            'start': {
                'dateTime': time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(start_time)),
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(start_time + 2 * 60 * 60)),
                'timeZone': 'UTC',
            },
            'reminders': {
                'useDefault': True
            },
        }
        event = service.events().insert(calendarId=calendar_id, body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))
else:
    print("Error: " + data["comment"])
