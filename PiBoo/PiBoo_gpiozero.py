#import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
import subprocess
from gpiozero import Button
from gpiozero import DigitalOutputDevice
from signal import pause
import os
import subprocess
import random

PIN_Relay=12
PIN_Switch=16

button=Button("BOARD16")
relay=DigitalOutputDevice("BOARD12")   
DIR = '/home/pi/Audio' # I 
files = [os.path.join(DIR, f) for f in os.listdir(DIR)]
AudioProcess=None

def button_callback():
    #if AudioProcess != None:
        #print("Killing previous audio AudioProcess")
        #subprocess.Popen.terminate(AudioProcess)
        #AudioProcess=None
    subprocess.call(["killall", "omxplayer"])  
    #Play a random audio clip
    audiofile=random.sample(files,1)[0]
    print("Chosen Randomfile:", audiofile)
    AudioProcess=subprocess.Popen(["omxplayer", audiofile])
    
    print("Button was pushed! Turn the motor on")
    relay.on()
    time.sleep(2.5) # 2.5 seconds minute on 2 rpm motor
    print("Turn the motor off")
    relay.off()
    
    
    
    
button.when_pressed=button_callback
pause()
    


