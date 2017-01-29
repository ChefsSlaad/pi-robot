import gpiozero
import time

# dit script test of de motors van de robots goed zijn aangesloten. 
# de wielen worden eerst 1-voor-1 getest, daarna samen


links_voor     = gpiozero.Motor(forward=13, backward=6)
rechts_voor    = gpiozero.Motor(forward=12, backward=16)
links_achter   = gpiozero.Motor(forward=26, backward=19)
rechts_achter  = gpiozero.Motor(forward=21, backward=20)

alle_motors = (links_voor, links_achter, rechts_voor, rechts_achter)
links = (links_voor, links_achter)
rechts = (rechts_voor, rechts_achter)
voor = (links_voor, rechts_voor)
achter = (links_achter, rechts_achter)



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


print(' versnellen')
for i in range(4):
    spd = i*0.2
    for m in alle_motors:
        m.forward(spd)
    time.sleep(1)
for m in alle_motors:
    m.stop()

print('linker_draai')
for m in links:
    m.forward()
time.sleep(1)
for m in alle_motors:
    m.stop()


print('rechter_draai')
for m in rechts:
    m.forward()
time.sleep(1)
for m in alle_motors:
    m.stop()


print('om de as')
for m in links:
    m.forward()
for m in rechts:
    m.backward()
time.sleep(1)
for m in alle_motors:
    m.stop()
