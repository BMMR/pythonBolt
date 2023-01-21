#################################################
# Software made by : Bruno Rocha, in 12-2022!
# Version 1
# Obejtive: Send ordens to Bolt Charger in order to send several comands at same time
# ------> Click_made <------- means ation was taken
#################################################
import io
import json
import threading
import time
from googleapiclient.http import MediaIoBaseDownload
from server import *
from control_android import *
from image_read import *
from read_excel import *


# Funtions related to viewer software
def start_program(select_mode,thresold,fast_speed,slow_speed,file_to_read,sheet_name,col_name):
    # Selected mode of working
    target_exec=selected_modes_of_working(select_mode) # Return all targets
    # Test read excel
    colls = read_return_all_cells(file_to_read, col_name) # Return all scooter tags

    while (True): # Main loop, in order to keep the readings of cells

        for col in colls:
            for select_target in target_exec: # Following rules
                set_speed=selected_speed_read_image(select_target, fast_speed, slow_speed)
                # Screenshot of screen
                screen_shot(set_speed) # Take screen shot of the screen
                # Start read process
                center_pointX, center_pointY=start_read_process('image/screenshot.png', select_target,thresold)
                # Click on target
                if center_pointX!="0" and center_pointY!="0":
                    click_touch(center_pointX,center_pointY)
                    print("------> Click_made <-------")

                # Only delect file when the ID was writed
                if select_target=="image/targets/tag_enter_id.png" or select_target=="image/targets/tag_enter_id_deploy.png":
                    # Selected col to insert text
                    col = col.replace("-", "")
                    col="851640"
                    print("QR SELECTED --->" + col + "<----")
                    insert_text(col) # insert text

                else:
                    print("current target:" + select_target)


def starting_threads(server,select_mode,thresold,fast_speed,slow_speed,file_to_read,sheet_name,col_name):

    if server:
        # create thread 1
        thread_1 = threading.Thread(target=start_web_server())

    # create thread 2
    thread_2 = threading.Thread(target=start_program(select_mode,thresold,fast_speed,slow_speed,file_to_read,sheet_name,col_name))

    if server:
        # start thread 1
        thread_1.start()
    # start thread 2
    thread_2.start()


# ----->  Main Menu <----- #
if __name__ == '__main__':

    ########### Initial configuration ###########
    # Selected device
    #device = '19173cd4'  # Xiaomi phone (Bruno device)
    #device = 'RFCCT10CRTL'  # SAMSUNG N6 (Bruno device)
    device = 'RZCT70FZATF'  # SAMSUNG N6 (Bruno device)

    # Phone cofiguration
    ativate_server = 0 # 1 to ativate the server to control the phone
    # Web server configuration (not used for now)
    server = False  # Start server ( not used for now)
    # Mode selection
    select_mode = 3 # 1 - Open battery 2 - Take battery and open scoote
    # Ajustments of selected speed
    fast_speed = 1 # More longer time, because of the conection
    slow_speed = 5 # General speed
    thresold = 0.97 # Ajusment for the image recognition
    # Selected reading files
    file_to_read = "external_info/escooter_orders.xlsx" # File source
    sheet_name="orders" # selected Sheet name
    col_name = "qr_to_command" # selected Column


    ###########################################
    if ativate_server==1:
        print("ativate_server")
        start_server()
    else:
        print("Starting_threads")
        starting_threads(server,select_mode,thresold,fast_speed,slow_speed,file_to_read,sheet_name,col_name)






