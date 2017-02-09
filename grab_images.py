from bs4 import BeautifulSoup
from selenium import webdriver


SEARCH_URL = "http://www.metmuseum.org/art/collection/search#!?showOnly=openaccess&offset=0&q=cuneiform&pageSize=0&sortBy=Relevance&sortOrder=asc&perPage=100"

def get_list_url(offset):
    return "http://www.metmuseum.org/art/collection/search#!?showOnly=openaccess&offset={}&q=cuneiform&pageSize=0&sortBy=Relevance&sortOrder=asc&perPage=100".format(str(offset))

def get_image_urls(url):
    # grab all of the links
    # first <a> under each div with class="card__text"
    # link looks like: http://www.metmuseum.org/art/collection/search/329081?sortBy=Relevance&amp;ft=cuneiform&amp;offset=0&amp;rpp=100&amp;pos=1
    # but need only: http://www.metmuseum.org/art/collection/search/329081


