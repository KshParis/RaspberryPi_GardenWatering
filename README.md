# RaspberryPi_GardenWatering
Python code base for interfacing raspberry pi with water pump to schedule watering at regular intervals Or based on moisture readings from the pot.

There are numerous other version of code available out there doing watering automation, however I have also uploaded a script that will let you host a web page on your raspberry pi to control the motor/watering. (You'd need to install Flask library prior to running this script - "pip install flask".)

Components used:
  1. Raspberry Pi B+ (Raspbian os) + adapter to power the PI
  2. Relay switch (https://www.amazon.fr/Kuman-Channel-Module-Arduino-Raspberry/dp/B01BAFLMCI/ref=sr_1_1?ie=UTF8&qid=1535539731&sr=8-1&keywords=4+channel+relay+switch)
  3. Water pump (https://www.amazon.fr/Gikfun-R385-Aquarium-refroidissement-diaphragme-Ek1856/dp/B0744FWNFR/ref=sr_1_fkmr0_1?ie=UTF8&qid=1535539868&sr=8-1-fkmr0&keywords=xcluma+R385)
  4. 12 V adapter for the waterpump.
  5. Moisture sensor. (https://www.amazon.fr/d%C3%A9tection-lhumidit%C3%A9-Hygrom%C3%A8tre-Capteur-dhumidit%C3%A9/dp/B00V35SYQI/ref=sr_1_5?s=computers&ie=UTF8&qid=1535540275&sr=1-5&keywords=moisture+sensor)
  5. Ribbon cables.

The assembly of the whole setup if fairly simple. The GPIO pins that needs to be used are available in the code base. In case you have questions feel free to comment.
