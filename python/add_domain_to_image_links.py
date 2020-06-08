def add_domain_to_image_links(image_link):

    domain = 'www.wonatrading.com/'

    # if image link is a string add domain
    if isinstance(image_link, str):
        return domain + image_link

    # otherwise return an empty string
    return ''