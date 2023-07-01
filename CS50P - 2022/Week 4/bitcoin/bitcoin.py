import requests
import sys

if len(sys.argv) == 2:
    try:
        sum = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    r = response.json()
    bitcoin = r["bpi"]["USD"]["rate_float"] * sum
    print(f"${bitcoin:,.4f}")
except requests.RequestException:
    sys.exit("Request declined")