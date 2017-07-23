#!/usr/bin/env python
import time
import requests
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

 # local time and date
Time = time.strftime("%H:%M:%S")
date = time.strftime("%d/%m/%Y")

# nanopool API reference: https://eth.nanopool.org/api
url ="<url>" # appropriate nanopool API url goes here
data = requests.get(url).json()

# get relevent data, balance and 12 hour average hash rate
balance = data['data']['balance']
h12 = data['data']['avgHashrate']['h12']

# google sheets authorisation and integration with gspread (http://gspread.readthedocs.io/en/latest/oauth2.html)
json_key = json.load(open('creds.json')) # json credentials from google developer console
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope) # get email and key from creds
gclient = gspread.authorize(credentials) # authenticate with Google

#gspread API references: http://gspread.readthedocs.io/en/latest/#main-interface
book = gclient.open_by_url('<google sheet file url>') 
sheet = book.get_worksheet(<index>) #select sheet by index, zero-indexed
value_list = [date, Time, h12, balance] #collect data into a list
sheet.append_row(value_list) #append to the sheet, make sure no empty rows in the sheet before appending
