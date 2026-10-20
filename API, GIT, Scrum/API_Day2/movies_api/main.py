#pip install "fastapi[standard]"
#python -m fastapi dev main.py


# Part 1: Your own API

# 1.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()



movies = [
    {"id": 1, "title": "Terminator 2", "director": "James Cameron", "year": 1991},
    {"id": 2, "title": "Fire Walk with Me", "director": "David Lynch", "year": 1992},
    {"id": 3, "title": "Life of Brian", "director": "Terry Jones", "year": 1979},
    {"id": 4, "title": "Modern Times", "director": "Charlie Chaplin", "year": 1936}
]
'''
@app.get("/movies")
def get_movies():
    return movies
'''
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
#print(get_movie("abc"))  # Also returns fastapi.exceptions.HTTPException: 404: Not Found, but in docs it stops on the fact that it is not an int


# 3.

@app.get("/movies")
def get_movies(director: str | None = None, year: int | None = None):
    filtered = []
    if director != None or year != None:
        for movie in movies:
            if movie["director"].lower() == director.lower() or movie["year"] == year:
                filtered.append(movie)

    if len(filtered) > 0:
        return filtered
    else:
        return movies
    
# print(get_movies("james cameron", 1992))


# 4.

class Movie(BaseModel):
    title: str
    director: str
    year: int


@app.post("/movies", status_code=201)
def add_movie(movie: Movie):
    new_id = max((mov["id"] for mov in movies), default=0) + 1
    new_movie = {"id": new_id, "title": movie.title, "director": movie.director, "year": movie.year}
    movies.append(new_movie)
    return new_movie

# If no director it gives Code: 422, Error: Unprocessable Content. It brings up both problems:
# "director" "msg": "Field required" and "year" "msg": "Input should be a valid integer, unable to parse string as an integer",


# 5.

