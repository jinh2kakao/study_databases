-- CREATE TABLE Persons (
--     PersonID int,
--     LastName varchar(255),
--     FirstName varchar(255),
--     Address varchar(255),
--     City varchar(255)
-- );


CREATE TABLE study_webscripings_database (
    id SERIAL PRIMARY KEY,
    contents TEXT,
    link TEXT,
    link_html TEXT,
    link_href TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);