import sys
import requests
import tkinter as tk
from tkinter import ttk, font

from tkinter import CENTER

import self as self


class LiveCurrencyConverter:

    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']


    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount

        #base currency is USD so convert to that first
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

        #round to 4 decimal places
        amount = round(amount * self.currencies[to_currency],4)
        return amount






url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = LiveCurrencyConverter(url)

#test print
result = converter.convert('EUR','USD',100)
string = str(result)
print( "100 EURO is worth " + string + " USD")




