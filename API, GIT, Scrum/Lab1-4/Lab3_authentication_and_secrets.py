



# Lab 3: Authentication and secrets


# 1. 

# Check


# 2.

# Check


# 3.

'''
import os
from dotenv import load_dotenv
from api_client import get_json

load_dotenv("API, GIT, Scrum/Lab1-4/other/.env")

username = str(input("Type usename:")).strip()

token = os.getenv("GITHUB_TOKEN")
params = {"sort": "pushed", "per_page": 5}
headers = {"Authorization": f"Bearer {token}"}
repos = get_json(f"https://api.github.com/users/{username}/repos", params=params, headers=headers)

for repo in repos:
    print(repo["name"])

'''

# 4.
'''
import requests
import os
from dotenv import load_dotenv
from api_client import get_json

load_dotenv("API, GIT, Scrum/Lab1-4/other/.env")

username = str(input("Type usename:")).strip()

token = os.getenv("GITHUB_TOKEN")
params = {"sort": "pushed", "per_page": 5}
headers = {"Authorization": f"Bearer {token}"}
repos = requests.get(f"https://api.github.com/users/{username}/repos", params=params, headers=headers)

print(repos.headers["X-RateLimit-Limit"])
'''
#Returns 5000

#----------------------------------------------
'''
username = str(input("Type usename:")).strip()

params = {"sort": "pushed", "per_page": 5}
repos = requests.get(f"https://api.github.com/users/{username}/repos", params=params)

print(repos.headers["X-RateLimit-Limit"])
'''
#Returns 60


# 5.
'''
import requests
import os
from dotenv import load_dotenv
from api_client import get_json

load_dotenv("API, GIT, Scrum/Lab1-4/other/.env")

username = str(input("Type usename:")).strip()

token = os.getenv("GITHUB_TOKEN")
params = {"sort": "pushed", "per_page": 5}
headers = {"Authorization": f"Bearer {token}"}
repos = requests.get(f"https://api.github.com/users/{username}/repos", params=params, headers=headers)

print(repos.json())
print(repos.status_code)
'''
# Returns {'message': 'Bad credentials', 'documentation_url': 'https://docs.github.com/rest', 'status': '401'} when run with a broken token.
# This means like it says, that there is something wrong with the credentials, whereas 403 would mean that the credentials are recognized.
# But with those credentials, you are not allowed to do the thing that you are trying to do.

# 6.

# Check


# 7.

# Check