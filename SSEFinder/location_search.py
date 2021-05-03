import requests
import json
import pprint
import sys
from datetime import date, timedelta

# location = "Kam Lok Hin Chicken and Fish Pot"
location = "wrsakifohsdafsfofonfsdao asfhos adoifsoadfjso j isafj "
location.replace(" ", "%20")
url = "https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q=" + location
response = requests.get(url)

case_data = []

if response.status_code == 200:
    data = json.loads(response.text)
case_data.append(data)
pprint.pprint(case_data)
