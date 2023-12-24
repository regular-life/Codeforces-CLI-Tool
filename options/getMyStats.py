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
import plotly.express as px

import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.join(script_dir, "..")
sys.path.append(project_dir)

from utils.credentials import *

def getUserRating(username):
    url = "https://codeforces.com/api/user.rating?handle=" + username
    response = requests.get(url)
    data = response.json()
    if data["status"] == "OK":
        return data["result"][-1]["newRating"]
    else:
        return "Error"
    
def getProblemsSolved(username):
    url = "https://codeforces.com/api/user.status?handle=" + username
    response = requests.get(url)
    data = response.json()
    if data["status"] == "OK":
        problems = data["result"]
        unique_problems = set()
        for problem in problems:
            if problem["verdict"] == "OK":
                unique_problems.add(problem["problem"]["name"])
        return len(unique_problems)
    else:
        return "Error"
    
def getProblemsVsRatings(username):
    url = "https://codeforces.com/api/user.status?handle=" + username
    response = requests.get(url)
    data = response.json()
    
    if data["status"] == "OK":
        problems = data["result"]
        problems_vs_ratings = {}
        
        for problem in problems:
            if problem["verdict"] == "OK":
                try:
                    rating = problem["problem"]["rating"]
                    if rating not in problems_vs_ratings:
                        problems_vs_ratings[rating] = 1
                    else:
                        problems_vs_ratings[rating] += 1
                except:
                    pass

        x = list(problems_vs_ratings.keys())
        y = list(problems_vs_ratings.values())

        min_x = min(x)
        max_x = max(x)
        
        tick_vals = list(range(min_x, max_x + 1, 100))
        
        fig = px.bar(x=x, y=y, labels={'x': 'Rating', 'y': 'Number of Problems Solved'},
                     title=f'Problems vs Ratings for {username}', text=y)
        
        fig.update_layout(xaxis=dict(tickvals=tick_vals, ticktext=tick_vals))
        
        fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                          marker_line_width=1.5, opacity=0.6)

        fig.show()

        return "Success. Check the graph on your browser."
    else:
        return "Error"
    
def printStats(username):
    print("User Rating: " + str(getUserRating(username)))
    print("Problems Solved: " + str(getProblemsSolved(username)))
    print("Problems vs Ratings: " + str(getProblemsVsRatings(username)))
        
if __name__ == "__main__":
    # username = input("Enter username: ")
    printStats(load_credentials()[0])