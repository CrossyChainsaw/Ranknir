import os
import requests
import time

# VARIABLES
_skywardClanID = "84648"
_lillyClanID = '864398'
_poopyBlenderClanID = '1923622'

# METHODS

def getClan():
  time.sleep(0.10) # 0.10 might be possible
  return requests.get("https://api.brawlhalla.com/clan/" + _poopyBlenderClanID +"/?api_key=" + os.environ['API_KEY'])

def getPlayerStats(brawlhalla_id):
  time.sleep(15)
  return requests.get("https://api.brawlhalla.com/player/" + 
str(brawlhalla_id) +"/ranked?api_key=" + os.environ['API_KEY'])

#test api
#https://api.brawlhalla.com/player/7364605/ranked?api_key=
#https://api.brawlhalla.com/clan/84648/?api_key=
