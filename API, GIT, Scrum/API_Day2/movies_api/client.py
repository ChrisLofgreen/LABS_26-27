#pip install "fastapi[standard]"
#python -m fastapi dev main.py



from api_client import get_json
import requests
import os
from dotenv import load_dotenv

load_dotenv("secrets/.env")

api_key = os.getenv("API_KEY")


BASE = "http://127.0.0.1:8000"

# all movies
#print(get_json(f"{BASE}/movies"))

# movie that does not exist
#print(get_json(f"{BASE}/movies/99"))

# add a movie
'''
movie = {
    "title": "Shutter Island",
    "director": "Martin Scorsese",
    "year": 2010
}


result = requests.post(f"{BASE}/movies", json=movie, timeout=1)
print(result.status_code)
print(result.json())


# update movie
movie = {
    "year": 1957
}

result = requests.patch(f"{BASE}/movies/1", json=movie, timeout=1)
#print(result.status_code)
'''

# Check update
#print(get_json(f"{BASE}/movies/1"))

'''
# Test the edges of update
# Empty body
movie = {}

result = requests.patch(f"{BASE}/movies/1", json=movie, timeout=1)
print(result.status_code)

movie = {
    "year": "ninetytwo"
}

result = requests.patch(f"{BASE}/movies/2", json=movie, timeout=1)
print(result.status_code)

movie = {
    "year": "1955"
}

result = requests.patch(f"{BASE}/movies/99", json=movie, timeout=1)
print(result.status_code)
'''

# Client POST

movie = {
    "title": "Shutter Island",
    "director": "Martin Scorsese",
    "year": 2010
}


result = requests.post(f"{BASE}/movies", json=movie, timeout=1, headers={"X-API-Key": api_key})
print(result.status_code)
print(result.json())