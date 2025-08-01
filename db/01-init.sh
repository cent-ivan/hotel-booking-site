#!/bin/bash
set -e
export PGPASSWORD=$POSTGRES_PASSWORD;
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  BEGIN;
    CREATE TABLE customertbl (
        customerID SERIAL PRIMARY KEY,
        public_uuid UUID UNIQUE NOT NULL,
        firstname VARCHAR(255) NOT NULL,
        lastname VARCHAR(255) NOT NULL,
        gender VARCHAR(8) NOT NULL,
        contactnumber VARCHAR(30) NOT NULL,
        email VARCHAR(255) NOT NULL,
        address VARCHAR(255) NOT NULL,
        country VARCHAR(10) NOT NULL
    );

    CREATE TABLE employeetbl(
        -- Custom ID--
        employeeID VARCHAR PRIMARY KEY,
        firstname VARCHAR(255) NOT NULL,
        lastname VARCHAR(255) NOT NULL,
        gender VARCHAR(8) NOT NULL,
        contactnumber VARCHAR(50) NOT NULL ,
        email VARCHAR(255) NOT NULL,
        address VARCHAR(255) NOT NULL ,
        role VARCHAR NOT NULL,
        password VARCHAR NOT NULL,
        createdon DATE NOT NULL
    );

    CREATE TABLE roomtypestbl (
        room_typeID SERIAL PRIMARY KEY,
        name VARCHAR(20) NOT NULL,
        price DECIMAL(8,2) NOT NULL,
        description VARCHAR NOT NULL,
        note VARCHAR,
        size DECIMAL(8,3) NOT NULL,
        capacity INT NOT NULL,
        capacitytype VARCHAR(50) NOT NULL,
        childrencapacity INT NOT NULL,
        bedtype VARCHAR(20) NOT NULL,
        amenities TEXT [],
        imageurl TEXT NOT NULL
    );

    CREATE TABLE roomstbl (
        roomID SERIAL PRIMARY KEY,
        room_typeID INT NOT NULL,
        roomnumber INT NOT NULL,
        status VARCHAR(20) DEFAULT 'available',
        CONSTRAINT fk_room_type
            FOREIGN KEY (room_typeID)
            REFERENCES roomtypestbl(room_typeID)
            ON UPDATE CASCADE
            ON DELETE CASCADE
    );

    CREATE TABLE promotbl (
        -- Custom ID--
        promoID VARCHAR PRIMARY KEY,
        discount DECIMAL(8,2) NOT NULL,
        description VARCHAR(30) 
    );

    CREATE TABLE bookingtbl( 
		bookingID SERIAL PRIMARY KEY, 
        public_uuid UUID NOT NULL, 
		customerID INT NOT NULL,
        checkin DATE NOT NULL,
        checkout DATE NOT NULL,
        request VARCHAR(255) NOT NULL,
        promoID VARCHAR,
        totalprice DECIMAL(8,2) NOT NULL,
        status VARCHAR(255) NOT NULL DEFAULT 'PENDING',
        createdon DATE NOT NULL,
		Constraint fk_customer
            FOREIGN KEY(customerID)
            REFERENCES customertbl(customerID)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
        Constraint	fk_promo
            FOREIGN KEY(promoID)
            REFERENCES promotbl(promoID)
            ON DELETE CASCADE
            ON UPDATE CASCADE
		); 
    CREATE TABLE reservationtbl(
        bookingID INT NOT NULL,
        roomID INT NOT NULL,
        roomqty INT NOT NULL,
        adults INT NOT NULL,
        children INT,
        PRIMARY KEY (bookingID, roomID),
        CONSTRAINT fk_booking
            FOREIGN KEY (bookingID)
            REFERENCES bookingtbl(bookingID)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
        CONSTRAINT fk_room
            FOREIGN KEY (roomID)
            REFERENCES roomstbl(roomID)
            ON UPDATE CASCADE
            ON DELETE CASCADE
    );

    --SAMPLE DATA NOT REAL

    -- Deluxe Room
    INSERT INTO roomtypestbl(room_typeid, name, price, description, note, size, capacity, capacitytype, childrencapacity, bedtype, amenities, imageurl)
    VALUES (
        1,
        'Deluxe Room',
        3500.00,
        'A spacious deluxe room perfect for couples or solo travelers.',
        'Inclusive of breakfast and free WiFi. For adults only',
        32,
        2,
        'Adults',
        0,
        '1 Queen Bed',
        ARRAY['Free WiFi', 'Air Conditioning', 'Flat Screen TV', 'Private Bathroom', 'Mini Bar', 'Desk', 'Hair Dryer'],
        'https://yourcdn.com/images/deluxe-room.jpg'
    );

    -- Family Suite
    INSERT INTO roomtypestbl(room_typeid, name, price, description, note, size, capacity, capacitytype, childrencapacity, bedtype, amenities, imageurl)
    VALUES (
        2,
        'Family Suite',
        5800.00,
        'Ideal for families with spacious living and sleeping areas.',
        'Children below 6 stay free with parents.',
        50,
        4,
        'Persons',
        2,
        '2 Double Beds',
        ARRAY['Free WiFi', 'Air Conditioning', 'Flat Screen TV', 'Private Bathroom', 'Mini Bar', 'Kitchenette', 'Sofa', 'Bathtub'],
        'https://yourcdn.com/images/family-suite.jpg'
    );

    -- Executive Suite
    INSERT INTO roomtypestbl(room_typeid, name, price, description, note, size, capacity, capacitytype, childrencapacity, bedtype, amenities, imageurl)
    VALUES (
        3,
        'Executive Suite',
        7200.00,
        'Premium suite with separate living area and executive workspace.',
        'Access to Executive Lounge included. Children below 6 stay free with parents.',
        65,
        2,
        'Persons',
        1,
        '1 King Bed',
        ARRAY['Free WiFi', 'Air Conditioning', 'Smart TV', 'Private Bathroom', 'Coffee Machine', 'Workspace Desk', 'Jacuzzi', 'Lounge Access'],
        'https://yourcdn.com/images/executive-suite.jpg'
    );

    -- Standard Room
    INSERT INTO roomtypestbl(room_typeid, name, price, description, note, size, capacity, capacitytype, childrencapacity, bedtype, amenities, imageurl)
    VALUES (
        4,
        'Standard Room',
        2500.00,
        'A basic but comfortable room for short stays or business travelers.',
        'Limited availability on weekends. Children below 6 stay free with parents.',
        25,
        2,
        'Persons',
        1,
        '1 Double Bed',
        ARRAY['Free WiFi', 'Air Conditioning', 'Flat Screen TV', 'Private Bathroom'],
        'https://yourcdn.com/images/standard-room.jpg'
    );

    INSERT INTO roomstbl(room_typeID, roomnumber) VALUES (1, 401), (1, 402), (2, 301), (3, 201), (4, 101);

  COMMIT;
EOSQL