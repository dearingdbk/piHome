"""
 * File:     thermo.py
 * Author:   BD
 * Date:     2013/03/29
 * Version:  1.0
 *
 * Purpose:  Handles the operations of reading sensor data, time and local temperature and
 *           running those values through the fuzzball instance to calculate whether
 *           or not the heater should run.
 """
import subprocess
from datetime import datetime
import re
import fuzzball
import time
import threading
import signal, os
import model

# Handles the read of sensor data, time and outside temperature.
class Thermostat:
    def __init__(self, pin, f_name, active):
        # Add pins in to the pincushion and database to ensure they are not used 
        # arbitrarily for other devices.
        try:
            model.new_pin('heater', 'Office', pin, active)
        except:
            print "ALREADY THERE"
        try:
            model.new_pin('thermostat', 'Office', 4, active)
        except:
            print "ALREADY THERE" 
        self.pin = pin
        self.input = Input(f_name)

    # Return temperature from one wire device on pin 4
    def get_temp(self):
        self.input.open_file()
        self.input.read_file()
        self.input.close_file()
        self.data = self.input.get_data().split()[-1]
        self.ret_val = float(self.data[2:])
        self.ret_val = self.ret_val / 1000
        return self.ret_val

    # return local time.
    def get_time(self):
        self.time = datetime.now()
        return self.time.hour
        
    # return local outside temperature as received from wether Canada
    def get_outside(self):
        self.trial = subprocess.Popen(
            "curl -s http://www.weatheroffice.gc.ca/city/pages/ns-35_metric_e.html | grep temperature ", stdout=subprocess.PIPE, shell=True).stdout.read()
        return re.sub('[a-z><"=  \n]', '', self.trial)

    # Request model.py to turn on the heater pin number 17. 
    def turn_on(self):
        model.turn_on(self.pin)        

    # Request model.py to turn off the heater pin number 17.
    def turn_off(self):
        model.turn_off(self.pin)       

# Handles the reading of the 1-wire sensor treating it as a file and using a regular 
# expression to strip out the required data.
class Input:
    def __init__(self, f_name):
        self.f_name = f_name

    # Set the file (sensor) to open
    def setfile(self, f_name):
        self.f_name = f_name

    # open the file (sensor)
    def open_file(self):
        try:
            self.tfile = open(self.f_name)
        except IOError:
            print ("Unable to Open File " + self.f_name)
            
    # read the file (sensor) into a local string
    def read_file(self):
        try:
            self.temp_data = self.tfile.read()
        except IOError:
            print ("Unable to Read File " + self.f_name)
            
    # close the file (sensor) now that we are done reading
    def close_file(self):
        self.tfile.close()

    # return the string representaation of the file (sensor). 
    def get_data(self):
        return self.temp_data


# Thread for handling the managing of Thermostat and fuzzball to read input variables
# and output appropriate responce to heater pin.
class ThermoThread(threading.Thread):
    
    def run(self):
        x = Thermostat(17, "/sys/bus/w1/devices/28-00000354a500/w1_slave", "LOW")
        f = fuzzball.FuzzyTemp("lib/therm.fcl")
        while True:
            if f.calc_val(x.get_temp(), x.get_time(), x.get_outside()):
                x.turn_on()
            else:
                x.turn_off()
                time.sleep(60 * 5)
