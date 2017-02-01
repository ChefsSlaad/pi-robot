import gpiozero
import time

# dit script test of de motors van de robots goed zijn aangesloten. 
# de wielen worden eerst 1-voor-1 getest, daarna samen

# de eerste stap is python vertellen hoe de verschillende motors 'gevonden'
# kunnen worden. met andere woorden, op welke gpio pinnen ze aangesloten zijn. 
# we geven de motoren makkelijke namen zodat we ze terug kunnen vinden. Maar
# eigenlijk kun je elke naam gebruiken die je wil
links_voor     = gpiozero.Motor(forward=13, backward=6)
rechts_voor    = gpiozero.Motor(forward=12, backward=16)
links_achter   = gpiozero.Motor(forward=26, backward=19)
rechts_achter  = gpiozero.Motor(forward=21, backward=20)

# hier maken we handige groepjes van de motoren die we tegelijk kunnen 
# gebruiken. In dit geval zijn dat alle_motoren, links en rechts. We hadden
# ook nog andere setjes kunnen maken, zoals voor of achter
alle_motors = (links_voor, links_achter, rechts_voor, rechts_achter)
links = (links_voor, links_achter)
rechts = (rechts_voor, rechts_achter)

# hier testen we of de motors werken. python voert zo snel mogelijk 
# achter elkaar de opdrachten uit. als je dus wil dat de motors een tijdje
# doordraaien moeten we het programma vertellen dat het even moet wachten. 
# Hier doen we dat met het commando time.sleep(1) - Letterlijk - doe 1 seconde niets
# 
# vraag: waarom eindigt elk blok met <motor>.stop()?

print('links voor')
links_voor.forward()
time.sleep(1)
links_voor.backward()
time.sleep(1)
links_voor.stop()


print('rechts voor')
rechts_voor.forward()
time.sleep(1)
rechts_voor.backward()
time.sleep(1)
rechts_voor.stop()


print('links achter')
links_achter.forward()
time.sleep(1)
links_achter.backward()
time.sleep(1)
links_achter.stop()


print('rechts achter')
rechts_achter.forward()
time.sleep(1)
rechts_achter.backward()
time.sleep(1)
rechts_achter.stop()

  
# hier gebruiken we een setje van motors die we aan het begin van het 
# programma gemaakt hebben. 
# for m in rechts:  vertelt python dat elke motor in de set rechts 
# een bepaalde opdracht moet krijgen. In dit geval dus het commando forward.
# for m in rechts:
#    m.forward()
# 
# is hetzelfde als: 
# rechts_voor.forward()
# rechts_achter.forward()

print('linker_draai')
for m in rechts:
    m.forward()
time.sleep(1)
for m in alle_motors:
    m.stop()

# vraag: waarom zetten we de wielen rechts aan als we een linker draai willen maken? 

print('rechter_draai')
for m in links:
    m.forward()
time.sleep(1)
for m in alle_motors:
    m.stop()

    
# hier testen we het versnellen van de motor dat doen we door elke motor steeds
# een beetje sneller te laten draaien. Range(10) is eigenlijk een setje van 10 
# getallen dat bij 0 begint. dus hetzelfde als (0,1,2,3,4,5,6,7,8,9)
# we veranderen de snelheid steeds in stapje van 0.1 door dat te het getal in de 
# set te vermenigvuldigen met 0.1 en daarna de motors met die snelheid vooruit te 
# laten bewegen. 

print(' versnellen')
for i in range(10):
    vaart = i*0.1 
    for m in alle_motors:
        m.forward(vaart)
    time.sleep(0.2)
for m in alle_motors:
    m.stop()

# vraag: waarom draait de auto nu om zijn as?    
    
print('om de as - met de klok mee')
for m in links:
    m.forward()
for m in rechts:
    m.backward()
time.sleep(1)
for m in alle_motors:
    m.stop()
