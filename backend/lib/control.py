# Base class for a controller object #

class Controller(object):
    def turn_on(self):
        raise NotImplementedError
    def turn_off(self):
        raise NotImplementedError


# Raspberry Pi Controller Class. This can be extended 
# to other controller devices such as Rs232 and USB at a later date

class Raspi(Controller):
    
    # Initialize the class with a GPIO object
    # The pin that controls the furnace or AC
    # and wheteher the device is active High or Active Low
    def __init__(self, GPIO, pin, active):
        self.GPIO = GPIO
        self.pin = pin
        self.active = active
        self.GPIO.setup(self.pin, self.GPIO.OUT)
        if self.active == "LOW":
            self.GPIO.output(self.pin, self.GPIO.HIGH)
    
    # Turn on the Pin that is being controlled
    def turn_on(self):
        if self.active == "LOW":
            self.GPIO.output(self.pin, self.GPIO.LOW)
        else:
            self.GPIO.output(self.pin, self.GPIO.HIGH)
            

    # Turn off the pin that is being controlled
    def turn_off(self):
        if self.active == "LOW":
            self.GPIO.output(self.pin, self.GPIO.HIGH)
        else:
            self.GPIO.output(self.pin, self.GPIO.LOW)
