# Load the Excel file
import pandas as pd

def read_excel():

    df = pd.read_excel('external_info/data_orders.xlsx')

    for index, row in df.iterrows():
        # Extract the values from the current row and store them in variables
        value1 = row['id_scooter']

    # Print the contents of the Excel file
    return value1
