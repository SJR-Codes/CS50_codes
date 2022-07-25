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
    ...

"""