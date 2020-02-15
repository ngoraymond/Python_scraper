import requests
from bs4 import BeautifulSoup
import pandas

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
    try:
        print(TK+","+financeinfo.find('td',{"class":"Fz(s) Fw(500) Ta(end) Pstart(10px) Miw(60px)"}).get_text())
        mCap.append(financeinfo.find('td',{"class":"Fz(s) Fw(500) Ta(end) Pstart(10px) Miw(60px)"}).get_text())
    except:
        mCap.append("N/A")
    
df = pandas.DataFrame({'Name':name,'Ticker':ticker,'Market Cap':mCap}) 
df.to_excel("python scraper/stonks.xlsx")
