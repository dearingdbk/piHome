import subprocess
from datetime import datetime
import re
import fuzzball
import time
import threading
import signal, os
import model


class Thermostat:
    def __init__(self, pin, f_name, active):
        
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

    def get_temp(self):
        self.input.open_file()
        self.input.read_file()
        self.input.close_file()
        self.data = self.input.get_data().split()[-1]
        self.ret_val = float(self.data[2:])
        self.ret_val = self.ret_val / 1000
        return self.ret_val

    def get_time(self):
        self.time = datetime.now()
        return self.time.hour
        
    def get_outside(self):
        self.trial = subprocess.Popen(
            "curl -s http://www.weatheroffice.gc.ca/city/pages/ns-35_metric_e.html | grep temperature ", stdout=subprocess.PIPE, shell=True).stdout.read()
        return re.sub('[a-z><"=  \n]', '', self.trial)

    def turn_on(self):
        model.turn_on(self.pin)        


    def turn_off(self):
        model.turn_off(self.pin)       

        
class Input:
    def __init__(self, f_name):
        self.f_name = f_name

    def setfile(self, f_name):
        self.f_name = f_name

    def open_file(self):
        try:
            self.tfile = open(self.f_name)
        except IOError:
            print ("Unable to Open File " + self.f_name)
            
    def read_file(self):
        try:
            self.temp_data = self.tfile.read()
        except IOError:
            print ("Unable to Read File " + self.f_name)
    def close_file(self):
        self.tfile.close()

    def get_data(self):
        return self.temp_data



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
