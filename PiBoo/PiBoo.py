import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
import subprocess

PIN_Relay=12
PIN_Switch=16


def button_callback(channel):
    print("Button was pushed! Turn the motor on")
    GPIO.output(PIN_Relay, GPIO.HIGH)
    time.sleep(2.0) # 1/6 minute on 2 rpm motor
    print("Turn the motor off")
    GPIO.output(PIN_Relay, GPIO.LOW)
    #Play a random audio clip
    subprocess.call(["omxplayer", "Audio/thriller-end-laugh_UmpZxje.mp3"])
    
    
    
    

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering


GPIO.setup(PIN_Relay,GPIO.OUT)
GPIO.output(PIN_Relay, GPIO.LOW)


GPIO.setup(PIN_Switch, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Set pin to be an input pin and set initial valu$
GPIO.add_event_detect(PIN_Switch,GPIO.FALLING,callback=button_callback,bouncetime=5000) # Setup event on pin 10 rising edge


try:
    while True:
        pass
        #time.sleep(0.2)
finally:
    GPIO.output(PIN_Relay, GPIO.LOW)
    GPIO.cleanup()

#message = input("Enter 0 to set LOW, 1 to set HI, q to quit \n") # Run until someone presses enter
#if message ==0:
        #GPIO.output(PIN_Relay, GPIO.LOW)        
#elif message ==1:
        #GPIO.output(PIN_Relay, GPIO.HIGH)
#elif message =='q':
        #GPIO.cleanup() # Clean up

