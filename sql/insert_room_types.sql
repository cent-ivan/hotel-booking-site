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