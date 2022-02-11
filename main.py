import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
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

        # base currency is USD so convert to that first
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

        # round to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount



def generateGraph(returned_data):
    # Creating pandas dataframe
    df = pd.DataFrame(returned_data)

    # X axis dates, y axis exchange rates
    x = df['date']
    y = df['exchange_rate']

    # Plot the date on x-axis in every 5 day
    plt.xticks(np.arange(0, len(returned_data), 5))

    # labels
    plt.xlabel('Date')
    plt.ylabel('Exchange Rates')

    plt.plot(x, y)
    plt.savefig('graph.png')
    plt.show()


def generateJSON(url):
    # parse and put in mongodb, using json just for testing api now
    response = requests.get(url)
    historical_rates = json.loads(response.text)
    #get 'rates' from the set
    rates_by_date = historical_rates['rates']
    historical_data = []
    for key, value in rates_by_date.items():
        historical_dict = {'date': key, 'exchange_rate': value} #['TRY']
        historical_data.append(historical_dict)

    historical_data.sort(key=lambda x: x['date'])
    return historical_data


url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = LiveCurrencyConverter(url)
print("Converter Created")

returned_data = []
returned_data = generateJSON(url)
print("JSON generated")

generateGraph(returned_data)
print("Graph Generated")

# test print
result = converter.convert('EUR', 'USD', 100)
string = str(result)
print("100 EURO is worth " + string + " USD")