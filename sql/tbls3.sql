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