# Base class for a controller object #

class Controller(object):
    def turn_on(self):
        raise NotImplementedError
    def turn_off(self):
        raise NotImplementedError


# Raspberry Pi Controller Class. This can be extended 
# to other controller devices such as Rs232 and USB at a later date

class Raspi(Controller):
    try:
        import RPi.GPIO as GPIO
    except RuntimeError:
        print("Error importing RPi.GPIO")
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    # The pin that controls the furnace or AC
    # and wheteher the device is active High or Active Low
    def __init__(self, pin, active):
        self.pin = pin
        self.active = active
        self.GPIO.setup(self.pin, self.GPIO.OUT)
        if self.active == "low":
            self.GPIO.output(self.pin, self.GPIO.HIGH)
    
    # Turn on the Pin that is being controlled
    def turn_on(self):
        if self.active == "low":
            self.GPIO.output(self.pin, self.GPIO.LOW)
        else:
            self.GPIO.output(self.pin, self.GPIO.HIGH)
            

    # Turn off the pin that is being controlled
    def turn_off(self):
        if self.active == "low":
            self.GPIO.output(self.pin, self.GPIO.HIGH)
        else:
            self.GPIO.output(self.pin, self.GPIO.LOW)

    def savecounter():

        try:
            import RPi.GPIO as GPIO
            GPIO.cleanup()
        except RuntimeError:
            print("Error importing RPi.GPIO")

    import atexit
    atexit.register(savecounter)
