# import requests
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# res.status_code == requests.codes.ok
# len(res.text)
#print(res.text[:250])

import requests, sys, webbrowser, bs4

print('Googling...')    # display text while downloading the Google page

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
#print(res.text[:250])

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, features="html.parser")

# Open a browser tab for each result.
linkElems = soup.select('.r a')
print (len(linkElems))
webbrowser.open('http://google.com' + linkElems[0].get('href'))


# Retrieve top search result links.
soup1 = bs4.BeautifulSoup(res.text, features="html.parser")
#print (soup1)
linkElems1 = soup1.select('.r img')

print(linkElems1)
#webbrowser.open('http://google.com' + linkElems1[0].get('src'))
