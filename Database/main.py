import mysql.connector
# Establish a connection to the MySQL server
mydb = mysql.connector.connect(host='localhost', user='root', password='', database='webd')

if mydb.is_connected():
    print("Connected to MySQL")


cursor =mydb.cursor()


# Create the 'YourDatabaseName' database if it doesn't exist

# Use the 'YourDatabaseName' database

#cursor.execute('''CREATE TABLE IF NOT EXISTS Payments (payment_id INTEGER PRIMARY KEY, user_id INTEGER, booking_id INTEGER, payment_date DATE, payment_amount REAL, payment_method TEXT, FOREIGN KEY (user_id) REFERENCES Users(user_id), FOREIGN KEY (booking_id) REFERENCES Bookings(booking_id))''')

#cursor.execute('''CREATE TABLE IF NOT EXISTS DestinationsImages (image_id INTEGER PRIMARY KEY, destination_id INTEGER, image_url TEXT, image_description TEXT, FOREIGN KEY (destination_id) REFERENCES Destinations(destination_id))''')


#cursor.execute('''CREATE TABLE IF NOT EXISTS UserRoles (role_id INTEGER PRIMARY KEY, user_id INTEGER, role_name TEXT, role_description TEXT, FOREIGN KEY (user_id) REFERENCES Users(user_id))''')

cursor.execute("CREATE TABLE IF NOT EXISTS Users (user_id VARCHAR(255) PRIMARY KEY, password VARCHAR(255), email VARCHAR(255), first_name VARCHAR(255), last_name VARCHAR(255),mobile_num  INT(10) )")


cursor.execute("CREATE TABLE IF NOT EXISTS Destinations (destination_id INTEGER PRIMARY KEY, location_name TEXT, price_adults REAL,price_children REAL)")

cursor.execute("CREATE TABLE IF NOT EXISTS Query (query_id INTEGER PRIMARY KEY, user_name TEXT, email  TEXT  ,subject TEXT, message TEXT )")

cursor.execute("CREATE TABLE IF NOT EXISTS Bookings (booking_id INTEGER(20) PRIMARY KEY, user_id VARCHAR(255), destination_id INTEGER,  check_in_date DATE,num_children INTEGER,num_adults INTEGER , total_price REAL, FOREIGN KEY (user_id) REFERENCES Users(user_id), FOREIGN KEY (destination_id) REFERENCES Destinations(destination_id))")

mydb.commit()
mydb.close()

print("Database and tables created successfully.")

