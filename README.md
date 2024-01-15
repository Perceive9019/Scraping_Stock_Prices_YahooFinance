# Yahoo Finance Stock Scraper

This project consists of a Python script designed to scrape, parse, and extract stock data from Yahoo Finance. It leverages the requests and BeautifulSoup libraries to fetch and parse HTML data, extracting key financial information about a list of specified stocks. The extracted data includes the stock symbol, its current price, and price change. Additionally, the script includes functionality to save this data into a CSV file for further analysis or record-keeping.

## Requirements
To run this script, you need the following:
   - Python 3.X
   - `requests` library
   - `BeautifulSoup` library
   - `csv` library (usually included in standard Python distribution)

You can install the required libraries (except `csv`) using pip:
`pip install requests beautifulsoup4`

## Usage

1. **Setting up the Portfolio:**

Edit the portfolio list in the script to include the stock symbols you want to track. By default, it includes a pre-defined set of stock/ETF symbols such as 'QQQM', 'SCHD', 'VOO', etc.

2. **Running the Script:**
Execute the script in your Python environment. It will iterate over each stock symbol in your portfolio list, scrape the relevant data from Yahoo Finance, and print the progress in the console.

3. **Output:**
The script stores the fetched data in a list of dictionaries, where each dictionary represents a stock item with its symbol, price, and change.
Finally, the script writes this data into a CSV file named stockdata.csv, creating a handy file that can be used for data analysis or record-keeping.

## Script Functionality

1. **getData Function:**

    - This is the core function that takes a stock symbol as input and returns a dictionary with the stock's symbol, price, and change.

2. **Data Scraping:**

    - The script sends an HTTP GET request to the Yahoo Finance page of the given stock symbol.
It then parses the HTML response to extract the needed data.

3. **Error Handling:**

    - Note: The current script does not include explicit error handling for network issues or HTML parsing. It's recommended to enhance the script with try-except blocks to handle potential exceptions.

4. **CSV Writing:**

    - The script uses Python's built-in csv library to write the scraped data into a CSV file.

## Customization

- You can customize the portfolio list as per your requirements.
- Further enhancements can be made to include more data points from

## License

This script is for educational purposes only. Always ensure compliance with Yahoo Finance's terms of service when scraping their website. Additionally, this script may need updates if Yahoo Finance changes its webpage structure or URL patterns.

**Unofficial APIs and Libraries:**
   - `yfinance`: A widely used open-source Python library that makes it easy to access Yahoo Finance data. Installation is straightforward using pip: `pip install    - yfinance --upgrade --no-cache-dir`. This library allows users to fetch a wide range of data including historical prices, dividends, and financial statements.
   - `Yahoo_fin`: Another open-source Python library similar to yfinance. It can be installed via pip and offers functionalities like fetching stock price data, financial statements, and stock option data.
