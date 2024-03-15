import sqlite3

con = sqlite3.connect("../imdb_very_small.db")
cur = con.cursor()

yearQuery = """
SELECT title, premiered, runtime_min
FROM titles
WHERE premiered < 2018
ORDER BY premiered DESC
"""
