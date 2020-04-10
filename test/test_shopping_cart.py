import pytest
from datetime import datetime

from app.shopping_cart import to_usd, tax_rate, date_format, get_products, get_subtotal, get_tax

def test_tax():
    assert(tax_rate) == 0.0875
    assert get_tax(100) == 8.75

def test_to_usd():
    assert to_usd(4.50) == '$4.50'
    assert to_usd(4.5) == '$4.50'
    assert to_usd(4.5555) == '$4.56'
    assert to_usd(1234567890.5555) == '$1,234,567,890.56'

def test_dates():
    sample_date = datetime(2020, 4, 10, 15, 29, 00)
    assert date_format(sample_date) == '04-10-2020 03:29:00 PM'

def test_products():
    sample = get_products(12)
    assert sample['name'] == 'Chocolate Fudge Layer Cake'

def test_subtotal():
    sample_list = [1,2,3,4,5]
    assert get_subtotal(sample_list) == 15