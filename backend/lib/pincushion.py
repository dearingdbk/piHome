import control

class Cushion:
    def __init__(self):
        self.pin_dict = dict()
        

    def add_pin(self, pin, active):
        if '_' + str(pin) not in self.pin_dict:
            self.pin_dict['_' + str(pin)] = control.Raspi(int(pin), active)

    def get_val(self, pin):
        return self.pin_dict['_' + str(pin)]

    def del_pin(self, pin):
        if '_' + str(pin) in self.pin_dict:
            del self.pin_dict['_' + str(pin)]
