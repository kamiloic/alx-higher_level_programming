-- Lists all genres not linked to the show Dexter in the hbtn_0d_tvshows database.
-- Each record displays: tv_genres.name
-- Results are sorted in ascending order by the genre name.
-- A maximum of two SELECT statements are used.
SELECT DISTINCT tg.name
    FROM tv_genres tg
    LEFT JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
    LEFT JOIN tv_shows ts ON tsg.show_id = ts.id AND ts.title = 'Dexter'
    WHERE ts.id IS NULL
    ORDER BY tg.name;
