import re

def remove_name_from_product_description(productname, description):

    # r'\s' + adds a white space to the begining of the pattern
    pattern = r'\s' + productname  # pattern we're looking for

    replacement = ''  # what to replace the string with

    target = description  # the string we want to replace

    # re.sub replaces the string and ignorescase
    replaced = re.sub(pattern, replacement, target, flags=re.IGNORECASE)

    # replace description of each product in original file
    return replaced

def remove_style_number_from_product_description(description):

    pattern = r'( Style No : )\d+\s' # pattern we're looking for

    replacement = ''  # replace pattern with nothing

    target = description  # the string we want to replace

    # re.sub replaces the string and ignorescase
    replaced = re.sub(pattern, replacement, target, flags=re.IGNORECASE)

    # return the cleaned string
    return replaced

def remove_colors_from_descrition(description):
    
    # pattern we're looking for
    # 2 patterns
    # (Color : )\w+\s OR (Color : )\w+,\s*\w+\s*
    pattern = r'((Color : )\w+\s|(Color : )\w+,\s*\w+\s*)'    

    replacement = ''             # replace pattern with nothing
    target = description         # the string we want to replace

    # re.sub replaces the string and ignorescase
    replaced = re.sub(pattern, replacement, target, flags=re.IGNORECASE)

    return replaced # return the cleaned string

def clean_description(productname, description):
  # chain functions together and return result
  description_no_name = remove_name_from_product_description(productname, description)
  description_no_style = remove_style_number_from_product_description(description_no_name)
  description_no_color = remove_colors_from_descrition(description_no_style)
  return description_no_color
