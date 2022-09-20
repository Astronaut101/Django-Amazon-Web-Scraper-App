from pathlib import Path

import lxml
from bs4 import BeautifulSoup


# -- Path Variables
TEMPLATE_BASE_PATH = Path.cwd() / Path('templates')
BASE_TEMPLATE = Path('base.html')


# -- Extracting our scraped data from our targetted URL
with open(TEMPLATE_BASE_PATH / BASE_TEMPLATE, 'r') as file:
    body = file.read()

# -- Getting the formatted html content 
soup = BeautifulSoup(body, 'lxml')
# print(soup.prettify())

# -- Getting the title
title = soup.title
# print(title)
# print(title.name)
print(title.getText())

# -- Getting the paragraph
paragraph = soup.p
print(paragraph)
# print(paragraph.name)
print(paragraph.getText())

# -- Getting the first div
first_div = soup.find('div')
# print(first_div)
print(first_div.getText())

# -- Getting all the divs
# all_divs = soup.find_all('div')
# print(all_divs)
# for div in all_divs:
#     print('----')
#     print(div)

# -- Get the first movie
# first_movie = soup.find('div', class_='movie')
first_movie = soup.select('.movie')  # returns a list of scraped objects
print(first_movie[0])
# print(first_movie.getText())

# -- Get all movies
# all_movies = soup.find_all('div', class_='movie')  # Method 01
all_movies = soup.select(selector='.movie')  # Method 02
for movie in all_movies:
    print('-----')
    print(movie.getText())

# -- Get all the links
links = soup.find_all('a')
for link in links:
    print('-----')
    # print(link)
    # print(link.getText())
    print(link.get('href'))

# -- Get element by ID
movie_box = soup.select_one('#movie-box')
print(movie_box)
print(movie_box.getText())

# -- Getting the Parent/Children
parent = movie_box.parent
print(parent)
children = movie_box.children
for child in children:
    print(child)

movie = soup.find('div', class_='movie')
parent = movie.find_parent()
print('-----')
print(parent)
parent = movie.find_parent('div')
print('-----')
print(parent)

interstellar = soup.find(text="Interstellar")
print('-----')
print(interstellar)
print('-----')
print(interstellar.find_parent())
print('-----')
print(interstellar.find_parent('div'))
print('-----')
print(interstellar.find_parent('a'))