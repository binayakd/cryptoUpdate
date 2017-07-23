# cryptoUpdate
Short python script to record data from Nanopool cryptocurrency mining account into Google sheets

## Libraries Used
- [Requests](http://docs.python-requests.org/en/master/) (get JSON data from Nanopool API)
- [Google Spreadsheets Python API](https://github.com/burnash/gspread) (connect and write to Google spreadsheets)
- [oauth2client](https://github.com/google/oauth2client) (Authorization to connect to Google Sheets)
- [JSON](https://docs.python.org/2/library/json.html) (parsing JSON data from Nanopool and credential file from Google)
- [time](https://docs.python.org/2/library/time.html) (getting local time and date)

## Getting JSON data from Nanopool API
Nanopool provides API endpoints to extract various kinds of data for your mining pool:
- https://eth.nanopool.org/api

Choose one to get the relevent data you need.

## Authorization to connect to Google Sheets
Proper credentials have to be generated and applied for your script to be able to connect and write to the google sheets:
- http://gspread.readthedocs.io/en/latest/oauth2.html

## Connecting and wrting to Google Sheets
The main list of gspread API references are given here:
- http://gspread.readthedocs.io/en/latest/

In this script the sheet file to be written to is selected using the url: `gclient.open_by_url(url)` <br>
The sheet is selected using the index, which is zero-indexed: `worksheet.get_worksheet(index)` <br>
The list of values are appened to the worksheet: `sheet.append_row(value_list)` <br>
Be sure to delete any existing empty rows, as the values will only be appended after those empty rows.
