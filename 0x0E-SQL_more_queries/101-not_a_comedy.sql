-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- Each record displays: tv_shows.title
-- Results are sorted in ascending order by the show title.
-- A maximum of two SELECT statements are used.
SELECT ts.title
    FROM tv_shows ts
    WHERE ts.id NOT IN (
        SELECT tsg.show_id
        FROM tv_show_genres tsg
        INNER JOIN tv_genres tg ON tsg.genre_id = tg.id
        WHERE tg.name = 'Comedy'
    )
    ORDER BY ts.title;
