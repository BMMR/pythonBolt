# Load the Excel file
import pandas as pd

def read_excel():

    df = pd.read_excel('external_info/data_orders.xlsx')

    for index, row in df.iterrows():
        # Extract the values from the current row and store them in variables
        Last_read = row['id_scooter']


    # Print the contents of the Excel file
    return Last_read


def delect_last_row():
    # Read the Excel file into a DataFrame
    df = pd.read_excel('external_info/data_orders.xlsx')

    # Delete the last row
    df = df[:-1]

    # Save the DataFrame to the Excel file
    df.to_excel('external_info/data_orders.xlsx', index=False)

