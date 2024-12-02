import json
import requests

# Uncomment this and add your own key for the pset:
KEY = "LQO97LCDCBF58OSS"


# Call this with your API url to get your data from the service
# You don't have to add anything to this.
def make_api_call(url):
    """
    Makes a request to a url endpoint that responds in json and returns
    the result as a python data structure (a list or dictionary).
    This is a very optimistic function and doesn't check for errors.
    """
    return requests.get(url).json()


# Build your api url here. See
# https://www.alphavantage.co/documentation/#dailyadj
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=LQO97LCDCBF58OSS
# do decide what values to add for the parameters.
def build_url(symbol):
    url = "https://www.alphavantage.co/query?"
    url += "function=TIME_SERIES_DAILY&"
    url += f"symbol={symbol}"#makes variable, so that the stock can be chosen
    url += f"&apikey={KEY}"
    return url


# Use this API url with your key and symbol
def get_quotes(symbol):
    """
    Takes a stock symbol and returns a list of tuples with the date
    and closing price for the last hundred days, for example,
    [ ('2022-07-15', '256.7200'), ('2021-07-15', '254.0800'), ... ]
    """
    url = build_url(symbol)  # gets url
    data = make_api_call(url)  # gets data
    x = data[
        "Time Series (Daily)"
    ]  # x is dictionary with dates and all info abt each date
    results = []
    dates = list(x.keys())  # makes dates from the ditionary
    for i in range(100):  # gets 100 days
        date = dates[i]
        close = float(
            x[date]["4. close"]
        )  # float so I can make it 2 decimalplaces at the end for format
        results.append((date, close))  # adds each day and close as a tuple to a list
    return results


def main():
    symbol = input("Enter a stock symbol: ")
    quotes = get_quotes(symbol)
    print(f"Date and closing price for {symbol}:")
    print("Date           Price")
    for date, price in quotes:  # gets each part of the tuple
        print(f"{date}    ${price:.2f}")


if __name__ == "__main__":
    main()
