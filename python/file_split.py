# Pandas is an open source library that is used to analyze data in Python.
import pandas as pd

def file_split():
    # df = the csv file we want to read
    df = pd.read_csv('C:/Users/Garrett/Desktop/projectone slack files/Tables/output.csv')

    duplicates = [] # list for duplicate product names
    unique = []     # list for unique product names

    # productname_df = a dataframe containing tuples of each row in df (index, productname)
    productname_df = df[['productname']]

    # tuples containing (index, true/false) for each name in productname_df
    duplicate_names = productname_df.duplicated(keep=False).iteritems()

    # for each name and index in duplicate_names
    for index, name in enumerate(duplicate_names):
        
        is_duplicate = name[1] # index 1 of name tells us if its a duplicate (index, true/false)   
        
        csv_row = df.loc[index] # current csv row from original file

        # if the name is a duplicate
        if is_duplicate:        
            duplicates.append(csv_row) # add the product name to duplicates list

        else:        
            unique.append(csv_row) # add product name to unique list

    # default columns for the DataFrames
    default_columns = ['productname', 'category1', 'category2', 'category3', 'image1', 'image2', 'description', 'price']

    # DataFrame for duplicates
    duplicate_df = pd.DataFrame(
        duplicates, # the list we're using for data
        columns=default_columns # columns for DataFrame 
        )

    # DataFrame for unique product names
    unique_df = pd.DataFrame(
        unique, # the list we're using for data
        columns=default_columns # columns for DataFrame
        )

    # .reset_index(drop=True) ensures that the indexes start from 1 and continue sequential
    # indexes = 1,2,3,4,5 etc...
    return unique_df.reset_index(drop=True)

    # write DataFrames to individual csv files
    # duplicate_df.to_csv('duplicates.csv', mode='w', index=False)
    # unique_df.to_csv('unique.csv', mode='w', index=False)

file_split()