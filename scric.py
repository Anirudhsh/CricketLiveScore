#Python program to scrape website 
#and save quotes from website 
import requests 
from bs4 import BeautifulSoup
from twilio.rest import Client 
 
account_sid = 'ACfcde959cc7bbd5fcd91d6a8dc62bbb9f' 
auth_token = 'Enter token' 
client = Client(account_sid, auth_token) 
URL = "https://www.cricbuzz.com/cricket-match/live-scores"
r = requests.get(URL) 
soup = BeautifulSoup(r.content, 'html5lib') 

quotes=[] # a list to store quotes 

#table = soup.find('div', attrs = {'id':'page-wrapper'}).find('div', attrs = {'class':'cb-bg-white cb-col-100 cb-col'}).find('div', attrs = {'class':'cb-col-67 cb-col cb-left cb-schdl'}).find('div', attrs = {'class':'cb-col cb-col-100 cb-lv-main'}) 
currtable = soup.find('div', attrs = {'class':'cb-lv-scrs-col text-black'})
targtable = soup.find('div', attrs = {'class':'cb-lv-scrs-col cb-text-live'})
score=currtable.text+"\n"+targtable.text
#score="TonyMkl"
message = client.messages.create(from_='whatsapp:+14155238886',body=score,to='whatsapp:+919588250337') 
 
print(message.sid)    
#   .find('div', attrs = {'class':'cb-col-100 cb-col cb-schdl'}).find('div', attrs = {'class':'cb-col'})

