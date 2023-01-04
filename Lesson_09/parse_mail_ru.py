"""
Here are methods to parse main news from mail.ru
"""

import requests
from bs4 import BeautifulSoup as bs, ResultSet, PageElement

def find_all_hrefs(hrefs:ResultSet[PageElement]) -> list[str]:
    res = []
    for href in hrefs:
        s = str(href)
        res += [s[s.find('href="') + 6: s.find('"', s.find('href="') + 6)]]
    return res


def import_main_news_from_mail_ru() -> ResultSet[PageElement]:
    url = 'https://mail.ru'
    response = requests.get(url).text
    soup = bs(response, 'html.parser')

    news = soup.find_all('a', class_='news__list__item__link news__list__item__link_simple')
    return news


def import_news_from_news_mail_ru(href: str) -> PageElement:
    url = href
    response = requests.get(url).text
    soup = bs(response, 'html.parser')
    return soup.find('div', class_='article__intro meta-speakable-intro')


def read_one_piece_of_news(n: int, hrefs_list: list[str]) -> list[str]:
    href = hrefs_list[n - 1]
    tidings = import_news_from_news_mail_ru(href)
    return [tidings.text] + [href]


if __name__ == '__main__':
    print('Главные новости этого часа на mail.ru:')
    news = import_main_news_from_mail_ru()
    hrefs = find_all_hrefs(news)
    for i, a in enumerate(zip(news, hrefs), start=1):
        print('\t', i, '. ', a[0].text, ' - ', a[1], sep='')
    number = int(input('\nВведите номер новости, которую хотите открыть: ')) % 10
    if number:
        print(' - '.join(read_one_piece_of_news(number, hrefs)))
    else:
        print('Номер новости не найден')
