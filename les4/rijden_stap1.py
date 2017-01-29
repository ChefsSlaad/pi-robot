import time
from curses import wrapper

def main(scherm):
    scherm.clear()
    r = 0
    run = True
    while run:
        scherm.refresh()
        key = scherm.getkey()
        if key == 'KEY_UP':
            richting = 'vooruit'
        elif key == 'KEY_LEFT':
            richting = 'links'
        elif key == 'KEY_DOWN':
            richting = 'achteruit'
        elif key == 'KEY_RIGHT':
            richting = 'rechts'
        elif key =='q':
            run = False
        else:
            richting = 'stop'
        scherm.addstr(r,0, richting)
        time.sleep(0.01)
        r=r+1
        # als r >40 en het scherm is kleiner,dan een error
        if r > 20:  
            scherm.clear()
            r = 0

if __name__ == "__main__":
    wrapper(main)