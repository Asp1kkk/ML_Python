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
