import gpiozero
from time import sleep

# maak een variabele ‘sensor’, die gekoppeld wordt aan de ‘Distance’ (afstand) sensor
# met de aansluitingen ECHO op GPIO18 en TRIGGER of GPIO17

sensor = gpiozero.DistanceSensor(echo=18,trigger=17)

# maak een variabele …… , die gekoppeld  wordt aan de ………….
# met de aansluitingen op GPIO…….

led = gpiozero.LED(22)

# while betekent: “zolang”
# true betekent: ‘waar’

while True:
    # maak een variabele ‘…….’
    # ‘round’ betekent ‘afronden’
    afstand = round(sensor.distance*100)
    
    print('Obstakel op', afstand, 'cm')

    # 'if' betekent als
    # 'in_range'
    if sensor.in_range:
        led.on()
    sleep(1)
    led.off()
