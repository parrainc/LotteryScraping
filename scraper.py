import re
import urllib.request
from bs4 import BeautifulSoup

url = "http://www.loteriasdominicanas.com/"

try:
    html = urllib.request.urlopen(url).read()
except:
    print("Error opening the url")
    exit()

# for i in range(0,3):
#     regex = '<div class="content"><ul style="width: 600px;float: left;">' \
#             '<li>(.+?)</li></ul></div>'
#
#     # pattern = re.compile(regex)
#     numbers = re.findall(b"<li>(.+?)</li>", html)
#     print(numbers)
soup = BeautifulSoup(html, "html.parser")

other = soup.find_all('div', class_='content')
lotteries = soup.select('div.lottery-list div.heading')
numbers = soup.select('div.lottery-list div.content ul')
date = soup.select('div.lottery-list div.content div.status')

lotteries_names = [lottery_name.contents[4].strip()
                   for lottery_name in lotteries]
numbers_dict = dict()
dates_list = [dates.contents[2].strip() for dates in date]

# for dates in date:
#    print(dates.contents[2].strip())

increment = 0
# for names in lotteries:
#     lotteries_names.append(names.contents[4].strip())

for tag in numbers:
    #var.append(tag.contents)
    #numbers_list.append(tag.contents)

    numbers_list = re.findall('<li>(.+?)</li>+?', str(tag.contents))
    #print(i)
    numbers_dict[lotteries_names[increment]] = {'numbers':numbers_list,
                                                'date':dates_list[increment]}
    increment = increment + 1

    # print(tag.contents[4].strip())

for k,v in numbers_dict.items():
    print(k, v)

# for tag in soup.find_all(re.compile("<li>(.+?)</li>")):
#     print(tag.contents)
