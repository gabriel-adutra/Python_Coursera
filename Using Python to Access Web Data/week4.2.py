import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


URL = input("Enter the URL:") #Enter main URL
posicao = int(input("Enter position:")) - 1 #The position of link relative to first link
count = int(input("Enter count:")) #The number of times to be repeated

while count >= 0:
    html = urllib.request.urlopen(URL, context=ctx).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    print(URL)
    URL = tags[posicao].get("href", None)
    count = count - 1
