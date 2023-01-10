# Load the Excel file
import pandas as pd

def return_size_col(file_to_read,sheet_name,col_name):
    # Read the Excel file
    df = pd.read_excel(file_to_read, sheet_name=sheet_name)

    # Get the size of a specific column
    column_name = col_name
    size = df[column_name].size

    print("Size of column '" + column_name + "':", size)

    return size



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

