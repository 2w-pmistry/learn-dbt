import csv
import random
from datetime import datetime, timedelta

# Define the last date from the provided data
last_date = datetime(2018, 4, 9)

# Define today's date for iteration
today = datetime.now()

# Create a list to hold the new order data entries
new_orders = []

# Generate order data up to today's date
order_id = 100  # starting from the last id in your sample
while last_date <= today:
    order_id += 1
    user_id = random.randint(1, 100)
    last_date += timedelta(days=random.randint(1, 3))
    status = random.choice(['completed', 'returned', 'return_pending', 'shipped', 'placed'])
    new_orders.append([order_id, user_id, last_date.strftime('%Y-%m-%d'), status])

# Write the new order data to a CSV file
with open('seeds/raw_orders_extended.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'user_id', 'date', 'status'])  # header row
    for item in new_orders:
        writer.writerow(item)

# Extract the last payment id from the given data
last_payment_id = 113

# Payment method possibilities
payment_methods = ['credit_card', 'coupon', 'bank_transfer', 'gift_card']

# Create a list to hold the new payment data entries
new_payments = []

# Generate payment data for each new order
for order in new_orders:
    last_payment_id += 1
    current_order_id = order[0]
    method = random.choice(payment_methods)
    
    # Randomly generating amount for simplicity; can be modified as per requirements
    amount = random.randint(100, 3000)
    
    if method == 'coupon':
        amount = random.randint(0, 1000)
    elif method == 'gift_card':
        amount = random.randint(0, 2000)
        
    new_payments.append([last_payment_id, current_order_id, method, amount])

# Write the new payment data to a CSV file
with open('seeds/raw_payments_extended.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'order_id', 'payment_method', 'amount'])  # header row
    for item in new_payments:
        writer.writerow(item)

print("Extended order data has been written to raw_orders_extended.csv")
print("Extended payment data has been written to raw_payments_extended.csv")
