import gpiozero
import time
from datetime import datetime

def now():
    return datetime.now().time()

class auto:
    def __init__(self):
        # auto bevat alle componenten van de auto/robot
        # de individuele wielen (links_voor, rechts_voor, etc)
        # de groepen wielen (links, rechts en alle)
        # en de snelheid (stadaard 100%)
                
        self.links_voor     = gpiozero.Motor(forward=6, backward=13)
        self.rechts_voor    = gpiozero.Motor(forward=12, backward=16)
        self.links_achter   = gpiozero.Motor(forward=19, backward=26)
        self.rechts_achter  = gpiozero.Motor(forward=20, backward=21)

        self.alle_motors = (self.links_voor, self.links_achter, self.rechts_voor, self.rechts_achter)
        self.links_motors = (self.links_voor, self.links_achter)
        self.rechts_motors = (self.rechts_voor, self.rechts_achter)
#        self.voor = (links_voor, rechts_voor)
#        self.achter = (links_achter, rechts_achter)
      
        self.vaart = 0
        

    def vooruit(self, duur = 0.5):
        print(now(), 'vooruit - snelheid', self.vaart, ';', duur, 'sec')
        for m in self.alle_motors:
            m.forward(self.vaart)
        time.sleep(duur)

    def stop(self):
        print(now(),'stop')
        for m in self.alle_motors:
            m.stop()

    def achteruit(self, duur = 0.5):
        print(now(), 'achteruit - snelheid', self.vaart, ';', duur, 'sec')
        for m in self.alle_motors:
            m.backward(self.vaart)
        time.sleep(duur)
 
    def links(self, duur = 0.5):
        print(now(), 'links - snelheid', self.vaart, ';', duur, 'sec')
        for m in self.links_motors:
            m.forward(self.vaart)
        time.sleep(duur)

    def rechts(self, duur = 0.5):
        print(now(), 'rechts - snelheid', self.vaart, ';', duur, 'sec')
        for m in self.rechts_motors:
            m.forward(self.vaart)
        time.sleep(duur)

    def rechts_as(self, duur = 0.5):
        print(now(), 'rechts om de as - snelheid', self.vaart, ';', duur, 'sec')
        for m in self.rechts_motors:
            m.forward(self.vaart)
        for m in self.links_motors:
            m.backward(self.vaart)
        time.sleep(duur)

    def links_as(self, duur = 0.5):
        print(now(), 'links om de as - snelheid', self.vaart, ';', duur, 'sec')
        for m in self.links_motors:
            m.forward(self.vaart)
        for m in self.rechts_motors:
            m.backward(self.vaart)
        time.sleep(duur)



if __name__ == "__main__":
    robot = auto()
    robot.vaart = 1

    while True:
        key = input('?')
        if key == 'w':
            robot.vooruit()
        elif key == 'a':
            robot.links_as()
        elif key == 's':
            robot.achteruit()
        elif key == 'd':
            robot.rechts_as()
        else:
            robot.stop()

        
import gpiozero
import time
from datetime import datetime


def now():
    return datetime.now().time()


class auto:

    def __init__(self):

        self.links_voor     = gpiozero.Motor(forward=6, backward=13)
        self.rechts_voor    = gpiozero.Motor(forward=12, backward=16)
        self.links_achter   = gpiozero.Motor(forward=19, backward=26)
        self.rechts_achter  = gpiozero.Motor(forward=20, backward=21)

        self.alle_motors = (self.links_voor, self.links_achter, self.rechts_voor, self.rechts_achter)
        self.links_motors = (self.links_voor, self.links_achter)
        self.rechts_motors = (self.rechts_voor, self.rechts_achter)
#        self.voor = (links_voor, rechts_voor)
#        self.achter = (links_achter, rechts_achter)
      
        self.vaart = 0
        

    def vooruit(self, duur = 0.5):
        print(now(), 'vooruit - snelheid', self.vaart, ';', duur, 'sec')
        for m in self.alle_motors:
            m.forward(self.vaart)
        time.sleep(duur)

    def stop(self):
        print(now(),'stop')
        for m in self.alle_motors:
            m.stop()

    def achteruit(self, duur = 0.5):
        print(now(), 'achteruit - snelheid', self.vaart, ';', duur, 'sec')
        for m in self.alle_motors:
            m.backward(self.vaart)
        time.sleep(duur)
 
    def links(self, duur = 0.5):
        print(now(), 'links - snelheid', self.vaart, ';', duur, 'sec')
        for m in self.links_motors:
            m.forward(self.vaart)
        time.sleep(duur)

    def rechts(self, duur = 0.5):
        print(now(), 'rechts - snelheid', self.vaart, ';', duur, 'sec')
        for m in self.rechts_motors:
            m.forward(self.vaart)
        time.sleep(duur)

    def rechts_as(self, duur = 0.5):
        print(now(), 'rechts om de as - snelheid', self.vaart, ';', duur, 'sec')
        for m in self.rechts_motors:
            m.forward(self.vaart)
        for m in self.links_motors:
            m.backward(self.vaart)
        time.sleep(duur)

    def links_as(self, duur = 0.5):
        print(now(), 'links om de as - snelheid', self.vaart, ';', duur, 'sec')
        for m in self.links_motors:
            m.forward(self.vaart)
        for m in self.rechts_motors:
            m.backward(self.vaart)
        time.sleep(duur)



if __name__ == "__main__":
    print('bestuur d auto met 'w = vooruit, a = links, s = achteruit, d = rechts')  
    robot = auto()
    robot.vaart = 1

    while True:
        key = input('?')
        if key == 'w':
            robot.vooruit()
        elif key == 'a':
            robot.links_as()
        elif key == 's':
            robot.achteruit()
        elif key == 'd':
            robot.rechts_as()
        else:
            robot.stop()

        
