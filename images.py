from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os
import sys


def StartSearch():
    search = input("Search for: ")
    if search == "exit":
        sys.exit()
    params = {"q": search}
    dir_name = search.replace(" ", "_").lower()
    
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    
    r = requests.get("http://bing.com/images/search?", params = params)
    
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})
    
    for each in links:
        try:
            img_ogj = requests.get(each.attrs["href"])
            print("Getting", each.attrs["href"])
            title = each.attrs["href"].split("/")[-1]
            try:
                img = Image.open(BytesIO(img_ogj.content))
                img.save("./" + dir_name +"/" + title + "." + img.format)
            except:
                print("Could not save image")
        except:
            print("Could not request image")
StartSearch()

