import sqlite3

def films(type, genre, rating):
	con = sqlite3.connect("/Users/yuliamusaeva/Downloads/imdb_very_small.db")
	cur = con.cursor()
	genre_query = """
	SELECT title, premiered, rating, genre_name, film_type
	FROM titles
	JOIN film_types
	ON film_types.id == titles.type
	JOIN film_genres
	ON film_genres.title_id == titles.title_id
	JOIN genre_types
	ON genre_types.id == film_genres.genre_id
	JOIN rating
	ON rating.title_id == titles.title_id
	WHERE film_type == ? AND genre_name == ? AND votes > 100000 AND rating > ?
	"""
	return cur.execute(genre_query, (type, genre, rating)).fetchall()

print(films("movie", "Comedy", 8))