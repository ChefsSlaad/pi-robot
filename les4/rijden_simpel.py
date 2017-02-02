from time import sleep
import gpiozero

links_voor     = gpiozero.Motor(forward=13, backward=6)
rechts_voor    = gpiozero.Motor(forward=12, backward=16)
links_achter   = gpiozero.Motor(forward=26, backward=19)
rechts_achter  = gpiozero.Motor(forward=21, backward=20)

alle_motors = (links_voor, links_achter, rechts_voor, rechts_achter)
links = (links_voor, links_achter)
rechts = (rechts_voor, rechts_achter)

vaart = 1

doorgaan = True
while doorgaan: # hier zeggen we dus dat zolang de voorwaarde (doorgaan) waar is de loop herhaaldmoe blijven worden
    # met het commando input() wacht de pi totdat je iets hebt ingetypt en op enter hebt gedrukt.
    # je kunt input() aan een variabele toewijzen. Dat hebben we in les 2 ook gedaan met de 
    # afstand sensor. Bijvoorbeeld met invoer = input('typ iets en druk op enter')

    invoer = input('Tik een van de letters: w=start, s=stop, q=exit')
    
    if invoer == 'q':
        doorgaan = False # als je op q drukt dan wordt doorgaan onwaar en sluit de loop
    elif invoer == 'w':
        print('vooruit')
        for m in alle_motors:
            m.forward(vaart)
        sleep(0.5)
        for m in alle_motors:
            m.stop()
        print('rechts')
        for m in links:
            m.forward(vaart)
        sleep(0.2)
    elif invoer == 's':
        print('Stop auto')
        for m in alle_motors:
            m.stop()   
        sleep(0.2)
