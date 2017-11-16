import RPi.GPIO as GPIO
import math
import time
from threading import Thread
GPIO.setmode(GPIO.BCM)
class ButtonInputManager(Thread):
    
    N1 = 24
    N2 = 25
    N3 = 4
    N4 = 14
    N5 = 15
    N6 = 18
    N7 = 17
    N8 = 27
    N9 = 22
    N10 = 23
    N11 = 10
    N12 = 9
    N13 = 11
    N14 = 8
    N15 = 7
    N16 = 5
    N = [N1, N2, N3, N4, N5, N6, N7, N8, N9, N10, N11, N12, N13, N14, N15, N16]
    
    def __init__(self):
        super().__init__()
        for n in ButtonInputManager.N:
            GPIO.setup(n ,GPIO.IN)
        self.queue = []
        self.start()
        
    def run(self):
        while True:
            state = self.getButtonStates()
            if state != 0:
                n = int(math.log(state, 2)) + 1
                self.add(n)
                time.sleep(0.4)

    def pop(self):
        return self.queue.pop(0)

    def add(self, number):
        self.queue.append(number)

    def getButtonStates(self):
        number = 0
        for n in range(len(ButtonInputManager.N)):
            number += (GPIO.input(ButtonInputManager.N[n]) * (2**n))
        return number
    
    def clear(self):
        self.queue = []

    def toString(self):
        return self.queue

class BreathInputManager:
    def __init__(self):
        GPIO.setup(6, GPIO.IN)
        while True:
            print(GPIO.input(6))

if __name__ == "__main__":
    """BIM = ButtonInputManager()
    while True:
        print(BIM.queue)
    """
    BreathInputManager()
    
