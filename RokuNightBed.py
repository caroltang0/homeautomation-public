import time
from roku import Roku

max_volume = 50
target_volume = 18

# Define volume setting function
def volume():
    for i in range(max_volume):
	    roku.volume_down()
    for i in range (target_volume):
        roku.volume_up()
# Define sleep_timer function to set sleep timer of 30 minutes
def sleep_timer():
    roku.info()
    time.sleep(.5)    
    roku.select()
    time.sleep(.5)     
    roku.down()
    time.sleep(.5) 
    roku.select()
    time.sleep(.5) 
    roku.left()

# Define picture_mode function to set low brightness picture mode
def picture_mode():
    roku.info()
    for i in range(2):
        roku.down()
        time.sleep(.5) 
        roku.select()
        time.sleep(.5) 
    for i in range(2):
        roku.up()
        time.sleep(.5) 
    roku.select()
    time.sleep(.5) 
    for i in range (2):
        roku.left()
        time.sleep(.5) 
        
# bedroom_ip = ''
roku = Roku(bed_ip)
volume()
time.sleep(1)
sleep_timer()
time.sleep(1)
picture_mode()