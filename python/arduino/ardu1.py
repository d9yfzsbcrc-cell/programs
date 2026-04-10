import pyfirmata
import time

board = pyfirmata.Arduino('/dev/cu.usbmodem2101')

#while True:
for i in range(1, 10):
    board.digital[13].write(1)
    time.sleep(0.5)
    board.digital[13].write(0)
    time.sleep(0.5)