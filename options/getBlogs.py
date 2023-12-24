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

def getBlogs(number_of_actions):
    url = "https://codeforces.com/api/recentActions?maxCount=" + str(number_of_actions)
    response = requests.get(url)
    data = response.json()
    if data["status"] == "OK" :
        actions = data["result"]
        number_of_actions = len(actions)
        print("Most Recent Actions:")
        print(f"{'Index':<5}{'Title':<50}{'Author':<20}{'Link'}")
        for i in range(number_of_actions):
            blog_id = actions[i]['blogEntry']['id']
            blog_link = f"https://codeforces.com/blog/entry/{blog_id}"
            blog_text = actions[i]['blogEntry']['title'][3:len(actions[i]['blogEntry']['title'])-4]
            
            print(f"{i+1:<5}{blog_text[:50]:<50}{actions[i]['blogEntry']['authorHandle']:<20}{blog_link}")
    else:
        print("Error")

if __name__ == '__main__':
    number_of_actions = int(input("Enter the number of actions you want to see: "))
    getBlogs(number_of_actions)
    