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