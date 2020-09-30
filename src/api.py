from bs4 import BeautifulSoup
import requests
import pytest

r_st = requests.get('https://sg.finance.yahoo.com/quote/%5ESTI?p=^STI')
r_aapl = requests.get('https://sg.finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch')
r_gold = requests.get('https://sg.finance.yahoo.com/quote/GC=F?p=GC=F')

soup_st = BeautifulSoup(r_st.text, features='lxml')
match_st_name = soup_st.find('h1', class_='D(ib)')
match_st_price = soup_st.find('span', attrs={"data-reactid": "32"})

print(match_st_name.text, match_st_price.text)

soup_aapl = BeautifulSoup(r_aapl.text, features='lxml')
match_aapl_name = soup_aapl.find('h1', class_='D(ib)')
match_aapl_price = soup_aapl.find('span', attrs={"data-reactid": "32"})

print(match_aapl_name.text, match_aapl_price.text)

soup_gold = BeautifulSoup(r_gold.text, features='lxml')
match_gold_name = soup_gold.find('h1', class_='D(ib)')
match_gold_price = soup_gold.find('span', attrs={"data-reactid": "32"})

print(match_gold_name.text, match_gold_price.text)

assert match_aapl_name.text == "Apple Inc. (AAPL)jj"