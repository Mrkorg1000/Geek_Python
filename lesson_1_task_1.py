
# Временной конвертер. Секунды в дни, часы, мин, сек.
# 1 год = 3 153 600 сек, месяц = 259 200 сек,
# 1 сутки  = 8640 сек, 1 час = 3600 сек, 1 мин = 60 сек.


while True:
    try:
        duration = int(input('Введите промежуток времени в секундах: '))

        if duration < 0:
            raise ValueError
    except ValueError:
        print("Введите целое положительное число")

    else:
        years = duration // 3153600
        months = duration % 3153600 // 259200
        days = duration % 3153600 % 259200 // 8640
        hours = duration % 3153600 % 259200 % 8640 // 3600
        minutes = duration % 3153600 % 259200 % 8640 % 3600 // 60
        sec = duration % 3153600 % 259200 % 8640 % 3600 % 60
        print(f'{years} года/лет, {months} месяцев, {days} дней, {hours} часов, {minutes} минут, {sec} секунд')


