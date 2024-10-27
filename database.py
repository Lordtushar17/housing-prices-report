import mysql.connector
import random

# Establish a connection to the MySQL server
connection = mysql.connector.connect(
    host='localhost',        # e.g., 'localhost'
    user='root',    # e.g., 'root'
    password='win19Ftu7'  # your MySQL password
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create a new database
cursor.execute("CREATE DATABASE IF NOT EXISTS housing_db")

# Use the new database
cursor.execute("USE housing_db")

# Create a new table for housing prices
cursor.execute("""
CREATE TABLE IF NOT EXISTS housing_prices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    zip_code VARCHAR(20),
    price DECIMAL(10, 2),
    bedrooms INT,
    bathrooms INT
)
""")

# Sample data for housing prices
addresses = [f"{random.randint(100, 999)} {random.choice(['Main St', 'Elm St', 'Maple Ave', 'Oak St'])}" for _ in range(50)]
cities = ['CityA', 'CityB', 'CityC', 'CityD', 'CityE']
states = ['State1', 'State2', 'State3']
zip_codes = [f"{random.randint(10000, 99999)}" for _ in range(50)]

# Inserting sample data into the table
for i in range(50):
    address = addresses[i]
    city = random.choice(cities)
    state = random.choice(states)
    zip_code = zip_codes[i]
    price = round(random.uniform(100000, 500000), 2)  # Random price between 100,000 and 500,000
    bedrooms = random.randint(1, 5)  # Random number of bedrooms between 1 and 5
    bathrooms = random.randint(1, 3)  # Random number of bathrooms between 1 and 3

    cursor.execute("""
        INSERT INTO housing_prices (address, city, state, zip_code, price, bedrooms, bathrooms)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (address, city, state, zip_code, price, bedrooms, bathrooms))

# Commit changes and close the connection
connection.commit()
cursor.close()
connection.close()

print("Database and table created, and 50 rows of sample data inserted into the housing_prices table.")
