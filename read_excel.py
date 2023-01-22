# Load the Excel file
import pandas as pd


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
    index_cells=column_cells.index

    return column_cells,index_cells


def read_excel(file):

    df = pd.read_excel(file)
    for index, row in df.iterrows():
        # Extract the values from the current row and store them in variables
        Last_read = row['id_scooter']
    # Print the contents of the Excel file
    return Last_read


def delect_selected_row_in_file(file_path,row_index):
    print("delect_selected_row_in_file")
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path)
    # Delete the specified row
    df = df.drop(row_index)
    # Save the changes to the file
    df.to_excel(file_path, index=False)


def delect_last_row(file):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file)
    # Delete the last row
    df = df[:-1]
    # Save the DataFrame to the Excel file
    df.to_excel(file, index=False)

def create_file_with_incoming_information(file,data):
    print("----> File updated from google drive <------")
    #print("all data->>>>>>>>>>>"+ str(data))
    df = pd.DataFrame(data)
    # Save the DataFrame to an .xlsx file
    df.to_excel(file,index=False,header=False)

