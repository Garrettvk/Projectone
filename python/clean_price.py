import re

def clean_price(price):

    pattern = re.compile(r'\d.{2}\d')  # pattern we're looking for

    matches = pattern.finditer(price)

    matches_list = [match.group() for match in matches]

    return matches_list[0]