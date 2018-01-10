###GetTemp.py
#Gets call from run.py, prints current ambient temp
#    as provided by temp sensor.
#
#Copyright 2017 hackmypi.com
#
#Author: mwagner@hackmypi.com
from envirophat import weather  
import sys, os, datetime, time 
print( 9.0/5.0 * float(weather.temperature()) + 32 -10)
