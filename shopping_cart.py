import csv
import pandas
import os 

from datetime import datetime

import smtplib


csv_filepath = os.path.join(os.path.dirname(__file__), "data", "products.csv")
products = pandas.read_csv(csv_filepath)

# I found this bit on inserting the current date and time from Stack Overflow
now = datetime.now()
current_time = now.strftime("%m-%d-%Y %I:%M:%S %p")

print("----------------------")
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
nfile = open("Receipt.txt", "w+")

print("----------------------------------")
print("----------------------------------")
print("JAYSON CORNER STORE")
print("Store #023: St. Pete Beach, FL")
print("Tel: (727) 437-9655")
print("www.jaysongrocery.com")
print("----------------------------------")
print("CHECKOUT:", current_time)
print("----------------------------------")
print("SELECTED PRODUCTS:")
nfile.write("----------------------------------\n")
nfile.write("----------------------------------\n")
nfile.write("JAYSON CORNER STORE\n")
nfile.write("Store #023: St. Pete Beach, FL\n")
nfile.write("Tel: (727) 437-1233\n")
nfile.write("www.jaysongrocery.com\n")
nfile.write("----------------------------------\n")
nfile.write("CHECKOUT: ")
nfile.write(current_time)
nfile.write("\n")
nfile.write("----------------------------------\n")
nfile.write("SELECTED PRODUCTS:\n")

for item in items:
    for index,row in products.iterrows():
        if item == row["id"]:
            print("...", row["name"], "(${0:.2f})".format(row["price"]))
            prices.append(row["price"])
            nfile.write(row["name"])
            nfile.write("(${0:.2f})".format(row["price"]))
            nfile.write(" \n")
print("----------------------------------")
subtotal = sum(prices)
print("SUBTOTAL: ", "${0:.2f}".format(subtotal))
tax = subtotal*(.0875)
print("TAX: ", "${0:.2f}".format(tax))
total = subtotal + tax
print("TOTAL: ", "${0:.2f}".format(total))
print("----------------------------------")
nfile.write("----------------------------------\n")
nfile.write("SUBTOTAL: ")
nfile.write("${0:.2f}".format(subtotal))
nfile.write("\n")
nfile.write("TAX: ")
nfile.write("${0:.2f}".format(tax))
nfile.write("\n")
nfile.write("TOTAL: ")
nfile.write("${0:.2f}".format(total))
nfile.write("\n")
nfile.write("Thank you for shopping with us!")
nfile.close()



copy = input("Would you like to send a copy of the receipt via email? ")
if copy.lower() == "yes":
    fromaddr = input("Please enter your employee email address: ")
    # I could not quite figure out the environment setup for a hidden file containing my password,
    # so I just allowed another user input here
    password = input("Please enter your password: ")
    toaddr = input("Please enter the customer's email address: ")
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(fromaddr, password)
    myfilehandle = open("Receipt.txt", "r")
    message = myfilehandle.read()
    myfilehandle.close()
    s.sendmail(fromaddr, toaddr, message) 
    s.quit()
    print("----------------------------------")
    print("THANK YOU, COME AGAIN SOON!")
else:
    print("----------------------------------")
    print("THANK YOU, COME AGAIN SOON!")







