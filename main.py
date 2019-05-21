import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]

    
    response = requests.get("https://api.github.com/users/{}/events".format(username))
    time_stamp = response.json()[0]['created_at']

    print("{}".format(time_stamp))
    


