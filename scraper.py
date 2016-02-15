# author: Carlos Parra (Parra Inc)
# python-version: 3.4.3 (3.x)

import re
import urllib.request
from bs4 import BeautifulSoup

url = "http://www.loteriasdominicanas.com/"

try:
    html = urllib.request.urlopen(url).read()
except:
    print("Error opening the url")
    exit()

soup = BeautifulSoup(html, "html.parser")

lotteries = soup.select('div.lottery-list div.heading')
numbers = soup.select('div.lottery-list div.content ul')
date = soup.select('div.lottery-list div.content div.status')

lotteries_names = [lottery_name.contents[4].strip()
                   for lottery_name in lotteries]
dates_list = [dates.contents[2].strip() for dates in date]
numbers_dict = dict()

increment = 0

for tag in numbers:
    numbers_list = re.findall('<li>(.+?)</li>+?', str(tag.contents))
    numbers_dict[lotteries_names[increment]] = {'numbers': numbers_list,
                                                'date': dates_list[increment]}
    increment = increment + 1


for k, v in numbers_dict.items():
    print(k, v)
