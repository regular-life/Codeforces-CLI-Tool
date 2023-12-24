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
from datetime import datetime
import pytz
import tzlocal

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.join(script_dir, "..")
sys.path.append(project_dir)

from utils.credentials import load_credentials

def get_user_title(username):
    user_info_url = f"https://codeforces.com/api/user.info?handles={username}"
    response = requests.get(user_info_url)
    
    if response.status_code == 200:
        user_info = response.json()
        if user_info['status'] == 'OK':
            return user_info['result'][0].get('rank', 'Unknown')
    
    return 'Unknown'

def get_user_color(title):
    # Map Codeforces titles to colors
    title_colors = {
        # grey
        'newbie': '\033[37m',
        # green
        'pupil': '\033[32m',
        # cyan
        'specialist': '\033[36m',
        # blue
        'expert': '\033[34m',
        # violet
        'candidate master': '\033[35m',
        # orange
        'master': '\033[33m',
        # orange
        'international master': '\033[33m',
        # red
        'grandmaster': '\033[31m',
        # red
        'international grandmaster': '\033[31m',
        # red
        'legendary grandmaster': '\033[31m'
    }
    return title_colors.get(title.lower(), '\033[0m')  # Default to reset color

def getSubmissionStatusDetails(username):
    while True:
        params = {'handle': username, 'from': 1, 'count': 1}
        response = requests.get("https://codeforces.com/api/user.status", params=params)

        if response.status_code == 200:
            submission_data = response.json()
            if submission_data['status'] == 'OK':
                result = submission_data['result'][0]
                verdict = result['verdict']
                test_set = result.get('testset', None)
                submission_time = result['creationTimeSeconds']

                if verdict == 'OK':
                    status = f"\033[92mAccepted\033[0m"  # Green color
                elif verdict == 'WRONG_ANSWER' and test_set == 'TESTS':
                    status = f"\033[91mWrong Answer on Test {result['passedTestCount'] + 1}\033[0m"  # Red color
                else:
                    status = f"\033[93m{verdict.capitalize()}\033[0m"  # Yellow color for other verdicts

                # Convert submission time to a human-readable format
                submission_time_utc = datetime.utcfromtimestamp(submission_time)
                local_timezone = tzlocal.get_localzone()  # Replace with your actual timezone
                submission_time_local = submission_time_utc.replace(tzinfo=pytz.utc).astimezone(local_timezone)
                submission_time_str = submission_time_local.strftime('%Y-%m-%d %H:%M:%S %Z')
                
                # Fetch user title and corresponding color
                user_title = get_user_title(username)
                user_color = get_user_color(user_title)
                
                # return this same sequence: # 	When 	Who 	Problem 	Lang 	Verdict 	Time 	Memory
                # under '#' we have a clickable link to submission, with overlaying text as submission id
                # under 'When' we have submission time
                # under 'Who' we have username with color based on title
                # under 'Problem' we have problem name
                # under 'Lang' we have language
                # under 'Verdict' we have verdict
                # under 'Time' we have time taken for code to run
                # under 'Memory' we have memory taken by code
                
                problem_contest_id = result['problem']['contestId']
                problem_index = result['problem']['index']
                problem_name = result['problem']['name']
                language = result['programmingLanguage']
                time_taken = result['timeConsumedMillis']
                memory_taken = result['memoryConsumedBytes']
                submission_id = result['id']
                submission_link = f'https://codeforces.com/contest/{problem_contest_id}/submission/{submission_id}'
                
                if (verdict != "TESTING"):
                    headers = "#\t\tWhen\t\t\t\tWho\t\tProblem\t\t\t\tLang\t\tVerdict\t\t\tTime\tMemory"
                    separator = "----------------------------------------------------------------------------------------------------------------------------------------------------------"
                    submission_template = "{:<10}\t{:<25}\t{:<20}\t{:<30}\t{:<10}\t{:<15}\t{:<8} {:<8}"

                    # Construct submission information
                    submission_info = submission_template.format(
                        f"{submission_id}", submission_time_str, f"{user_color}{username}\033[0m",
                        f"{problem_contest_id}-{problem_index}:{problem_name}", language, status,
                        f"{time_taken}ms", f"{memory_taken}B"
                    )

                    # Print headers, separator, and submission information
                    return(f"{headers}\n{separator}\n{submission_info}\nSubmission Link: {submission_link}")

if __name__ == "__main__":
    try:
        print(getSubmissionStatusDetails(load_credentials()[0]))
    except:
        print(f"\033[31mError\033[0m: Please enter your Codeforces username and password using \033[32mcftool --credentials\033[0m")
