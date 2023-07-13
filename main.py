from bs4 import BeautifulSoup
import requests
import csv
import lxml
i=1
while i<=113:
    association=[]
    page = requests.get(f"https://jamaity.org/associations/page{i}/")
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    associations = soup.find_all('a', {'class':'card-xs-textflow text-left'})
    for j in range(len(associations)):
        association.append(associations[j].text)
    print(association)
    i+=1



