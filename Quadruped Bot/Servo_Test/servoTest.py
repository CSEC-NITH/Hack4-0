from gpiozero import AngularServo
from time import sleep
import math


servo11 = AngularServo(17,min_angle = -90,max_angle = 90)
servo12 = AngularServo(27,min_angle = -90,max_angle = 90)
servo13 = AngularServo(22,min_angle = -90,max_angle = 90)

servo21 = AngularServo(14,min_angle = -90,max_angle = 90)
servo22 = AngularServo(15,min_angle = -90,max_angle = 90)
servo23 = AngularServo(18,min_angle = -90,max_angle = 90)

servo31 = AngularServo(8,min_angle = -90,max_angle = 90)
servo32 = AngularServo(7,min_angle = -90,max_angle = 90)
servo33 = AngularServo(1,min_angle = -90,max_angle = 90)

servo41 = AngularServo(0,min_angle = -90,max_angle = 90)
servo42 = AngularServo(5,min_angle = -90,max_angle = 90)
servo43 = AngularServo(6,min_angle = -90,max_angle = 90)


servo11.max()
servo12.max()
servo13.max()
sleep(1)
servo11.mid()
servo12.mid()
servo13.mid()
sleep(1)
servo11.min()
servo12.min()
servo13.min()
sleep(1)

servo21.max()
servo22.max()
servo23.max()
sleep(1)
servo21.mid()
servo22.mid()
servo23.mid()
sleep(1)
servo21.min()
servo22.min()
servo23.min()
sleep(1)


servo31.max()
servo32.max()
servo33.max()
sleep(1)
servo31.mid()
servo32.mid()
servo33.mid()
sleep(1)
servo31.min()
servo32.min()
servo33.min()
sleep(1)

servo41.max()
servo42.max()
servo43.max()
sleep(1)
servo41.mid()
servo42.mid()
servo43.mid()
sleep(1)
servo41.min()
servo42.min()
servo43.min()
sleep(1)


print("Hi")
