from sqlalchemy import create_engine, text
DB_URL = "sqlite:///movies.db"

# Create the engine
engine = create_engine(DB_URL, echo=True)


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
        return 0

# def commit_query(query, params):
#     """uizu"""
#     try:
#         with engine.begin() as connection:
#             connection.execute(text(query), params)
#             connection.commit()
#     except Exception as e:
#         print(e)

# def list_movies():
#     """Retrieve all movies from the database."""
#     query = "SELECT title, year, rating, poster_url FROM movies"
#     movies = execute_query(query)
#     print(movies)
#     return {row[0]: {"year": row[1], "rating": row[2], "poster_url":row[3]} for row in movies}

#print("list movie",list_movies())
print("last line",execute_query("SELECT * FROM movies"))