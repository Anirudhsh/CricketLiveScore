#Python program to scrape website 
import requests 
from bs4 import BeautifulSoup

URL = "https://www.cricbuzz.com/cricket-match/live-scores"
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html5lib') 

table = soup.find('div', attrs = {'id':'page-wrapper'}).find('div', attrs = {'class':'cb-bg-white cb-col-100 cb-col'}).find('div', attrs = {'class':'cb-col-67 cb-col cb-left cb-schdl'}).find('div', attrs = {'class':'cb-col cb-col-100 cb-lv-main'}) 
currtable = soup.find('div', attrs = {'class':'cb-lv-scrs-col text-black'})
targtable = soup.find('div', attrs = {'class':'cb-lv-scrs-col cb-text-live'})
score=currtable.text+"\n"+targtable.text
print(score)
    
#   .find('div', attrs = {'class':'cb-col-100 cb-col cb-schdl'}).find('div', attrs = {'class':'cb-col'})
