import mysql.connector
# Establish a connection to the MySQL server
mydb = mysql.connector.connect(host='localhost', user='root', password='', database='travel')

if mydb.is_connected():
    print("Connected to MySQL")


cursor=mydb.cursor()


# Create the 'YourDatabaseName' database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS travel")

# Use the 'YourDatabaseName' database

# Create the Users Table
cursor.execute("CREATE TABLE IF NOT EXISTS Users (user_id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(255),password VARCHAR(255),email VARCHAR(255),first_name VARCHAR(255), last_name VARCHAR(255) )")

# Create the Admins Table
#cursor.execute("CREATE TABLE IF NOT EXISTS Admins ( admin_id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255) )")

# Create the Destinations Table
cursor.execute("CREATE TABLE IF NOT EXISTS Destinations (destination_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),location VARCHAR(255),price DECIMAL(10, 2),rating DECIMAL(3, 2))")

# Create the Bookings Table
cursor.execute("CREATE TABLE IF NOT EXISTS Bookings (booking_id INT AUTO_INCREMENT PRIMARY KEY,user_id INT,destination_id INT,booking_date DATE,check_in_date DATE,check_out_date DATE,total_price DECIMAL(10, 2),FOREIGN KEY (user_id) REFERENCES Users(user_id),FOREIGN KEY (destination_id) REFERENCES Destinations(destination_id) )")

# Create the Reviews Table
cursor.execute(" CREATE TABLE IF NOT EXISTS Reviews (review_id INT AUTO_INCREMENT PRIMARY KEY,user_id INT,destination_id INT,rating DECIMAL(3, 2), comment TEXT,date_posted DATE, FOREIGN KEY (user_id) REFERENCES Users(user_id), FOREIGN KEY (destination_id) REFERENCES Destinations(destination_id) )")

# Commit the changes and close the connection
mydb.commit()
mydb.close()

print("Database and tables created successfully.")





