from sqlalchemy import create_engine, text


# Define the database URL
DB_URL = "sqlite:///data/movies.db"

# Create the engine
engine = create_engine(DB_URL, echo=True)


def commit_query(query, params):
    """Execute query with parameters, does changes in table"""
    try:
        with engine.begin() as connection:
            connection.execute(text(query), params)
            connection.commit()
    except Exception as e:
        print(e)


def delete_table():
    """Delete movies table"""
    query = ("DROP TABLE IF EXISTS movies")
    commit_query(query, params=None)

def create_table():
    """Create the movies table if it does not exist."""
    query = ("""
            CREATE TABLE movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT UNIQUE NOT NULL,
                year INTEGER NOT NULL,
                rating REAL NOT NULL,
                poster_url TEXT
            )
        """)
    commit_query(query, params=None)


def execute_query(query, params=None):
    """
    Execute an SQL query with the params provided in a dictionary,
    and returns a list of records
    """
    try:
        with engine.connect() as conn:
            if params:
                results = conn.execute(text(query), params)
            else:
                results = conn.execute(text(query))
            rows = results.fetchall()
            return rows
    except Exception as e:
        print("Query error:", e)
        return []


def list_movies():
    """Retrieve all movies from the database."""
    query = "SELECT title, year, rating, poster_url FROM movies"
    movies = execute_query(query)
    return {row[0]: {"year": row[1], "rating": row[2], "poster":row[3]} for row in movies}


def add_movie(title, year, rating, poster):
    """Add a new movie to the database."""
    query = "INSERT INTO movies (title, rating, year, poster_url) VALUES (:title, :rating, :year, :poster)"
    params = {"title": title,  "rating": rating, "year": year, "poster": poster}
    commit_query(query, params)


def delete_movie(title):
    """Delete a movie from the database."""
    query = "DELETE FROM movies WHERE title = :title"
    params = {"title": title}
    commit_query(query, params)


def update_movie(title, rating):
    """Update a movie's rating in the database."""
    query = "UPDATE movies SET rating = :rating WHERE title = :title"
    params = {
        "title": title,
        "rating": rating
    }
    commit_query(query, params)

