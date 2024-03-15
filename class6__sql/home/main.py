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

actorQuery = """
SELECT title, premiered, name
FROM titles
JOIN crew
ON crew.title_id == titles.title_id
JOIN people
ON people.person_id == crew.person_id
WHERE people.name IN ({})
ORDER BY premiered DESC
"""

def filmsByActors(*actors):
	placeholders = ', '.join(['?'] * len(actors))
	return cur.execute(actorQuery.format(placeholders), actors).fetchall()

genreByYearQuery = """
SELECT premiered, count(titles.title_id)
FROM titles
JOIN film_genres
ON film_genres.title_id == titles.title_id
JOIN genre_types
ON genre_types.id == film_genres.genre_id
WHERE genre_name == ?
GROUP BY premiered
"""

def filmsByGenre(genre):
	return cur.execute(genreByYearQuery, (genre,)).fetchall()

actorsByAgeQuery = """
SELECT name, born, died,
	CASE
		WHEN died IS NOT NULL THEN died - born
		ELSE CURRENT_DATE - born
	END AS age
FROM crew
JOIN people ON people.person_id == crew.person_id
WHERE born IS NOT NULL
GROUP BY people.person_id
ORDER BY age DESC
LIMIT 10
"""

actorsAge100Query = """
SELECT name, born, died,
	CASE
		WHEN died IS NOT NULL THEN died - born
		ELSE CURRENT_DATE - born
	END AS age
FROM crew
JOIN people ON people.person_id == crew.person_id
WHERE born IS NOT NULL AND age >= 100
GROUP BY people.person_id
ORDER BY age DESC
"""
