import datetime
import time
import execute_gpio_pin
import RPi.GPIO as GPIO
from write_log import log_me

#mode = 'GPIO' # or 'SCH'
mode = 'SCH'
comments = {"GPIO": "Watering happens only when the moisture sensor senses no water", 
            "SCH" : "Watering happens at the scheduled interval in the program"}
anomalie_counter = 0

#Scheduled intervals for watering the plants.
intervals = ['06:00', '14:00',  '22:00']

file_name = "/home/pi/watering/touch.txt"

#GPIO PIN
pump_pin = 24
sensor_pin = 23

#Seconds for which the watering loop will wait to check if the current time == interval.
v_sleep = 10

#main program loop that checks for the intervals defined, to water the plants.
def run_watering_loop():
    try:
        while True:
            try:
               f = open(file_name, "r")
               log_me("Exiting program: Please remove the file touch.txt and retry the launch..")
               f.close()
               break
            except Exception:
               curr_time = str(datetime.datetime.now().strftime('%H:%M'))
               
               for interval in intervals:
                   if curr_time == interval:
                       execute_gpio_pin.main(pump_pin)
                       log_me("Pin configured: " + str(pump_pin))
                       log_me("watered at: " + str(datetime.datetime.now().strftime('%d-%m-%y %H:%M')))
            
            time.sleep (v_sleep)

    except Exception as error:
        log_me("ERR (schedul_watering.py) : " + str(error))
    
    finally:
        log_me("Program terminated..")
        
def CheckSensor():
    anomalie_counter = 0
    while True:
        try:
            f=open(file_name, 'r')
            log_me("Touch file found - exiting.." + str(datetime.datetime.now().strftime('%d-%m-%y %H:%M')))
            f.close()
            break
        except:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(sensor_pin, GPIO.IN)
            
            if anomalie_counter > 1:
                log_me("Sensor loop ran for more than 2 cycle.. breaking sensor reading loop to avoid water wastage")
                log_me("Please check sensor status")
                break
            
            if GPIO.input(sensor_pin):
                anomalie_counter = anomalie_counter + 1
                execute_gpio_pin.main(24)
                log_me("Sensor activated")
                log_me("Low water level detected, watering plants")  
            else:
                continue
     
        time.sleep(2)
        
def run_program():
    if mode == 'GPIO':
        CheckSensor()
    elif mode == 'SCH':
        run_watering_loop()

def main():
    try:
        log_me("Starting: schedule_watering.py")
        log_me("Mode : " + str(mode))
        log_me(comments[mode])
        run_program()
    finally:
        log_me("Stoping schedule_watering.py...")    
        
if __name__ == "__main__":
    main()
