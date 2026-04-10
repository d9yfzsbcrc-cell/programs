# Source - https://stackoverflow.com/q
# Posted by Eeshan Mishra
# Retrieved 2026-01-09, License - CC BY-SA 4.0

from pyfirmata import ArduinoMega, SERVO, util, Arduino
from time import sleep

port = "/dev/cu.usbmodem2101"
joint_pin = 9
base_pin = 10
board = ArduinoMega(port)
board.digital[base_pin].mode=SERVO

def rotateServo(pin, angle):
    board.digital[pin].write(180)
    sleep(0.015)

def main():

    #for i in range(0, 90):
        #rotateServo(base_pin, i, board)
    # rotate joint servo
    for j in range(0, 90):
        rotateServo(base_pin, j)

if __name__ == '__main__':
    #board = pyfirmata.ArduinoMega('/dev/cu.usbmodem2101')
    print("Communication Successfully started")
    M1=board.digital[2]
    M1.mode=pyfirmata.PWM
    M2=board.digital[3]
    M2.mode=pyfirmata.PWM
    while True:
        M1.write(.1)
        M2.write(0)
        #time.sleep(.001)