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
import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.join(script_dir, "..")
sys.path.append(project_dir)

from utils.credentials import *

def pastContests(username):
    url = "https://codeforces.com/api/user.rating?handle=" + username
    response = requests.get(url)
    data = response.json()
    if data["status"] == "OK":
        contests = data["result"]
        number_of_contests = len(contests)
        print(f"Total number of contests: {number_of_contests}")
        print("Most Recent Contests:")
        print("Contest ID\tContest Name\t\t\t\t\tRank\tResulant Rating\t\tDelta")
        for i in range(number_of_contests-1, number_of_contests-6, -1):
            contest_id = str(contests[i]["contestId"])
            contest_name = contests[i]["contestName"]
            rank = str(contests[i]["rank"])
            new_rating = str(contests[i]["newRating"])
            old_rating = str(contests[i]["oldRating"])
            
            # Calculate the delta (change) in rating
            delta = int(new_rating) - int(old_rating)
            if (delta > 0):
                delta = "+" + str(delta)
            elif (delta < 0):
                delta = str(delta)
            
            print(f"{contest_id}\t\t{contest_name.ljust(40)}\t{rank}\t{new_rating}\t\t\t{delta}")
    else:
        print("Error")

if __name__ == "__main__":
    pastContests(load_credentials()[0])
