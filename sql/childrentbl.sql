CREATE TABLE childrentbl( 
    childrenID SERIAL PRIMARY KEY,
    bookingID INT,
    age INT,
    CONSTRAINT fk_booking
        FOREIGN KEY (bookingID)
        REFERENCES bookingtbl(bookingID)
        ON UPDATE CASCADE
        ON DELETE CASCADE

);