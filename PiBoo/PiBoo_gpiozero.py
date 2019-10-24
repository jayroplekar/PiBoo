
import time
import subprocess
import os
import random
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
    time.sleep(2.5) # 2.5 seconds minute on 2 rpm motor
    print("Turn the motor off")
    relay.off()
        
    
button.when_pressed=button_callback
pause()
    


