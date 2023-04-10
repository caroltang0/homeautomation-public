import time
from roku import Roku

max_volume = 50
target_volume = 24
# Define volume setting function
def volume():
    for i in range(max_volume):
	    roku.volume_down()
    for i in range (target_volume):
        roku.volume_up()
# Define picture_mode function to set normal daytime picture mode
def picture_mode():
    roku.info()
    time.sleep(.5)
    for i in range(2):
        roku.down()
        time.sleep(.5) 
        roku.select()
        time.sleep(.5) 
    for i in range(2):
        roku.down()
        time.sleep(.5) 
    roku.select()
    time.sleep(.5) 
    for i in range (2):
        roku.left()
        time.sleep(.5) 
        
# bedroom_ip = ''
roku = Roku(living)
volume()
time.sleep(1)
picture_mode()