-- Import the database dump from hbtn_0d_tvshows to your MySQL serve
-- Each record displays: tv_shows.title - tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_shows_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title, tv_show_genres.genre_id;

