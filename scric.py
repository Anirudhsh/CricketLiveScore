#Python program to scrape website 
#and save quotes from website 
import time
import requests 
from bs4 import BeautifulSoup
from twilio.rest import Client 
 
account_sid = 'ACfcde959cc7bbd5fcd91d6a8dc62bbb9f' 
auth_token = 'Enter token' 
client = Client(account_sid, auth_token) 
URL = "https://www.cricbuzz.com/cricket-match/live-scores"
r = requests.get(URL) 
soup = BeautifulSoup(r.content, 'html5lib') 

quotes=[] # a list to store comments
scoresent=""



#number list

print("enter numbers for score updates")

numbs = input().strip().split()

table = soup.find('div', attrs = {'id':'page-wrapper'}).find('div', attrs = {'class':'cb-bg-white cb-col-100 cb-col'}).find('div', attrs = {'class':'cb-col-67 cb-col cb-left cb-schdl'}).find('div', attrs = {'class':'cb-col cb-col-100 cb-lv-main'}) 



while True:
 currtable = soup.find('div', attrs = {'class':'cb-lv-scrs-col text-black'})
 targtable = soup.find('div', attrs = {'class':'cb-lv-scrs-col cb-text-live'})
 score=currtable.text
 
 #check curremt score 
 
 currscore = int(score[:-4])
 scoresent = 0
  if scoresent+10<=currscore:
    for i number in numbs:
        st = 'sms:'+ numbs
        message = client.messages.create(from_='whatsapp:+14155238886',body=currscore+"\n"+str(time.time()),to=st)
    scoresent=currscore

print(message.sid)    
#   .find('div', attrs = {'class':'cb-col-100 cb-col cb-schdl'}).find('div', attrs = {'class':'cb-col'})
