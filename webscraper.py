from bs4 import BeautifulSoup
import requests

page = requests.get("https://primes.utm.edu/lists/small/millions/")

soup = BeautifulSoup(page.content, 'html.parser')

for link in soup.find_all('a'):
    l = str(link.get('href'))
    if "millions/prime" in l:
        file = requests.get(l)
        name = 'undef'
        if l[-6] == 's':
            #One number file
            name = l[-11:]
        else:
            #Two number file
            name = l[-12:]
        print(name)
        open(name, 'wb').write(file.content)

