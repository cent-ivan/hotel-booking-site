CREATE TABLE roomtypestbl (
    room_typeID SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    price DECIMAL(8,2) NOT NULL,
    description VARCHAR NOT NULL,
    note VARCHAR,
    size DECIMAL(8,3) NOT NULL,
    capacity VARCHAR(10) NOT NULL,
    bedtype VARCHAR(20) NOT NULL,
    amenities TEXT [],
    imageurl TEXT NOT NULL
);

