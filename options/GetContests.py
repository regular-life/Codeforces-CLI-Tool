"""
Copyright (C) 2023 yash

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import requests
from datetime import datetime, timedelta
import time
import pytz
import tzlocal

def get_upcoming_contests():
    url = "https://codeforces.com/api/contest.list"
    response = requests.get(url)
    
    if response.status_code == 200:
        contests = response.json()['result']
        now = time.time()
        
        upcoming_contests = [contest for contest in contests if contest['phase'] == 'BEFORE' and contest['startTimeSeconds'] > now]
        upcoming_contests.sort(key=lambda x: x['startTimeSeconds'])
        
        return upcoming_contests
    else:
        return None

def display_contest_countdown():
    upcoming_contests = get_upcoming_contests()
    
    if upcoming_contests:
        print("Upcoming Contests:")
        local_timezone = tzlocal.get_localzone()  # Get the local timezone
        print("{:<5} {:<50} {:<25} {:<15}".format("Index", "Contest Name", "Start Time", "Countdown"))
        for i, contest in enumerate(upcoming_contests, start=1):
            start_time_utc = datetime.utcfromtimestamp(contest['startTimeSeconds'])
            start_time_local = start_time_utc.replace(tzinfo=pytz.utc).astimezone(local_timezone)  # Convert to local timezone
            start_time_str = start_time_local.strftime('%Y-%m-%d %H:%M:%S %Z')
            
            countdown = int(contest['startTimeSeconds'] - time.time())
            countdown_str = str(timedelta(seconds=countdown))
            
            print("{:<5} {:<50} {:<25} {:<15}".format(i, contest['name'], start_time_str, countdown_str))
    else:
        print("Error fetching contest data.")

if __name__ == "__main__":
    display_contest_countdown()
