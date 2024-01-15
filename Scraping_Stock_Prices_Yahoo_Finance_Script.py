# 1.0 Import Necessary Libraries
import requests
from bs4 import BeautifulSoup

# 2.0 Create a FUnction to Scrap, Ffetch and Extract Data
def getData(symbol):
    # Create custom headers as best practice
    headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    #
    # Set the url
    url = f'https://finance.yahoo.com/quote/{symbol}'
    #
    # Query the website and the server to get the data from yahoo finance page
    # Use get() method on the website
    response = requests.get(url, headers=headers)
    #
    # Parse the html content
    soup = BeautifulSoup(response.text, 'html.parser')
    #
    # Create dictionary that stores price and change data
    stock = {
        'symbol' : symbol,
        'price' : soup.find('fin-streamer', {'class' : 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text,
        'change' : soup.find('fin-streamer', {'class' : 'Fw(500) Pstart(8px) Fz(24px)'}).text,
    }
    return stock

# Print out stock
# print(getData('SCHD'))

# Create a For Loop
portfolio = ['QQQM', 'SCHD', 'VOO', 'DGRO', 'VYM', 'MSFT', 'AAPL', 'COST', 'LLY', 'NVDA', 'GOOG', 'SHOP', 'ANET', 'AMZN']
#
# Create empty list to store stockdata
stockdata = [] 

for item in portfolio:
    stockdata.append(getData(item))
    print('Getting: ', item)
    
print(stockdata)

# 3.0 Data Storage
import csv

# Assuming stockdata is a list of dictionaries
# and each dictionary represents a stock item

# Open a file for writing
with open('stockdata.csv', 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)

    # Writing the header (column names)
    writer.writerow(stockdata[0].keys())

    # Writing the data rows
    for stock in stockdata:
        writer.writerow(stock.values())