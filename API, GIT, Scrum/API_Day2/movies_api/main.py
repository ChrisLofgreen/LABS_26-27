#pip install "fastapi[standard]"
#python -m fastapi dev main.py
#git init
#git status

import os
from dotenv import load_dotenv
from fastapi import Depends, Header

load_dotenv("secrets/.env")

api_key = os.getenv("API_KEY")


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



# Check key function for part 3
def check_key(x_api_key: str | None = Header(default=None)):
    expected = api_key
    if x_api_key is None or x_api_key != expected:
        raise HTTPException(status_code=401, detail="Invalid API key")


# 2. 

@app.get("/movies/{movie_id}")
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


@app.post("/movies", status_code=201, dependencies=[Depends(check_key)])
def add_movie(movie: Movie):
    new_id = max((mov["id"] for mov in movies), default=0) + 1
    new_movie = {"id": new_id, "title": movie.title, "director": movie.director, "year": movie.year}
    movies.append(new_movie)
    return new_movie

# If no director it gives Code: 422, Error: Unprocessable Content. It brings up both problems:
# "director" "msg": "Field required" and "year" "msg": "Input should be a valid integer, unable to parse string as an integer",


# 5.

@app.put("/movies/{movie_id}", dependencies=[Depends(check_key)])
def replace_movie(movie_id: int, movie: Movie):
    replace_id = get_movie(movie_id)
    replace_id["title"] = movie.title
    replace_id["director"] = movie.director
    replace_id["year"] = movie.year
    return replace_id

@app.delete("/movies/{movie_id}", status_code=204, dependencies=[Depends(check_key)])
def delete_movie(movie_id: int):
    delete_id = get_movie(movie_id)
    movies.remove(delete_id)

# The second time returns 404 Error: not found since it cannot find the movie with get_movie()
# Upon server restart the movies list is returned to the original state


# 6.

# Check, see client.py
# Responses as expected




# Part 2: PATCH


# 1.

class MovieUpdate(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None


@app.patch("/movies/{movie_id}", dependencies=[Depends(check_key)])
def update_movie(movie_id: int, changes: MovieUpdate):
    movie = get_movie(movie_id)
    update_data = changes.model_dump(exclude_unset=True)
    movie.update(update_data)

    return movie

# 2.

# Check


# 3.

# Empty body gives 200 but changes noting
# Year as text gives error 422
# Missing id gives error 404


# 4.

# Put might be useful if there is a reason to replace every field, like a product being replaced with a new model, but even then...
# Wouldnt you want a new id for the new model!? Ok, any situation where a full change of all fields are required an non shall remain untuched,
# A full anonymization maybe? PUT makes sure that all fields are taken care of, so it could be used for that.
# PATCH seems like the right choice for almost every scanario exept the ones described above.



# Part 3: Protect your API with a key


# 1-4.

# Check


# 5.

# without key: 401
# with key: 204
# wrong key: 401


# 6.

# without key: 401
# with key: 201


# 7.

# Check