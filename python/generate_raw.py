import csv
import random
import faker

# Create a Faker generator for generating random names
fake = faker.Faker()

# Generate 100 random records
num_records = 100
data = []
for _ in range(num_records):
    record = {
        'id': _ + 1,
        'first_name': fake.first_name(),
        'last_name': fake.last_name()
    }
    data.append(record)

# Specify the CSV file path
csv_file_path = 'names.csv'

# Write the data to the CSV file
with open(csv_file_path, mode='w', newline='') as csv_file:
    fieldnames = ['id', 'first_name', 'last_name']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for record in data:
        writer.writerow(record)

print(f"{num_records} records written to '{csv_file_path}' successfully.")