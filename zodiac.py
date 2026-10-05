import sys

day = int(input("Введите день рождения: "))
month = int(input("Введите месяц рождения: "))

if month < 1 or month > 12:
    print("Ошибка: некорректный месяц!")
    print("Введите месяц от 1 до 12")
    sys.exit()

if month == 2 and (day < 1 or day > 29):
    print("Ошибка: в феврале не может быть больше 29 дней!")
    sys.exit()
elif month in [4, 6, 9, 11] and (day < 1 or day > 30):
    print("Ошибка: в этом месяце только 30 дней!")
    sys.exit()
elif day < 1 or day > 31:
    print("Ошибка: в этом месяце только 31 день!")
    sys.exit()

if (month == 3 and day >= 21) or (month == 4 and day <= 19):
    zodiac = "Овен"
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    zodiac = "Телец"
elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
    zodiac = "Близнецы"
elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
    zodiac = "Рак"
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    zodiac = "Лев"
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    zodiac = "Дева"
elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    zodiac = "Весы"
elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    zodiac = "Скорпион"
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    zodiac = "Стрелец"
elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
    zodiac = "Козерог"
elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
    zodiac = "Водолей"
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    zodiac = "Рыбы"

print("Ваш знак зодиака:", zodiac)
