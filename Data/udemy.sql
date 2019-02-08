CREATE TABLE udemy(
	id INT,
	avg_rating_recent NUMERIC,
	objectives_summary TEXT,
	num_subscribers NUMERIC,
	content_info TEXT,
	headline TEXT,
	image_304x171 TEXT,
	title TEXT,
	url TEXT,
	language TEXT,
	category TEXT,
	description TEXT    
);
COPY udemy FROM '/Udemy.csv' WITH DELIMITER ',' HEADER CSV;      