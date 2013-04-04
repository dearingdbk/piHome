"""
 * File:     fuzzball.py
 * Author:   BD
 * Date:     2013/03/29
 * Version:  1.0
 *
 * Purpose:  Handles the Fuzzy Logic Controller portion of the intelligent agent
 *           Uses packages from pyFuzzy to read Fuzzy Control Language document therm.fcl.
"""
import fuzzy.storage.fcl.Reader

# Sets up a dictionary containing initial values for temp, time, and outside.
# contains a method calc_vals() to calculate a crisp output from our fuzzy input values.
# Based on rule blocks contained in therm.fcl.
class FuzzyTemp:
    def __init__(self, f_name):
        self.f_name = f_name
        self.fz = fuzzy.storage.fcl.Reader.Reader().load_from_file(self.f_name)
        # preallocate input and output values
        self.my_input = {"temp" : 0.0, "time" : 0.0, "outside" : 0.0}    
        self.my_output = {"heater" : 0.0}

    # set input values
    def calc_val(self, temp, time, outside):
        self.my_input["temp"] = temp
        self.my_input["time"] = time
        self.my_input["outside"] = outside        
        self.fz.calculate(self.my_input,self.my_output)
        return self.my_output["heater"]
