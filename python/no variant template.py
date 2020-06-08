# Pandas is an open source library that is used to analyze data in Python.
import pandas as pd

from file_split import file_split
from clean_description import clean_description

# 2 lists containing the field names for input an outputs
output_fields = ['Product Name', 'Category','Product Image File - 1','Product Image File - 2','Product Description','Price']

input_fields = ['productname','category','image1','image2','description','price',]

# open file
input_csv = file_split()

# 1st column of 'No Variant Template.xlsx'
# name of each column for No Variant Template
fields = [
    'Item Type',
    'Product ID',
    'Product Name',
    'Product Type',
    'Product Code/SKU',
    'Bin Picking Number',
    'Brand Name',
    'Option Set',
    'Option Set Align',
    'Product Description',
    'Price',
    'Cost Price',
    'Retail Price',
    'Sale Price',
    'Fixed Shipping Cost',
    'Free Shipping',
    'Product Warranty',
    'Product Weight',
    'Product Width',
    'Product Height',
    'Product Depth',
    'Allow Purchases?',
    'Product Visible?',
    'Product Availability',
    'Track Inventory',
    'Current Stock Level',
    'Low Stock Level',
    'Category',
    'Product Image ID - 1',
    'Product Image File - 1',
    'Product Image Description - 1',
    'Product Image Is Thumbnail - 1',
    'Product Image Sort - 1',
    'Product Image ID - 2',
    'Product Image File - 2',
    'Product Image Description - 2',
    'Product Image Is Thumbnail - 2',
    'Product Image Sort - 2',
    'Product Image ID - 3',
    'Product Image File - 3',
    'Product Image Description - 3',
    'Product Image Is Thumbnail - 3',
    'Product Image Sort - 3',
    'Product Image ID - 4',
    'Product Image File - 4',
    'Product Image Description - 4',
    'Product Image Is Thumbnail - 4',
    'Product Image Sort - 4',
    'Product Image ID - 5',
    'Product Image File - 5',
    'Product Image Description - 5',
    'Product Image Is Thumbnail - 5',
    'Product Image Sort - 5',
    'Search Keywords',
    'Page Title',
    'Meta Keywords',
    'Meta Description',
    'Product Condition',
    'Show Product Condition?',
    'Sort Order',
    'Product Tax Class',
    'Product UPC/EAN',
    'Stop Processing Rules',
    'Product URL',
    'Redirect Old URL?',
    'GPS Global Trade Item Number',
    'GPS Manufacturer Part Number',
    'GPS Gender',
    'GPS Age Group',
    'GPS Color',
    'GPS Size',
    'GPS Material',
    'GPS Pattern',
    'GPS Item Group ID',
    'GPS Category',
    'GPS Enabled',
    'Tax Provider Tax Code',
    'Product Custom Fields'
]

# 3rd column of 'No Variant Template.xlsx'
# default values for No Variant Template
example = [
    'Product',
    '',
    '2PCS - HEART CHARM METAL LINK LAYERED ANKLETS',
    'P',
    '479533',
    '',
    'BIJOUX PIECES',
    '2PCS - HEART CHARM METAL LINK LAYERED ANKLETS',
    'Right',
    'Theme : Heart Size : 0.5"H, 7.5" + 3" L One Side Only Lead and Nickel Compliant',
    '6',
    '3',
    '0',
    '0',
    '0',
    'N',
    '',
    '0',
    '0',
    '0',
    '0',
    'Y',
    'Y',
    'Y',
    'by product',
    '50',
    '10',
    'JEWELRY;ANKLET/FASHION',
    '',
    'https://www.wonatrading.com/images/20200311/AK0071-@GD-XX@2P-05H-75_3L@479533@300@01.jpg',
    '',
    'Y',
    '0',
    '',
    'https://www.wonatrading.com/images/20200311/des_img/AK0071-@GD-XX@2P-05H-75_3L@479533@300@01@1.jpg',
    '',
    'N',
    '1',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    'New',
    'N',
    '0',
    'N',
    '',
    'N',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    'N',
    '',
    'Color=Gold'
]

# DataFrame for 'No Variant Template.xlsx'
template = pd.DataFrame(
    [example], # the list we're using for data
    columns=fields # columns for DataFrame 
    )

# the number of products or rows
number_of_rows = len(input_csv)

# this list will be used for the data of output_df
output_list = []

for row in range(number_of_rows): # for each row in dataframe
    """
    Compress Categories
    """
    # save each category to a variable
    category1 = input_csv['category1'].loc[row]
    category2 = input_csv['category2'].loc[row]
    category3 = input_csv['category3'].loc[row]

    # combine everything in a formated string
    Category = f"{category1};{category2}/{category3}"

    # for counter, value in enumerate(output_fields):
    for i, field in enumerate(output_fields):

        # if iterating over category, combine all 3 categories       
        if field == 'Category':
            template[field] = Category
        elif field == 'Product Description':
            # create variables for name and descrition of product
            productname, description = input_csv['productname'].loc[row], input_csv['description'].loc[row]
            # the template description field = the return of function call
            template[field] = clean_description(productname, description) 
        else:
            # each cell of input data frame
            input_field = input_csv[input_fields[i]].loc[row]
            # template cell = input cell
            template[field] = input_field    

    # append each row of template dataframe to output_list
    output_list.append(template.iloc[0])

# DataFrame for 'No Variant Template.xlsx'
output_df = pd.DataFrame(
    output_list, # the list we're using for data
    columns=fields # columns for DataFrame 
    )

# write dataframe to csv file
output_df.to_csv('C:/Users/Garrett/Desktop/projectone slack files/Tables/no variant.csv', index=False)
    