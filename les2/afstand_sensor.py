import gpiozero
from time import sleep

#test de afstand sensor

sensor = gpiozero.DistanceSensor(echo=18,trigger=17,max_distance=2, threshold_distance=0.5)
led = gpiozero.LED(22)

while True:
    afstand = round(sensor.distance*100)
    print('obstacle at', afstand, 'm')
    if sensor.in_range:
        led.on()
    sleep(1)
    led.off()

