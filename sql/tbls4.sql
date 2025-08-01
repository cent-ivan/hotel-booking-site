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