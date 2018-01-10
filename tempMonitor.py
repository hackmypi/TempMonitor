###TempMonitor.py
#Gets call input of cell number and temp from run.py. Monitors ambient temp, if temp exceeds temp from sys.argv, notfies the cell number of unsafe temp.
#
#Copyright 2017 hackmypi.com
#
#Author: mwagner@hackmypi.com
from envirophat import weather 
from twilio.rest import Client 
import sys, os, datetime, time 

fromNumber = 'your from number'
account_sid = 'twilio account'
auth_token = 'twilio token'


client = Client(account_sid , auth_token) 
toNumber = sys.argv[1] 
debugTimer = 0 
maxTemp = float(sys.argv[2]) 
currentTemp = 9.0/5.0 * float(weather.temperature()) + 32 -10
hour = 0 
client.api.account.messages.create(to = toNumber , from_ = fromNumber , body = 'Monitoring temperature up to ' + str(maxTemp))
while (True):
    if(currentTemp > maxTemp):
        print str(currentTemp) + ' is more than ' + str(maxTemp)
        break
    print str(currentTemp) + ' is less than ' + str(maxTemp) + ' safe range counter= '+str(hour)
    currentTemp = 9.0/5.0 * float(weather.temperature()) + 32 -10
    if(hour == 60):
        client.api.account.messages.create(t0 = toNumber , from_ = fromNumber , body = 'Hourly update temp: ' + str(currentTemp)[0:5])
        hour = 0
    time.sleep(60)
    hour += 1 
client.api.account.messages.create(to = toNumber , from_ = fromNumber , body = "Warning: Temperature is now: " + str(currentTemp)[0:5])
