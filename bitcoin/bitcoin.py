"""
* CS50P Problem Set 4
* Bitcoin Price Index
* by Samu Reinikainen 25.07.2022
"""

import sys
import json
import requests as r

if len(sys.argv) != 2:
    sys.exit("Error: Argument missing!")
try:
    coins = float(sys.argv[1])
except ValueError:
    sys.exit("Error: Argument not float!")

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    response = r.get(url)
except requests.RequestException:
    sys.exit("Error connecting to coindesk.com!")

#    "bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"21,818.6220"

o = response.json()

try:
    rate = float((o["bpi"]["USD"]["rate"]))
except ValueError:
    sys.exit("Error: Rate not float!")
except IndexError:
    sys.exit("Error: rate not available!")


