"""
File with task 1
"""


class Soup:
    def __init__(self, additional=''):
        self.additional = additional.lower()
        self.soup_dict = {'капуста' : 'щи', 'сардина' : 'рыбный', 'свекла' : 'борщ'}

    def show_my_soup(self):
        return f"Ваш суп - {self.soup_dict[self.additional]}, основной ингредиент - {self.additional}" if self.additional in self.soup_dict else 'Кипяток какой-то, а не суп!'

    def add_new_soup(self, soup, additional):
        self.soup_dict[additional] = soup


if __name__ == '__main__':
    soup1 = Soup()
    print(soup1.show_my_soup())

    soup2 = Soup('капуста')
    print(soup2.show_my_soup())

    soup3 = Soup('лук')
    soup3.add_new_soup('луковый', 'лук')
    print(soup3.show_my_soup())
