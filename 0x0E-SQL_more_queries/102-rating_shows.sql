-- Lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record displays: tv_shows.title - rating sum
-- Results are sorted in descending order by the rating.
-- Only one SELECT statement is used.
SELECT ts.title, SUM(tr.rating) as rating_sum
    FROM tv_shows ts
    INNER JOIN tv_shows_rate tr ON ts.id = tr.show_id
    GROUP BY ts.title
    ORDER BY rating_sum DESC;
