from pyA20.gpio import gpio, port
import time

class Sensor():

    def __init__(self):

        self.TRIG = port.PA21 # change this if necessary
        self.ECHO = port.PC3 # change this if necessary
        
        gpio.init()

        gpio.setcfg(TRIG, gpio.OUTPUT)
        gpio.setcfg(ECHO, gpio.INPUT)
                
    def get_distance(self):

        gpio.output(TRIG, 0)

        time.sleep(0.2)
        gpio.output(TRIG, 1)
        time.sleep(0.00001)
        gpio.output(TRIG, 0)

        while gpio.input(ECHO) == 0:
            pulse_start = time.time()

        while gpio.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        return round(distance, 2)
