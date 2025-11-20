-- CREATE TABLE study_webscripings_database (
--     contents varchar(500),
--     link varchar(500),
--     link_html varchar(500),
--     link_href varchar(500)
-- );

CREATE TABLE study_webscripings_database (
    id varchar(500) PRIMARY KEY,
    contents varchar(500),
    link varchar(500),
    link_html varchar(500),
    link_href varchar(500),
    created_at varchar(500) DEFAULT NOW()
);


SELECT * FROM study_webscripings_database;

INSERT INTO study_webscripings_database (contents, link, link_html, link_href)
VALUES 
    ('Sample Content 1', 'https://example.com/1', '<html>...</html>', 'https://example.com/1'),
    ('Sample Content 2', 'https://example.com/2', '<html>...</html>', 'https://example.com/2');