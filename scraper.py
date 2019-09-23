import sys
sys.path.append(r"c:\users\ngora\appdata\local\packages\pythonsoftwarefoundation.python.3.7_qbz5n2kfra8p0\localcache\local-packages\python37\site-packages")
import requests
from bs4 import BeautifulSoup

ticker = []
name = []
PE_Ratio = []
mCap = []


seperator = 0
url = requests.get('https://www.slickcharts.com/sp500')
info = BeautifulSoup(url.text,'html.parser')
for x in info.findAll('tr'):
    for y in x('td'):
        for z in y.findAll('a'):
            if seperator%2==0:
                name.append(z.get_text())
            else:
                ticker.append(z.get_text())
            seperator+=1
for TK in ticker:
    financesite = requests.get('https://finance.yahoo.com/quote/'+TK + '/key-statistics')
    financeinfo = BeautifulSoup(financesite.text, 'html.parser')
    mCap.append(financeinfo.find('td',{"class":"Fz(s) Fw(500) Ta(end) Pstart(10px) Miw(60px)"}).get_text())
print(ticker)
print(mCap)
