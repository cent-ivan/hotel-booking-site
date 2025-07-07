CREATE TABLE customertbl (
    customerID SERIAL PRIMARY KEY,
    firstname VARCHAR(20) NOT NULL,
    lastname VARCHAR(20) NOT NULL,
    gender VARCHAR(8) NOT NULL,
    contactnumber INT NOT NULL,
    email VARCHAR(20) NOT NULL,
    address VARCHAR(20) NOT NULL,
    country VARCHAR(10) NOT NULL
);