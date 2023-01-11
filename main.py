# Software made by Bruno Rocha, in 12-2022!
# Version 1 (not tested in real world)

import threading
import time
from server import *
from control_android import *
from image_read import *
from read_excel import *

# Funtions related to viewer software
def start_program(select_mode,thresold,speed_number,atual_speed):
    ###open SC###
    #1º Select, "tag_enter_id"; 2º Write, "tag_write_id"; 3º Select, "tag_open_sc"; 4º) Select, "tag_return";
    file_to_read="external_info/Battery.xlsx"
    sheet_name="Baterias"
    col_name="id_scooter"

    size_col=return_size_col(file_to_read, sheet_name, col_name)
    cont=0

    while(size_col>cont):
        cont=cont+1
        # code to be executed in thread
        if (select_mode==1):
            target_open_scooter = ['image/targets/tag_enter_id.png', 'image/targets/tag_open_sc.png', 'image/targets/tag_return.png']
            target_exec = target_open_scooter

        # 1º Select, "tag_enter_id": 2º Write, "tag_write_id": 3º Select, "tag_open_sc", 4º Select, "tag_3_dots"; 5º Select, "tag_replace_batt"; 6º) Select, "tag_return".
        if select_mode==2:
            target_open_batt_scooter = ['image/targets/tag_enter_id.png', 'image/targets/tag_open_sc.png','image/targets/tag_3_dots.png','image/targets/tag_replace_batt.png', 'image/targets/tag_return.png']
            target_exec = target_open_batt_scooter



        for select_target in target_exec: ## Following rules

            # Ajusting speed
            if select_target == "image/targets/tag_open_sc.png":  # process should be most slow
                set_speed = speed_number
            else:
                set_speed =atual_speed

            # Screenshot of screen
            screen_shot(set_speed) # Take screen shot of the screen
            # Location of target
            original = 'image/screenshot.png'
            # Start read process
            center_pointX, center_pointY=start_read_process(original, select_target,thresold)
            # Click on target
            if center_pointX!="0" and center_pointY!="0":
                print("click_made")
                click_touch(center_pointX,center_pointY)
                time.sleep(0.1)
            # Only delect file when the ID was writed
            if select_target=="image/targets/tag_enter_id.png":
                last_row_id=read_excel('external_info/Battery.xlsx')
                last_row_id = last_row_id.replace("-", "")
                last_row_id="851-640"
                print("SCOOOTER_ID_ATUAL->>>>"+last_row_id)

                #last_row_id="851640"
                insert_text(last_row_id) # insert text
                #delect_last_row('external_info/Battery.xlsx') # delect last row from file
            else:
                print("current target:" + select_target)


######### Starting threads
def starting_threads(server,select_mode,thresold,speed_number,atual_speed):

    if server:
        # create thread 1
        thread_1 = threading.Thread(target=start_web_server())

    # create thread 2
    thread_2 = threading.Thread(target=start_program(select_mode,thresold,speed_number,atual_speed))

    if server:
        # start thread 1
        thread_1.start()
    # start thread 2
    thread_2.start()

################# Main Menu
if __name__ == '__main__':
    #device = '19173cd4'  # Xiaomi phone (Bruno device)
    device = 'RFCCT10CRTL'  # SAMSUNG N6 (Bruno device)
    select_mode=2
    thresold=0.97

    speed_number=3
    atual_speed=0.4

    ativate_server=0
    server=False
    # Create system with order

    if ativate_server==1:
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
        starting_threads(server,select_mode,thresold,speed_number,atual_speed)






