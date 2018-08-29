import RPi.GPIO as GPIO
from write_log import log_me
from time import sleep
import datetime
import sys

# Takes 1 input paramebter : The GPIO Pin number to which the device (motor, led, etc..) sends signal for intitialization
# once initialized/powered on, the signal is maintained for 10 seconds - this can be adjusted to your needs.
def run_gpio(pin):
    try:
        # The script as below using BCM GPIO 00..nn numbers
        GPIO.setmode(GPIO.BCM)
    
        # Set relay pins as output
        GPIO.setup(pin, GPIO.OUT)
            
        # Turn all relays ON
        GPIO.output(pin, GPIO.HIGH)

        f = open("water_time", "w")
        v_time = datetime.datetime.now().strftime('%d-%b-%y %H:%M')
        f.write(v_time)
        f.close()        

        GPIO.output(pin, GPIO.LOW)
        
        # Sleep for 10 seconds
        sleep(10)
    
        GPIO.cleanup()
        print("GPIO Cleaned up")
        
    except Exception as error:
        log_me(error)
        
def main(pin):
    run_gpio(int(pin))

if __name__ == "__main__":
    main(sys.argv[1]) 
