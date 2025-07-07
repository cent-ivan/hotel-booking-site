CREATE TABLE bookingtbl( 
		bookingID SERIAL PRIMARY KEY, 
		customerID INT NOT NULL,
        checkin DATE NOT NULL,
        checkout DATE NOT NULL,
        adults INT NOT NULL,
        children INT,
        request VARCHAR(50) NOT NULL,
        promoID VARCHAR,
        totalprice DECIMAL(8,2) NOT NULL,
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