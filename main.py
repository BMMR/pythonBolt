# Software made by Bruno Rocha, in 12-2022!
# Version 1 (not tested in real world)

import threading
import time
from server import *
from control_android import *
from image_read import *
from read_excel import *

# Funtions related to viewer software
def start_program():
    # code to be executed in thread
    target = ['image/targets/tag_enter_id.png', 'image/targets/tag_write_id.png', 'image/targets/tag_open_sc.png', 'image/targets/tag_replace_batt.png', 'image/targets/tag_return.png']
    # Create an empty array

    # Iterate through the list of names
    for select_target in target:
        # Screenshot of screen
        screen_shot() # Take screen shot of the screen
        # Location of target
        original = 'image/screenshot.png'
        select_target = 'image/targets/tag_google_bar.png'
        print("row:" + select_target)

        center_pointX, center_pointY=start_read_process(original, select_target)
        # Click on target
        click_touch(center_pointX,center_pointY)
        time.sleep(1)
        # Only delect file when the ID was writed
        if select_target=="image/targets/tag_write_id.png":
            last_row_id=read_excel('external_info/Battery.xlsx')
            insert_text(last_row_id)
            delect_last_row('external_info/Battery.xlsx')
        else:
            print("current target:" + select_target)

        time.sleep(10)

######### Starting threads
def starting_threads(server):

    if server:
        # create thread 1
        thread_1 = threading.Thread(target=start_web_server())

    # create thread 2
    thread_2 = threading.Thread(target=start_program())

    if server:
        # start thread 1
        thread_1.start()

    # start thread 2
    thread_2.start()

################# Main Menu
if __name__ == '__main__':
    device = '19173cd4'  # Xiaomi phone
    variable=0
    server=False

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
        starting_threads(server)






