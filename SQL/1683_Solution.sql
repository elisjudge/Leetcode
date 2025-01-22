SELECT tweet_id
FROM Tweets
WHERE length(content) > 15;

-- -- MySQL can also use CHAR_LENGTH
-- SELECT tweet_id
-- FROM Tweets
-- WHERE CHAR_LENGTH(content) > 15;

