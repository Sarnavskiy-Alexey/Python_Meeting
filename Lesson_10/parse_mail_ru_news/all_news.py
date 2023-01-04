import Lesson_10.parse_mail_ru_news.parse_mail_ru as pm

hrefs_from_news = []


def all_news():
    global hrefs_from_news
    news = pm.import_main_news_from_mail_ru()
    hrefs_from_news = []
    hrefs_from_news = pm.find_all_hrefs(news)
    res = ['Главные новости этого часа на mail.ru:']
    for i, a in enumerate(news, 1):
        res += [f"""{i}. {a.text}\n"""]
    res = '\n'.join(res)
    return res


def one_tidings(n: int):
    res = '\n\nПодробнее: '.join(pm.read_one_piece_of_news(n, hrefs_from_news))
    return res
