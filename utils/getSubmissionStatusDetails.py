import requests
from datetime import datetime
import pytz
import tzlocal

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
                
                if (verdict != "TESTING"):
                    return f"{status} submitted at {submission_time_str}"

if __name__ == "__main__":
    print(getSubmissionStatusDetails("nobody_alt"))
