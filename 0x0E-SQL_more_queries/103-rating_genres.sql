-- Selects all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record displays: tv_genres.name - rating sum
-- Results are sorted in descending order by their rating.
-- Only one SELECT statement is used.
SELECT tg.name, SUM(tr.rating) as rating_sum
    FROM tv_genres tg
    INNER JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
    INNER JOIN tv_shows_rate tr ON tsg.show_id = tr.show_id
    GROUP BY tg.name
    ORDER BY rating_sum DESC;
