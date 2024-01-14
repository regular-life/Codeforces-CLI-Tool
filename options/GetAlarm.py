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

import tzlocal
import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.join(script_dir, "..")
sys.path.append(project_dir)

from options.GetContests import *
from config.ConfigInterpreter import *

def countdown_to_contest():
    try:
        upcoming_contests = get_upcoming_contests()
        if upcoming_contests:
            contest = upcoming_contests[0]
            local_timezone = tzlocal.get_localzone()  # Get the local timezone
            start_time_utc = datetime.utcfromtimestamp(contest['startTimeSeconds'])
            start_time_local = start_time_utc.replace(tzinfo=pytz.utc).astimezone(local_timezone)  # Convert to local timezone
            start_time_str = start_time_local.strftime('%Y-%m-%d %H:%M:%S %Z')
            
            countdown = int(contest['startTimeSeconds'] - time.time())
            countdown_str = str(timedelta(seconds=countdown))
            
            # if linux, send notification using notify-send, if windows, use win10toast, if mac use mac notification
            # print date and time of contest
            if sys.platform == 'linux':
                os.system(f"notify-send --urgency=critical 'Codeforces Contest \' '{contest['name']}\nCountdown: {countdown_str}\nContest time: {start_time_str}'")
                print(f"Linux: Codeforces Contest: {contest['name']}\nCountdown: {countdown_str}")
            elif sys.platform == 'win32':
                toast = ToastNotifier()
                toast.show_toast("Codeforces Contest", f"{contest['name']}\n Countdown: {countdown_str}\nContest time: {start_time_str}", duration=10)
                print(f"Win: Codeforces Contest: {contest['name']}\n Countdown: {countdown_str}\nContest time: {start_time_str}")
            elif sys.platform == 'darwin':
                os.system(f"osascript -e 'display notification \"{contest['name']}\n Countdown: {countdown_str}\nContest time: {start_time_str}\" with title \"Codeforces Contest\"'")
                print(f"Mac: Codeforces Contest: {contest['name']} starts in {countdown_str}\n{start_time_str}")
            else:
                print("Unsupported OS")
        else:
            print("No upcoming contests")
    except Exception as e:
        print(e)
        print("Error in countdown_to_contest")
        return

if __name__ == "__main__":
    config = read_config()
    if config["alarm_for_next_contest_on_boot"]:
        countdown_to_contest()
    else:
        print("alarm_for_next_contest_on_boot is set to false in config/config.yml")
        print("If you want to enable this feature, set alarm_for_next_contest_on_boot to true in config/config.yml")