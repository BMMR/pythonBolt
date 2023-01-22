#################################################
# Software made by : Bruno Rocha, in 12-2022!
# Version 1
# Obejtive: Send ordens to Bolt Charger in order to send several comands at same time
# ------> Click_made <------- means ation was taken
#################################################
from __future__ import print_function

import io
import json
import threading
import time
from googleapiclient.http import MediaIoBaseDownload
from server import *
from control_android import *
from image_read import *
from read_excel import *
from Google import *
#############################33

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



# Funtions related to viewer software
def start_program(select_mode,thresold,fast_speed,slow_speed,file_to_read,sheet_name,col_name):
    # Selected mode of working
    target_exec=selected_modes_of_working(select_mode) # Return all targets
    # Test read excel
    colls,index_cells = read_return_all_cells(file_to_read, col_name) # Return all scooter tags

    while (True): # Main loop, in order to keep the readings of cells
        index=0
        for col in colls:
            delect_last_row_val = True  # Delect last ROW By default

            for select_target in target_exec: # Following rules
                set_speed=selected_speed_read_image(select_target, fast_speed, slow_speed)
                # Screenshot of screen
                screen_shot(set_speed) # Take screen shot of the screen
                # Start read process
                center_pointX, center_pointY, max_val=start_read_process('image/screenshot.png', select_target,thresold)
                # Means that Found the dismiss warning and fail the deploy Means as well that dont need to delect the espefic Row
                if max_val>thresold and select_target=="image/targets/tag_dismiss_deploy.png":
                    delect_last_row_val= False # Fail, do not delect last row
                # Click on target
                if center_pointX!="0" and center_pointY!="0":
                    click_touch(center_pointX,center_pointY)
                    print("------> Click_made <-------")

                # Only delect file when the ID was writed
                if select_target=="image/targets/tag_enter_id.png" or select_target=="image/targets/tag_enter_id_deploy.png":
                    # Selected col to insert text
                    col = col.replace("-", "")
                    print("QR SELECTED --->" + col + "<----")
                    insert_text(col) # insert text
                else:
                    print("current target:" + select_target)

            if delect_last_row_val: # Delect the last row, means that deploy was sucess
                print(" DELETE QR --> " + str(col) + " with index --> " + str(index))
                delect_selected_row_in_file(file_to_read,index)

        index = index + 1 # Index to delete file



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


def test_drive_connection():

    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    # The ID and range of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1P0iPFgKK4M_kiqTUgAHTa4X9NlGWmeZf5DKDPMvweI8'
    SAMPLE_RANGE_NAME = 'orders'


    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials/client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))
    except HttpError as err:
        print(err)


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
    select_mode = 1 # 1 - Open Scooter 2 - Take battery and open scoote - 3 Make deploy 4 - Make safety Check
    # Ajustments of selected speed
    fast_speed = 1 # More longer time, because of the conection
    slow_speed = 5 # General speed
    thresold = 0.97 # Ajusment for the image recognition
    # Selected reading files
    file_to_read = "external_info/escooter_orders.xlsx" # File source
    sheet_name="orders" # selected Sheet name
    col_name = "qr_to_command" # selected Column
    ###########################################
    test_drive_connection()


    ###########################################
    if ativate_server==1:
        print("ativate_server")
        #start_server()
    else:
        print("Starting_threads")
        #starting_threads(server,select_mode,thresold,fast_speed,slow_speed,file_to_read,sheet_name,col_name)






