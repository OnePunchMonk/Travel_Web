CREATE TABLE IF NOT EXISTS Users (
    user_id VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255),
    email VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    mobile_num INT(10)
);

CREATE TABLE IF NOT EXISTS Destinations (
    destination_id INTEGER PRIMARY KEY,
    location_name TEXT,
    price_adults REAL,
    price_children REAL
);

CREATE TABLE IF NOT EXISTS Query (
    query_id INTEGER PRIMARY KEY,
    user_name TEXT,
    email TEXT,
    subject TEXT,
    message TEXT
);

CREATE TABLE IF NOT EXISTS Bookings (
    booking_id INTEGER PRIMARY KEY,
    user_id VARCHAR(255),
    destination_id INTEGER,
    check_in_date DATE,
    num_children INTEGER,
    num_adults INTEGER,
    total_price REAL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (destination_id) REFERENCES Destinations(destination_id)
);
