import requests 
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

n = ToastNotifier()

def getdata(url) :
    r = requests.get(url)
    return r.text

htmldata = getdata("https://weather.com/en-IN/weather/today/l/fae343506b25ed3d2aebefac27c45ebdeaa78b11e818531062e2d3e8c323ce52")
                   

soup = BeautifulSoup(htmldata , 'html.parser')

# print(soup.prettify())

current_temp = soup.find_all("span" , class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")


chances_rain = soup.find_all("div" , class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")
temp = str(current_temp)
temp_rain = str(chances_rain)
result = "current_temp " + temp[128:-9] + "  in patna bihar" + "\n" + temp_rain[131:-14]
n.show_toast("live Weather update",  result, duration = 10) 