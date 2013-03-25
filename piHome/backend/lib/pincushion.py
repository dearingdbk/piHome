import control
# HOLDER CLASS #
class Cushion:
    def __init__(self):
        self.pin_dict = dict()
        

    def add_pin(self, pin, active):
        if '_' + str(pin) not in self.pin_dict:
            self.pin_dict['_' + str(pin)] = control.Raspi(pin, active)

    def get_val(self, pin):
        return self.pin_dict['_' + str(pin)]

    def del_pin(self, pin):
        if '_' + str(pin) in self.pin_dict:
            del self.pin_dict['_' + str(pin)]

def main():
    x = Cushion()
    x.add_pin(23, "LOW")
    x.add_pin(24, "HIGH")
    x.get_val(23).turn_on()
    print x.get_val(23).get_val()
    x.get_val(23).turn_off()
    print x.get_val(23).get_val()
    print x.pin_dict
    x.del_pin(23)
    print x.pin_dict

if __name__ == '__main__':main()
