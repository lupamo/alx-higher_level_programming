-- Import the database dump of hbtn_0d_tvshows to your MySQL
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genres
	RIGHT JOIN tv_shows
	ON tv_shows.id = tv_show_genres.show_id
	ORDER BY tv_shows.title, tv_show_genres.genre_id;

