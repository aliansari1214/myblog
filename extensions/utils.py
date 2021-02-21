from . import jalali
from django.utils import timezone


def persian_number_converter(mystr):
    numbers = {
        '0': '۰',
        '1': '۱',
        '2': '۲',
        '3': '۳',
        '4': '۴',
        '5': '۵',
        '6': '۶',
        '7': '۷',
        '8': '۸',
        '9': '۹',
    }
    for e, p in numbers.items():
        mystr = mystr.replace(e, p)

    return mystr


def jalali_converter(time):
    jmonth = [
        "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر",
        "آبان", "آذر", "دی", "بهمن", "اسفند"
    ]

    time = timezone.localtime(time)
    time_is_str = "{},{},{}".format(time.year, time.month, time.day)
    time_is_tuple = jalali.Gregorian(time_is_str).persian_tuple()
    time_is_list = list(time_is_tuple)

    for index, month in enumerate(jmonth):
        if time_is_list[1] == index + 1:
            time_is_list[1] = month
            break

    output = '{} {} {}  ساعت  {}:{}'.format(time_is_list[2], time_is_list[1],
                                            time_is_list[0], time.hour,
                                            time.minute)

    return persian_number_converter(output)