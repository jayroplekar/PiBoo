
import time
import subprocess
import os
import random
import signal
from signal import pause

from gpiozero import Button
from gpiozero import DigitalOutputDevice




PIN_Relay=12
PIN_Switch=16

button=Button("BOARD16")
relay=DigitalOutputDevice("BOARD12")   
DIR = '/home/pi/Audio' # Directory where various audio files are
files = [os.path.join(DIR, f) for f in os.listdir(DIR)]


def button_callback():
    #kill any player process that might block button response
    subprocess.call(["killall", "omxplayer"])  
    #Play a random audio clip
    audiofile=random.sample(files,1)[0]
    AudioProcess=subprocess.Popen(["omxplayer", audiofile])
    
    print("Button was pushed! Turn the motor on")
    
    relay.on()

    time.sleep(3.0)  # 3.75 seconds minute on 2 rpm motor is 45  deg
                     # 2.5 seconds on 3 rpm is 45 degrees
                     # found 3.0 with delay what centers the indexer

    print("Turn the motor off")
    relay.off()
        
def calibrate():
    print("Calibrating by 3 degrees")
    relay.on()
    time.sleep(0.2)  # 3.75 seconds minute on 2 rpm motor is 45  deg
                     # 2.5 seconds on 3 rpm is 45 degrees
                     # found 3.0 with delay what centers the indexer
    relay.off()



button.when_pressed=button_callback
signal.signal(signal.SIGUSR1, calibrate)

pause()
    


