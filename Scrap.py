from msilib.schema import tables
import urllib
from bs4 import BeautifulSoup
import json
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko)  Chrome/24.0.1312.57 Safari/537.17',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'
}

version = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17'


# myopener = MyOpener()
url = 'https://www.ccilindia.com/FPI_ARCV.aspx'
# first HTTP request without form data
f = urllib.request.urlopen(url)
soup_dummy = BeautifulSoup(f, "html5lib")
# soup_dummy = BeautifulSoup(f, "lxml")
# parse and retrieve two vital form values
viewstate = soup_dummy.select("#__VIEWSTATE")[0]['value']
# print('viewstate', viewstate)
viewstategen = soup_dummy.select("#__VIEWSTATEGENERATOR")[0]['value']
event_validation = soup_dummy.select("#__EVENTVALIDATION")[0]['value']

# formData = (
#     ('__VIEWSTATE', viewstate),
#     ('__VIEWSTATEGENERATOR', viewstategen),
#     ('__EVENTTARGET', 'drpArchival'),
#     ('drpArchival', '15-Sep-2022'),
#     ('__EVENTVALIDATION', event_validation)
# )
formData = {
    '__EVENTTARGET': 'drpArchival',
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategen,

    'drpArchival': '14-Sep-2022',
    '__EVENTVALIDATION': event_validation
}


encodedFields = urllib.parse.urlencode(formData)
# second HTTP request with form data
# f = myopener.open(url, encodedFields).status

f = urllib.request.urlopen(url, data=bytes(
    json.dumps(formData), encoding="utf-8"))

raw_data = f.read()

soup = BeautifulSoup(raw_data, "html5lib")
tables = soup.find_all("tr")
for table in tables:
    print('table:', table)
