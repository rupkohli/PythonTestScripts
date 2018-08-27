# Import libraries
import requests
from bs4 import BeautifulSoup

# Collect first page of artists’ list
page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')

page2 = requests.get('https://www.google.co.in/search?q=predictive+software+testing')

page3 = requests.get('https://www.google.co.in/search?q=predictive+software+testing&rlz=1C5CHFA_enIN746IN746&source=lnt&tbs=qdr:m&sa=X&ved=0ahUKEwjD1Zbzl_DcAhUBqY8KHT8lByAQpwUIHg&biw=825&bih=780')

# Create a BeautifulSoup object
soup = BeautifulSoup(page2.text, 'html.parser')

# Pull all text from the BodyText div
search_list = soup.find(class_='BodyText')

# Pull all text from the med div of page3
search_list0 = soup.find_all('cite')
print('1=========================med')
print(search_list0)

#search_list = soup.find(class_='g')
#print('2=========================g')
#print(search_list)

#print()
#also read the st class which gives the summary on the link
#search_list1 = soup.find(class_='st')

# Pull text from all instances of <a> tag within BodyText div
#search_list_items = search_list0.find_all('a')
#print('3=========================')
#print(search_list_items)

#print()
#print('4=========================')

#print(search_list1)

#print()
#print(search_list_items[0])

#print()
#print (search_list_items[1])

print('5=========================LOOP')


#Create for loop to print out all artists' names
for search in search_list0:
    print(search.prettify())
    #print(search_list1)

