import sqlite3

con = sqlite3.connect("../imdb_very_small.db")
cur = con.cursor()

yearQuery = """
SELECT title, premiered, runtime_min
FROM titles
WHERE premiered < 2018
ORDER BY premiered DESC
"""

ratingQuery = """
SELECT title, premiered, rating
FROM titles
JOIN rating
ON rating.title_id == titles.title_id
ORDER BY rating DESC
LIMIT 50
"""

comedyQuery = """
SELECt title, premiered, rating, votes, genre_name
FROM titles
JOIN rating
ON rating.title_id == titles.title_id
JOIN film_genres
ON film_genres.title_id == titles.title_id
JOIN genre_types
ON genre_types.id == film_genres.genre_id
WHERE premiered == 2019 AND genre_name == "Comedy" AND rating >= 7
ORDER BY VOTES DESC
LIMIT 10
"""