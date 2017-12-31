#!/usr/bin/python3

import gpiozero
import time
from datetime import datetime
from curses import wrapper


def now():
    return datetime.now().time().strftime('%H:%M:%S:%f')


class robo_car:
# auto heeft 4 motoren die we aan kunnen sturen. elke motor kan met 
# een vaste speed voor- of achteruit. de wielen heten (voorspelbaar)
# left_front, right_front, left_back en right_back.
# verder heeft de auto de volgende methoden (dingen die hij kan doen)
# stop(), vooruit(), achteruit(), links() en rechts()
# links_as() en rechts_as() zorgen dat de auto linksom dan wel rechtsom 
# om zijn eigen as draait.

    def __init__(self):
        self.valid_go       = ('stop', 'forward', 'backward', 
                               'rotate_left', 'rotate_right', 
                               'forward_left', 'forward_right', 
                               'backward_left', 'backward_right')
                               
        self.left_front     = gpiozero.Motor(forward=6, backward=13)
        self.right_front    = gpiozero.Motor(forward=12, backward=16)
        self.left_back      = gpiozero.Motor(forward=19, backward=26)
        self.right_back     = gpiozero.Motor(forward=20, backward=21)

        self.all_motors = (self.left_front, self.left_back, self.right_front, self.right_back)
        self.left_motors = (self.left_front, self.left_back)
        self.right_motors = (self.right_front, self.right_back)
#        self.voor_motors = (left_front, right_front)
#        self.achter_motors = (left_back, right_back)

        self.command_list = []
        self.current_command = 'stop'
        self.speed = 1
        

    def go(self, direction):
        if direction not in self.valid_go:
            raise ValueError('{} is not a valid direction. accepted values are {}'.format(direction, self.valid_go)) 

        if direction == 'forward':
            self.forward()
        elif direction == 'backward':
            self.backward()
        elif direction == 'forward_left':
            self.left_forward()
        elif direction == 'forward_right':
            self.right_forward()
        elif direction == 'backward_left':
            self.left_backward()
        elif direction == 'backward_right':
            self.right_backward()
        elif direction == 'rotate_left':
            self.rotate_left()
        elif direction == 'rotate_right':
            self.rotate_right()
        else:
            self.stop()
            
    def run(self, ms = 500, scripted = False):
        while True:
            direction = 'stop'
            if len(self.command_list) > 0:
                if not scripted:
                    direction = self.command_list.pop():  #most recent item from the list
                    self.command_list = []                #empty list -> only listen for new commands 
                else:
                    direction = self.command_list.pop(0): #first item from the list
            if direction == 'stop':
                self.speed = 0
            else:
                print('going {} for {} ms'.format(direction, ms))
                self.speed = min( self.speed + 0.25, 1)
            
            self.go(direction)
            time.sleep(ms/1000)
        
    def forward(self):
        for m in self.all_motors:
            m.forward(self.speed)

    def stop(self):
        for m in self.all_motors:
            m.stop()

    def backward(self):
        for m in self.all_motors: 
            m.backward(self.speed)
 
    def left_forward(self):
        # linker motors staan stil, rechter motors draaien
        for m in self.left_motors:
            m.stop()
        for m in self.right_motors: 
            m.forward(self.speed)

    def right_forward(self):
        for m in self.right_motors:
            m.stop()
        for m in self.left_motors:
            m.forward(self.speed)

    def left_backward(self):
        # linker motors staan stil, rechter motors draaien
        for m in self.right_motors:
            m.stop()
        for m in self.left_motors: 
            m.backward(self.speed)

    def right_backward(self):
        for m in self.left_motors:
            m.stop()
        for m in self.right_motors:
            m.backward(self.speed)

    def rotate_right(self):
        for m in self.right_motors:
            m.forward(self.speed)
        for m in self.left_motors:
            m.backward(self.speed)

    def rotate_left(self):
        for m in self.left_motors:
            m.forward(self.speed)
        for m in self.right_motors:
            m.backward(self.speed)




def main(scherm):
    r = 0
    scherm.clear()
    run = True
    while run:
        scherm.refresh()
        key = scherm.getkey()
        if key == 'KEY_UP':
            robot.forward()
            richting = 'vooruit'
        elif key == 'KEY_LEFT':
            robot.rotate_left()
            richting = 'links'
        elif key == 'KEY_DOWN':
            robot.backward()
            richting = 'achteruit'
        elif key == 'KEY_RIGHT':
            robot.rotate_right()
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
    robot = robo_car()
    robot.speed = 1
    wrapper(main)
