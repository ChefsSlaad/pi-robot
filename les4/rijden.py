import gpiozero
import time
from datetime import datetime
from curses import wrapper


def now():
    return datetime.now().time().strftime('%H:%M:%S:%f')


class auto:
# auto heeft 4 motoren die we aan kunnen sturen. elke motor kan met 
# een vaste vaart voor- of achteruit. de wielen heten (voorspelbaar)
# links_voor, rechts_voor, links_achter en rechts_achter.
# verder heeft de auto de volgende methoden (dingen die hij kan doen)
# stop(), vooruit(), achteruit(), links() en rechts()
# links_as() en rechts_as() zorgen dat de auto linksom dan wel rechtsom 
# om zijn eigen as draait.

    def __init__(self):

        self.links_voor     = gpiozero.Motor(forward=6, backward=13)
        self.rechts_voor    = gpiozero.Motor(forward=12, backward=16)
        self.links_achter   = gpiozero.Motor(forward=19, backward=26)
        self.rechts_achter  = gpiozero.Motor(forward=20, backward=21)

        self.alle_motors = (self.links_voor, self.links_achter, self.rechts_voor, self.rechts_achter)
        self.links_motors = (self.links_voor, self.links_achter)
        self.rechts_motors = (self.rechts_voor, self.rechts_achter)
#        self.voor_motors = (links_voor, rechts_voor)
#        self.achter_motors = (links_achter, rechts_achter)
      
        self.vaart = 1
        

    def vooruit(self):
        for m in self.alle_motors:
            m.forward(self.vaart)

    def stop(self):
        for m in self.alle_motors:
            m.stop()

    def achteruit(self):
        for m in self.alle_motors: 
            m.backward(self.vaart)
 
    def links(self):
        # linker motors staan stil, rechter motors draaien
        for m in self._links_motors:
            m.stop()
        for m in self.rechts_motors: 
            m.forward(self.vaart)

    def rechts(self):
        for m in self.rechts_motorss:
            m.stop()
        for m in self.links_motors:
            m.forward(self.vaart)

    def rechts_as(self):
        for m in self.rechts_motors:
            m.forward(self.vaart)
        for m in self.links_motors:
            m.backward(self.vaart)

    def links_as(self):
        for m in self.links_motors:
            m.forward(self.vaart)
        for m in self.rechts_motors:
            m.backward(self.vaart)


def main(scherm):
    r = 0
    scherm.clear()
    run = True
    while run:
        scherm.refresh()
        key = scherm.getkey()
        if key == 'KEY_UP':
            robot.vooruit()
            richting = 'vooruit'
        elif key == 'KEY_LEFT':
            robot.links_as()
            richting = 'links'
        elif key == 'KEY_DOWN':
            robot.achteruit()
            richting = 'achteruit'
        elif key == 'KEY_RIGHT':
            robot.rechts_as()
            richting = 'rechts'
        elif key =='q':
            run = False
        else:
            robot.stop()
            richting = 'stop'
        scherm.addstr(r,0, now() + ' ' + richting)
        time.sleep(0.1)
        r=r+1
        if r > 40:
            r = 0
            scherm.clear()

if __name__ == "__main__":
    robot = auto()
    robot.vaart = 1
    wrapper(main)
