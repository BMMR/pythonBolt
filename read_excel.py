# Load the Excel file
import pandas as pd
import gdown
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def read_excel_from_drive():
    # login: boltscooterorders @ gmail.com
    # Pass: BoltScooterOrdersGmail
    # https://docs.google.com/spreadsheets/d/1P0iPFgKK4M_kiqTUgAHTa4X9NlGWmeZf5DKDPMvweI8/edit?usp=sharing

    url = "https://docs.google.com/spreadsheets/d/1P0iPFgKK4M_kiqTUgAHTa4X9NlGWmeZf5DKDPMvweI8/edit?usp=sharing"
    output = 'file.xlsx'
    gdown.download(url, output, quiet=False,fuzzy=True)



def return_excel_size_col(file_to_read,sheet_name,col_name):
    # Read the Excel file
    df = pd.read_excel(file_to_read, sheet_name=sheet_name)

    # Get the size of a specific column
    column_name = col_name
    size = df[column_name].size

    print("Size of column '" + column_name + "':", size)

    return size

def read_return_all_cells(file_path,column_name):
    # read the excel file into a pandas dataframe
    df = pd.read_excel(file_path)
    # get all cells in the specified column
    column_cells = df[column_name]
    return column_cells


def read_excel(file):

    df = pd.read_excel(file)
    for index, row in df.iterrows():
        # Extract the values from the current row and store them in variables
        Last_read = row['id_scooter']
    # Print the contents of the Excel file
    return Last_read



def delect_last_row(file):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file)

    # Delete the last row
    df = df[:-1]

    # Save the DataFrame to the Excel file
    df.to_excel(file, index=False)

