import requests
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
        print("Contest ID\tContest Name\t\t\t\t\tRank\tResulant Rating")
        for i in range(number_of_contests-1, number_of_contests-6, -1):
            contest_id = str(contests[i]["contestId"])
            contest_name = contests[i]["contestName"]
            rank = str(contests[i]["rank"])
            new_rating = str(contests[i]["newRating"])
            print(f"{contest_id}\t\t{contest_name.ljust(40)}\t{rank}\t{new_rating}")
    else:
        print("Error")

if __name__ == "__main__":
    pastContests(load_credentials()[0])
