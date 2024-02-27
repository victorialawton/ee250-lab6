import sys
sys.path.append('~/Dexter/GrovePi/Software/Python')
import time
import grovepi
from grove_rgb_lcd import *

# Grove Ultrasonic Ranger connectd to digital port 2
ultrasonic_ranger = 2
# potentiometer connected to analog port A0 as input
potentiometer = 0
grovepi.pinMode(potentiometer,"INPUT")

# clear lcd screen  before starting main loop
setText("")

while True:
  try:
# Read distance value from Ultrasonic Ranger
    distance = grovepi.ultrasonicRead(ultrasonic_ranger)
    
    # Read threshold from potentiometer
    # The potentiometer value will be directly used as the threshold
    threshold = grovepi.analogRead(potentiometer)
    
    # Format LCD text according to threshold
    # Top line: Threshold value and optionally "OBJ PRES"
    # Bottom line: Current ultrasonic ranger output
    if distance < threshold:
        # Object is within threshold distance
        setText_norefresh(f"{threshold} OBJ PRES\n{distance}")
    else:
        # No object detected within threshold distance
        setText_norefresh(f"{threshold}\n{distance}")
        
    # Small delay to prevent overwhelming the GrovePi
    time.sleep(0.1)
  
    
  except IOError:
    print("Error")
