SELECT  bookingtbl.bookingid, roomstbl.roomid, roomqty, adults, children, 
 bookingtbl.public_uuid,  bookingtbl.checkin, bookingtbl.checkout, bookingtbl.request, bookingtbl.promoid, bookingtbl.totalprice, bookingtbl.status, bookingtbl.createdon,  
 customertbl.firstname, customertbl.lastname, customertbl.gender, customertbl.contactnumber, customertbl.email, customertbl.address, customertbl.country,
 roomstbl.roomnumber, roomstbl.status, 
 roomtypestbl.room_typeid, roomtypestbl.name, roomtypestbl.price FROM reservationtbl 
 INNER JOIN bookingtbl ON reservationtbl.bookingid = bookingtbl.bookingid 
 INNER JOIN customertbl ON bookingtbl.customerid = customertbl.customerid
 INNER JOIN roomstbl ON reservationtbl.roomid = roomstbl.roomid
 INNER JOIN roomtypestbl ON roomstbl.room_typeid  = roomtypestbl.room_typeid
 WHERE bookingtbl.public_uuid =  %s;
