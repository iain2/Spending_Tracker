PRAGMA FOREIGN_KEYS = ON;

DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS users;

CREATE TABLE tags(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    active BOOLEAN
);

CREATE TABLE merchants(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR
    -- logo of merchant
    -- availability BOOL
);

CREATE TABLE transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount INT,
    date DATE,
    tag_id INTEGER NOT NULL,
    merchant_id INTEGER NOT NULL,
        FOREIGN KEY (tag_id)
            REFERENCES tags(id),
        FOREIGN KEY (merchant_id)
            REFERENCES merchants (id)
    );

CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount INT,
    name VARCHAR
);
