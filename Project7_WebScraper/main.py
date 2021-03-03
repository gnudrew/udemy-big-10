import requests
from bs4 import BeautifulSoup
import pandas

base_url="http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/"

r = requests.get(base_url, headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content
soup = BeautifulSoup(c, "html.parser")

pages = soup.find_all("a",{"class":"Page"})
last_page = pages[-1].text

l=[]
for page in range(0,int(last_page)*10,10):
    r = requests.get(base_url+"t=0&s="+str(page)+".html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c = r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"propertyRow"})
    for item in all:
        d = {}
        d["Price"]=item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
        d["Address_1"]=item.find_all("span",{"class":"propAddressCollapse"})[0].text
        d["Address_2"]=item.find_all("span",{"class":"propAddressCollapse"})[1].text
        try:
            d["Beds"]=item.find("span",{"class":"infoBed"}).find("b").text
        except:
            d["Beds"]=None
        try:
            d["SqFt"]=item.find("span",{"class":"infoSqFt"}).find("b").text
        except:
            d["SqFt"]=None
        try:
            d["Bathrooms"]=item.find("span",{"class":"infoValueFullBath"}).find("b").text
        except:
            d["Bathrooms"]=None
        try:
            d["Half Bathrooms"]=item.find("span",{"class":"infoValueHalfBath"}).find("b").text
        except:
            d["Half Bathrooms"]=None
        for colGroup in item.find_all("div", {"class":"columnGroup"}):
            for featureGroup, featureName in zip(colGroup.find_all("span",{"class":"featureGroup"}),colGroup.find_all("span",{"class":"featureName"})):
                if "Lot Size" in featureGroup.text:
                    d["Lot Size"]=featureName.text
        l.append(d)

df = pandas.DataFrame(l)
df.to_csv("Output.csv")