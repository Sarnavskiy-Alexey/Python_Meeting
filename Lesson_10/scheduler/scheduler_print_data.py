"""
File with print_data methods
"""


def change_date_to_emoji(date: str):
    res = date.split('-')
    for i in range(len(res)):
        res[i] = change_digits_to_emoji(res[i])
    return '➖'.join(res)


def change_time_to_emoji(time: str):
    d = {
        '01:00' : '🕐', '02:00' : '🕑', '03:00' : '🕒', '04:00' : '🕓', '05:00' : '🕔',
        '06:00' : '🕕', '07:00' : '🕖', '08:00' : '🕗', '09:00' : '🕘', '10:00' : '🕙',
        '11:00' : '🕚', '12:00' : '🕛', '13:00' : '🕐', '14:00' : '🕑', '15:00' : '🕒',
        '16:00' : '🕓', '17:00' : '🕔', '18:00' : '🕕', '19:00' : '🕖', '20:00' : '🕗',
        '21:00' : '🕘', '22:00' : '🕙', '23:00' : '🕚', '00:00' : '🕛',
        '01:30' : '🕜', '02:30' : '🕝', '03:30' : '🕞', '04:30' : '🕟', '05:30' : '🕠',
        '06:30' : '🕡', '07:30' : '🕢', '08:30' : '🕣', '09:30' : '🕤', '10:30' : '🕥',
        '11:30' : '🕦', '12:30' : '🕧', '13:30' : '🕜', '14:30' : '🕝', '15:30' : '🕞',
        '16:30' : '🕟', '17:30' : '🕠', '18:30' : '🕡', '19:30' : '🕢', '20:30' : '🕣',
        '21:30' : '🕤', '22:30' : '🕥', '23:30' : '🕦', '00:30' : '🕧'
    }
    time = time.split(':')
    if 0 < int(time[1]) < 30:
        time[1] = '00'
    elif 30 < int(time[1]) < 60:
        time[1] = '30'
    time = ':'.join(time)
    return d[time]


def change_digits_to_emoji(digits: str):
    d = {
        '0' : '0️⃣', '1' : '1️⃣', '2' : '2️⃣', '3' : '3️⃣', '4' : '4️⃣',
        '5' : '5️⃣', '6' : '6️⃣', '7' : '7️⃣', '8' : '8️⃣', '9' : '9️⃣'
     }
    digits = list(digits)
    for i in range(len(digits)):
        digits[i] = digits[i].replace(digits[i], d[digits[i]])
    return ''.join(digits)


def print_data(data: list) -> str:
    res = []
    if len(data):
        res = ['Вот, что было найдено по вашему запросу:']
        for idx, item in enumerate(data, 1):
            res += [f'{change_digits_to_emoji(str(idx))}\nДата: {change_date_to_emoji(item[0][:10])}\n{item[0][11:] + change_time_to_emoji(item[0][11:])}\nКурс: "{item[1]}"\nНомер занятия: {change_digits_to_emoji(item[2])}\nТема: "{item[3]}"\nЗаметка: {item[4]}\n']
    else:
        res = ['К сожалению, нужной информации не найдено!']

    return '\n'.join(res)
