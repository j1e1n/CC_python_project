DROP TABLE journal_entries;
DROP TABLE places;
DROP TABLE countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE places (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    visited BOOLEAN,
    country_id INT REFERENCES countries(id) ON DELETE CASCADE
);


CREATE TABLE journal_entries (
    id SERIAL PRIMARY KEY,
    place_id INT REFERENCES places(id) ON DELETE CASCADE,
    journal_entry VARCHAR(255)
);