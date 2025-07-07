CREATE TABLE employeetbl(
    -- Custom ID--
    employeeID VARCHAR PRIMARY KEY,
    firstname VARCHAR(20) NOT NULL,
    lastname VARCHAR(20) NOT NULL,
    gender VARCHAR(8) NOT NULL,
    contactnumber INT NOT NULL ,
    email VARCHAR(20) NOT NULL,
    address VARCHAR(20) NOT NULL ,
    role VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    createdon DATE NOT NULL
);