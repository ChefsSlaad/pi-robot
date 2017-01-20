import gpiozero
from time import sleep

# maak een variabele ‘sensor’, die gekoppeld wordt aan de ‘Distance’ (afstand) sensor
# met de aansluitingen ECHO op GPIO18 en TRIGGER of GPIO17

sensor = gpiozero.DistanceSensor(echo=18,trigger=17)

# while betekent: “zolang”
# true betekent: ‘waar’

while True:
    # maak een variabele ...
    # ‘round’ betekent ‘afronden’
    afstand = round(sensor.distance*100)
    
    # deze ken je wel nu toch?
    print('Obstakel op', afstand, 'cm')