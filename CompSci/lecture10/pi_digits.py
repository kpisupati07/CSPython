import requests
from sys import argv
# PROBLEM: Use the pi delivery api https://pi.delivery/#apipi_get
#         to get some digits of pi


def make_api_call(url):
    '''
    Makes a request to a url endpoint that responds in json and returns
    the result as a python data structure (a list or dictionary).
    '''
    return requests.get(url).json()


def build_url(start, num_digits):
    url = "https://api.pi.delivery/v1/pi?"
    url += f"start={start}"
    url += f"&numberOfDigits={num_digits}"
    return url


def pi_digits(start, num_digits):
    url = build_url(start, num_digits)
    return make_api_call(url)



def main():
    if len(argv) != 3:
        print('Usage: python pi_digits.py start num_digits')
        return
    print("Welcome to the csci s-7 pi service!")
    start = int(argv[1])
    num_digits = int(argv[2])
    answer = pi_digits(start, num_digits)
    print(answer['content'])


if __name__ == "__main__":
    main()
