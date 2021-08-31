from time import sleep
from random import randint
import board
from math import floor
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn

battery = AnalogIn(board.A2)

led = DigitalInOut(board.GP15)
led.direction = Direction.OUTPUT

filename = "log/" + str(randint(0, 999999999))

def get_voltage(pin):
    return (pin.value * 3.3) / 65536

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return floor(n*multiplier + 0.5) / multiplier

def mean(values):
    total = sum(values)
    return total / len(values)

def get_average_voltage(pin, iterations=29, sample_rate=1):
    voltages = []

    for _ in range(1, iterations):
        led.value = True
        voltages.append(get_voltage(pin))
        sleep(sample_rate / 4)
        led.value = False
        sleep(sample_rate - sample_rate / 4)
        
    
    return round_half_up(mean(voltages), 3)

while True:
    voltage = get_average_voltage(battery)
    led.value = True
    print(voltage)
    log = open(filename, "a")
    log.write('{0:f}\n'.format(voltage))
    log.flush()
    log.close()
    sleep(1)
    led.value = False