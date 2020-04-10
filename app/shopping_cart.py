import os
import pandas as pd
from datetime import datetime

csv_filepath = os.path.join(os.path.dirname(__file__), "data", "products.csv")
products = pd.read_csv(csv_filepath)

tax_rate = .0875

def date_format(time):
    return time.strftime("%m-%d-%Y %I:%M:%S %p")

def to_usd(price):
    return "${0:,.2f}".format(price)

def get_subtotal(l):
    return sum(l)

def get_tax(sub):
    return sub*tax_rate

def lines():
    print("----------------------------------")

def get_products(identifier):
    for index,row in products.iterrows():
        if identifier == row["id"]:
            return row

now = datetime.now()
current_time = date_format(now)

lines()
print("Welcome, user!")
print("Type an integer between 1 and 20 to reference a product ID, \n or type 'DONE' when all items have been checked out.")

items = []
stop = 0
while stop == 0:
    choice = input("Please input a product identification number: ")
    if choice.upper() == "DONE":
        stop += 1
    else:
        choice = int(choice)
        if choice in range(1,21):
            items.append(choice)
        else:
            print("Error -- no product with ID", choice,"-- Please try again!")

items.sort()
prices = []

lines()
lines()
print("JAYSON CORNER STORE")
print("Store #023: St. Pete Beach, FL")
print("Tel: (727) 437-9655")
print("www.jaysongrocery.com")
lines()
print("CHECKOUT:", current_time)
lines()
print("SELECTED PRODUCTS:")
for item in items:
    info = get_products(item)
    print("...", info["name"], to_usd(info["price"]))
    prices.append(info["price"])
lines()
subtotal = get_subtotal(prices)
print("SUBTOTAL: ", to_usd(subtotal))
tax = get_tax(subtotal)
print("TAX: ", to_usd(tax))
total = subtotal + tax
print("TOTAL: ", to_usd(total))
lines()
lines()
print("THANK YOU! PLEASE COME AGAIN SOON.")


