"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names' + year + '.html'

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features='html.parser')

        # ----- Write your code below this line ----- #
        tags = soup.tbody.find_all('tr')  # [tr1, tr2]
        male_total = 0
        female_total = 0
        for tag in tags[:-1]:
            td = tag.find_all('td')  # [td1, td2]
            male_total += int(remove_sign(td[2].text))
            female_total += int(remove_sign(td[4].text))
        print(f'Male Number: {male_total}')
        print(f'Female Number: {female_total}')


def remove_sign(n):
    clean_int = ''
    number = '0123456789'
    for ch in n:
        if ch in number:
            clean_int += ch
    return clean_int



if __name__ == '__main__':
    main()
