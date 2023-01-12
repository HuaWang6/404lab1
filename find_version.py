import requests
#print current python version
print(requests.__version__)
#print google home page's information
print(requests.get("https://raw.githubusercontent.com/HuaWang6/404lab1/master/find_version.py").text)

