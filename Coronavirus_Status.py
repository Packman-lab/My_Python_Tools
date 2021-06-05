#Packman-lab
#05-06-2021
import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"
url1 = "https://www.worldometers.info/coronavirus/country/india"

# To scrape data country specific url path need to be modified
req = requests.get(url)
bsObj = BeautifulSoup(req.text, "html.parser")
data = bsObj.find_all("div",class_ = "maincounter-number")

print("")
print("World :")
print("Total Cases: ", data[0].text.strip())
print("Total Deaths: ", data[1].text.strip())
print("Total Recovered: ", data[2].text.strip())

print("")
print("India :")
req1 = requests.get(url1)
bsObj1 = BeautifulSoup(req1.text, "html.parser")
data1 = bsObj1.find_all("div",class_ = "maincounter-number")

print("Total Cases: ", data1[0].text.strip())
print("Total Deaths: ", data1[1].text.strip())
print("Total Recovered: ", data1[2].text.strip())
