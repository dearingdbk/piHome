CREATE TABLE devices (
    id INTEGER PRIMARY KEY,
    controller VARCHAR(255),
    connection VARCHAR(255),
    active VARCHAR(8),
    type VARCHAR(255),
    state BOOLEAN,
    floor DECIMAL(4, 1),
    ceiling DECIMAL(4, 1),
    reading DECIMAL(4, 1),
    x INTEGER,
    y INTEGER
);

CREATE TABLE rooms (
    id INTEGER PRIMARY KEY,
    x INTEGER,
    y INTEGER,
    width INTEGER,
    height INTEGER
);