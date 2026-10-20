



from api_client import get_json
import requests

BASE = "http://127.0.0.1:8000"

# all movies
print(get_json(f"{BASE}/movies"))

# movie that does not exist
print(get_json(f"{BASE}/movies/99"))

# add a movie
movie = {
    "title": "Shutter Island",
    "director": "Martin Scorsese",
    "year": 2010
}
result = requests.post(f"{BASE}/movies", json=movie, timeout=1)
print(result.status_code)