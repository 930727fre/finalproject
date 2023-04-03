import requests
import json
from datetime import datetime, timedelta


def cf_ChatGPT():
    # Set the API endpoint URL
    url = 'https://codeforces.com/api/contest.list'

    # Set the current date and the date three days from now
    now = datetime.now()
    end = now + timedelta(days=30)

    # Send a GET request to the API endpoint
    response = requests.get(url)

    # Parse the response JSON data
    data = json.loads(response.content)

    # Filter the contests that start within the next three days
    contests = []
    for contest in data['result']:
        start_time = datetime.fromtimestamp(contest['startTimeSeconds'])
        if start_time >= now and start_time <= end:
            contests.append({
                'name': contest['name'],
                'start_time': start_time.strftime('%Y-%m-%d %H:%M:%S'),
                'duration': contest['durationSeconds'] // 3600
            })

    # Save the contests data in a JSON file
    with open('./jsons/GPT_codeforce.json', 'w') as f:
        json.dump(contests, f)
