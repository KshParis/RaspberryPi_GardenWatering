'''
///// The program when run, renders a web page with a button that can be used to initializes the water pump, irrespective of the
///// watering time scheduled in the script.
'''
from flask import Flask, render_template, request, redirect, url_for
import datetime
import RPi.GPIO as GPIO
import SpeedTest as speedtest
import execute_gpio_pin
from file_read_backwards import FileReadBackwards
app = Flask(__name__, static_url_path='/')
import os

file_name = '/home/pi/speedtest/speed_test.log'

app = Flask(__name__)
     

@app.route("/", methods=["GET", "POST"])
def home_inded():
    v_time = datetime.datetime.now()
    
    f = open('water_time','r')
    last_watered = f.readlines()
    
    return render_template("index_v1.0.html", last_watered = last_watered, title='My automation')

@app.route("/WaterPlants", methods=["GET", "POST"])
def water_me():
    if request.method == "POST":
        mypin=24
        execute_gpio_pin.main(mypin)
        print("gpio call executed sucesfuly")
        
        return redirect(url_for("home_inded"))


if __name__ == "__main__":
    app.run(host="192.168.1.6", port=80, debug=True)
    #app.run(debug=True)
