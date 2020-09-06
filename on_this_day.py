# on this day
from datetime import date
import random
today = date.today()
# Textual month, day and year
d2 = today.strftime("%B")
d1 = today.strftime("%d") # gettin the date
d3 = (f'{d2}_{d1}')

import bs4
import requests
res = requests.get(f'https://en.wikipedia.org/wiki/{d3}')    # finding the wikipedia page
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

soupy = soup.select('ul')  # selecting element lists

texty = (soupy[2].getText())   # getting the second list on the page
lines = texty.count('\n')      # counting number of lines in multi-line string
a = random.randint(0, lines)       # getting a random number as high as the number of lines
y =texty.split('\n')[a]      # getting a random line from the string

texty = (soupy[1].getText())
nlines = texty.count('\n')
int = random.randint(0, nlines)
x =texty.split('\n')[int]

texty = (soupy[3].getText())
line = texty.count('\n')
a = random.randint(0, line)
z =texty.split('\n')[a]

print(f'On this day: {d2} {d1}')
print(x)
print(f'{y} was born')
print(f'{z} died')

