from time import sleep


# we maken een loop (een stukje code dat zich blijft herhalen) zolang een bepaalde 
# voorwaarde waar (True) is. we kunnen die loop sluiten door de voorwaarde 
# onwaar (False) te maken.

doorgaan = True
while doorgaan: # hier zeggen we dus dat zolang de voorwaarde (doorgaan) waar is de loop herhaaldmoe blijven worden
    # met het commando input() wacht de pi totdat je iets hebt ingetypt en op enter hebt gedrukt.
    # je kunt input() aan een variabele toewijzen. Dat hebben we in les 2 ook gedaan met de 
    # afstand sensor. Bijvoorbeeld met invoer = input('typ iets en druk op enter')

    invoer = input('Tik een van de letters: w=voor, a=links, d=rechts, s=achter, q=exit')
    
    if invoer == 'q':
        doorgaan = False # als je op q drukt dan wordt doorgaan onwaar en sluit de loop
    elif invoer == 'w':
        print('vooruit')
        # welk commando zou je hier kunnen gebruiken om de auto vooruit te laten bewegen?
        # tip: kijk eens naar het programma dat we gebruikt hebben om te testen of de 
        # wielen het doen
    sleep(0.5)

    # hoe zorg je dat de auto weeer stopt?
    
