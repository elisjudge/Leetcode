CREATE TABLE IF NOT EXISTS Tweets (
    tweet_id INTEGER,
    content TEXT
);

DELETE FROM Tweets;

INSERT INTO Tweets (tweet_id, content) VALUES (1, 'Let us Code');
INSERT INTO Tweets (tweet_id, content) VALUES (2, 'More than fifteen chars are here!');
