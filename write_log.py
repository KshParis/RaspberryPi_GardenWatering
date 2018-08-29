import datetime
import os.path
'''
# Log generator
    Takes 1 parameter - Comment/action description (text) and write it to "watering.log" with a timestamp automatically attached to it.
'''
log_name = "watering.log"

def log_me(action):

    if os.path.isfile(log_name):
        mode = "a"
    else:
        mode = "w"

    try:
        f = open(log_name, mode)
        act_time = datetime.datetime.now().strftime('%d-%m-%y %H:%M')
        f = open(log_name, mode)
        
        len_action = len(action)
        len_time = len(str(act_time))
        tot_len = len_action + len_time
       
        f.write(str(act_time) + ' : ' +  action  + '\n')
        f.close()
        
    except Exception as error:
        print(error)
        print("Error writing log to file")
