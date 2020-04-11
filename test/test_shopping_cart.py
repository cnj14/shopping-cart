import pytest
from datetime import datetime

from app.shopping_cart import to_usd, tax_rate, date_format, get_products, get_subtotal, get_tax

def test_tax():
    # tax rate should be equal to 8.75%
    assert(tax_rate) == 0.0875
    # get_tax function should multiply param by 8.75%
    assert get_tax(100) == 8.75

def test_to_usd():
    # function should add dollar sign and transform numeric object into string
    assert to_usd(4.50) == '$4.50'
    # function should round to two decimal places
    assert to_usd(4.5) == '$4.50'
    assert to_usd(4.5555) == '$4.56'
    # function should apply commas for numbers greater than 1,000
    assert to_usd(1234567890.5555) == '$1,234,567,890.56'

def test_dates():
    # function should format a datetime object as MM-DD-YYYY HH-MM-SS and apply the 12-hour format
    sample_date = datetime(2020, 4, 10, 15, 29, 00)
    assert date_format(sample_date) == '04-10-2020 03:29:00 PM'

def test_products():
    # function should retrieve a dictionary element from list of products using ID number
    sample = get_products(12)
    assert sample['name'] == 'Chocolate Fudge Layer Cake'

def test_subtotal():
    # function should sum list objects
    sample_list = [1,2,3,4,5]
    assert get_subtotal(sample_list) == 15