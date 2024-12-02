#
# Example: Get an exchange rate quote
# Demonstrates using an HTTP API.
#
import requests
import sys

API_KEY = "demo"  # Add your key to get all the data
                  # This only works for EUR -> USD


def make_api_call(url):
    """
    Makes a request to a url endpoint that responds in json and returns
    the result as a python data structure (a list or dictionary).
    """
    return requests.get(url).json()

#https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&apikey=demo
# PROBLEM: Finish this function to properly add the request parameters.
def build_url(from_curr, to_curr):
    """ Build and return FX_DAILY request url for from_curr -> to_curr
    """
    url = "https://www.alphavantage.co/query"
    url += "?function=FX_DAILY"
    url += f"&from_symbol={from_curr}"
    url += f"&to_symbol={to_curr}"
    url += f"&apikey={API_KEY}"
    print("Using url ", url)
    return url


def get_fx_daily_data(from_curr, to_curr):
    """ Make an Alphavantage query to get daily currency exchange data
    from_curr - the currency to exchange from
    to_curr - the currency to exchange to
    Returns a dictionary with the exchange data.
    """
    url = build_url(from_curr, to_curr)
    return make_api_call(url)


# PROBLEM: Get the FX_DAILY data for EUR -> USD and print out the date
# and closing exchange rate for each item in the response.
def main():
  data = get_fx_daily_data("EUR", "USD")
  time_series = data["Time Series FX (Daily)"]
  for date, prices in time_series.items():
    print(date, prices["4. close"])


if __name__ == "__main__":
    main()
