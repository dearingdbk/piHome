import fuzzy.storage.fcl.Reader

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
