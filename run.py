###run.py
#main receive function for Persephone and handles receiving texts and acting accordingly based on what is received
#based on the framework set forth by Twilio for receiving text messages
#
#Copyright 2017 hackmypi.com
#
#Author: mwagner@hackmypi.com

from flask import Flask, request, redirect 
from twilio.twiml.messaging_response import MessagingResponse 
import sys, os, datetime 
import subprocess 
from random import randint  
fromNumber = 'your_number_here' 

app = Flask(__name__) 
tempOffset = 8 
@app.route("/", methods=['GET', 'POST']) 

def hello_monkey():
    recFrom = request.values.get('From') #the number of the person who texted
    recBody = request.values.get('Body') #body of text received

	if ('-help' in recBody): #run helpdoc
        resp = MessagingResponse().message( 'Usage:\n -getAuth\n -getTime\n -getTemp\n -getAlarms \n -setTemp\n -setAlarm\n -auth\n -help\n -tweet')
        return str(resp)

    elif ('-getTemp' in recBody):#print the temp of where the Persephone Module is
        temp = float(os.popen('sudo python /scripts/persephone/temperature/getTemp.py').read())
        temp = str(temp)[0:5]
        resp = MessagingResponse().message(temp)
        return str(resp)

    elif ('-setTemp' in recBody):#Set temp monitoring, and notify if it exceeds a users input
        tempCom = recBody[9:]
        print tempCom
        os.system('sudo python /scripts/persephone/temperature/tempMonitor.py ' + recFrom + ' ' + tempCom + ' &')
        resp = MessagingResponse().message('Warning temp set to: ' + tempCom)
        return str(resp)

    else: #Unrecognized command error handling
        resp = MessagingResponse().message('Unrecognized Command, type -help for list of available commands')
        return str(resp) 

if __name__ == "__main__":
    app.run(debug=True)
