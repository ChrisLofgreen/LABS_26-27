#pip install "fastapi[standard]"
#python -m fastapi dev main.py


# Part 1: Your own API

# 1.

from fastapi import FastAPI, HTTPException


app = FastAPI()



movies = [
    {"id": 1, "title": "Terminator 2", "director": "James Cameron", "year": 1991},
    {"id": 2, "title": "Fire Walk with Me", "director": "David Lynch", "year": 1992},
    {"id": 3, "title": "Life of Brian", "director": "Terry Jones", "year": 1979},
    {"id": 4, "title": "Modern Times", "director": "Charlie Chaplin", "year": 1936}
]

@app.get("/movies")
def get_movies():
    return movies

#print(get_movies())

# 2. 

@app.get("movies/{movie_id}")
def get_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=404)

#print(get_movie(1))     # Returns the movie
#print(get_movie(99))    # Returns fastapi.exceptions.HTTPException: 404: Not Found
#print(get_movie("abc"))  # Also returns fastapi.exceptions.HTTPException: 404: Not Found
