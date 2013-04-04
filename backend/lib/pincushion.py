"""
 * File:     pincushion.py
 * Author:   BD
 * Date:     2013/03/29
 * Version:  1.0
 *
 * Purpose:  Contains a dictionary in which Raspi controller object pins 
 *           are added using there pin number with a _ in front as the 
 *           dictionary key. the Raspi control object can then be easily 
 *           returned by supplying a pin number.
"""
import control

# Class to hold all of the pins registered in use with the system.
class Cushion:
    # create instance of class Cushion
    def __init__(self):
        self.pin_dict = dict()
        
    # add a pin and Raspi controller object to the dictionary.
    def add_pin(self, pin, active):
        if '_' + str(pin) not in self.pin_dict:
            self.pin_dict['_' + str(pin)] = control.Raspi(int(pin), active)
            
    # return the identified Raspi control object.
    def get_val(self, pin):
        return self.pin_dict['_' + str(pin)]
        
    # del a pin from the dictionary when no longer required.
    def del_pin(self, pin):
        if '_' + str(pin) in self.pin_dict:
            del self.pin_dict['_' + str(pin)]
