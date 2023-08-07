import csv
import random
from datetime import datetime

# Read the data from raw_customer.csv
with open('seeds/raw_customers.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip the header row
    users = list(reader)

# Possible email domains for generating emails
domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'example.com']

# US Street names (fictional)
streets = ['Maple', 'Elm', 'Oak', 'Pine', 'Cedar', 'Birch', 'Cherry', 'Walnut', 'Spruce', 'Fir']

# US City, State, and Zip Code combinations
city_state_zip = [
    ('Dallas', 'Texas', '75001'),
    ('Los Angeles', 'California', '90001'),
    ('New York', 'New York', '10001'),
    ('Chicago', 'Illinois', '60601'),
    ('Houston', 'Texas', '77001'),
    ('Phoenix', 'Arizona', '85001'),
    ('Philadelphia', 'Pennsylvania', '19019'),
    ('San Antonio', 'Texas', '78201'),
    ('San Diego', 'California', '92101'),
    ('San Jose', 'California', '95101')
]

# Prepare the output
output = []

for user in users:
    id, first_name, last_name_initial = user
    
    # Generate random email
    random_number = random.randint(1, 100)
    domain = random.choice(domains)
    email = f"{first_name.lower()}.{last_name_initial.lower()}{random_number}@{domain}"
    
    # Generate random phone number
    phone = f"({random.randint(100,999)})-{random.randint(100,999)}-{random.randint(1000,9999)}"
    
    # Generate random address with accurate city, state, and zip
    street_name = random.choice(streets)
    city, state, zipcode = random.choice(city_state_zip)
    address = f"{random.randint(1,9999)} {street_name} St, {city}, {state} {zipcode}"
    
    # Generate random date of birth between 1950 and 2000
    birth_year = random.randint(1950, 2000)
    birth_month = random.randint(1, 12)
    max_day = 28 if birth_month == 2 else (30 if birth_month in [4, 6, 9, 11] else 31)
    birth_day = random.randint(1, max_day)
    dob = f"{birth_month}/{birth_day}/{birth_year}"
    
    output.append([id, first_name, last_name_initial, email, phone, address, dob])

# Write the data to a new CSV
with open('seeds/customers_detailed.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'first_name', 'last_name', 'email', 'phone', 'address', 'dob'])  # header row
    for row in output:
        writer.writerow(row)

print("Detailed customer data with accurate city-state-zip has been written to customers_detailed.csv")
