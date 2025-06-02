import os
from dotenv import load_dotenv
import requests


load_dotenv()
API_KEY = os.getenv('API_KEY')


def fetch_data(movie_title):
    """
    Fetches the movie data for the movie 'title'.
    Returns: movie's data tuple.
    """
    api_url = f'http://www.omdbapi.com/?t={movie_title}'
    try:
        response = requests.get(api_url, params={'apikey': API_KEY})
        movie = response.json()
        if response.status_code == requests.codes.ok:
                try:
                    title = movie['Title']
                    rating = (movie['imdbRating'])
                    year = int(movie['Year'])
                    poster = movie['Poster']

                    return title, rating, year, poster
                except Exception as e:
                    print("Error movie was not found:", response.status_code, e)
        else:
            print(response.status_code)
    except Exception as e:
        print("Error in connection",e)
        return
