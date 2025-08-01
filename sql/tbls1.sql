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
