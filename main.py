import threading
import time

from server import *
from control_android import *
from image_read import *
from read_excel import *

# Funtions related to viewer software
def start_program():
    # code to be executed in thread 2
    print("Hello from start!")

    target = ['tag_enter_id.png', 'tag_write_id.png', 'tag_open_sc.png', 'tag_replace_batt.png', 'tag_return.png']
    # Create an empty array
    # Iterate through the list of names
    for row in target:
        # Append the ame to the array
        print("row:" + row)
        # Screenshot of screen
        screen_shot() # Take screen shot of the screen
        # Location of target
        original='image/screenshot.png'
        target='image/targets/tag_record.png'
        center_pointX, center_pointY=start_read_process(original, target)
        # Click on target
        click_touch(center_pointX,center_pointY)
        time.sleep(10)



######### Starting threads
def starting_threads():
    # create thread 1
    thread_1 = threading.Thread(target=start_server)
    # create thread 2
    thread_2 = threading.Thread(target=start_program)
    # start thread 1
    thread_1.start()
    # start thread 2
    thread_2.start()

################# Main Menu
if __name__ == '__main__':
    device = '19173cd4'  # Xiaomi phone

    variable=0
    if variable==1:
        #id_scooter=read_excel()
        #print(id_scooter)
        start_server()
        #time.sleep(4)
        #screen_shot()
        #connect(device)
        #click_touch("200","300")
        #end_server(device)
    else:
        print("Starting_threads")
        starting_threads()





