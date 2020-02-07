import csv
import pandas
import os 
from datetime import datetime


csv_filepath = os.path.join(os.path.dirname(__file__), "data", "products.csv")
products = pandas.read_csv(csv_filepath)

# I found this bit on inserting the current date and time from Stack Overflow
now = datetime.now()
current_time = now.strftime('%Y-%m-%d %H:%M:%S')

print("--------------")
print("Welcome, user!")
print("Type an integer between 1 and 20 to reference a product ID, \n or type 'DONE' when all items have been checked out.")

items = []
stop = 0
while stop == 0:
    choice = input("Please input a product identification number: ")
    if choice == "DONE":
        stop += 1
    else:
        choice = int(choice)
        if choice in range(1,21):
            items.append(choice)
        else:
            print("Error -- no product with ID: ", choice)











