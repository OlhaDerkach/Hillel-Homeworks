#Hапишіть программу "Касир в кінотеатрі", яка буде виконувати наступне:
#
# Попросіть користувача ввести свсвій вік.
# - якщо користувачу менше 7 - вивести "Тобі ж <>! Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Тобі лише <>, а це е фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Вам <>? Покажіть пенсійне посвідчення!"
# - якщо вік користувача містить 7 - вивести "Вам <>, вам пощастить"
# - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <>, білетів всеодно нема!"
#
# Замість <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік
#
# Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача (1 - рік, 22 - роки, 35 - років і тд...).
#
# Наприклад :
#
# "Тобі ж 5 років! Де твої батьки?"
# "Вам 81 рік? Покажіть пенсійне посвідчення!"
# "Незважаючи на те, що вам 42 роки, білетів всеодно нема!"
#
# Зробіть все за допомогою функцій! Не забувайте що кожна функція має виконувати тільки одне завдання і про правила написання коду.

def check_input(user_age):
    if user_age.isdigit():
        return True
    else:
        print("Уважніше! Треба вводити ціле числове значення!")
        return False

def check_age_overstated(user_age):
    if 0 < int(user_age) < 100:
        return True
    else:
        print("Стільки люди не живуть!")
        return False

def make_year(user_age):
    if 10 < int(user_age) < 20:
        s = 9
    else:
        s = user_age[len(user_age)-1]

    if int(s) == 1:
        year = "рік"
    elif 1 < int(s) < 5:
        year = "роки"
    else:
        year = "років"

    return year

def do_main_check(user_age):
    final_age = int(user_age)
    if final_age < 7:
        print("Тобі ж", final_age, make_year(user_age), ", де твої батьки?")
    elif final_age < 16:
        print("Тобі лише", final_age, make_year(user_age), ", а це є фільм для дорослих!")
    elif final_age > 65:
        print("Вам", final_age, make_year(user_age), "? Покажіть пенсійне посвідчення!")
    elif final_age or final_age % 10 == 7:
        print("Тобі", final_age, make_year(user_age), ", тобі сьогодні пощастить")
    else:
        print("Незважаючи на те, що Вам", final_age, make_year(user_age), "білетів всеодно нема!")

user_age = input("Скільки тобі років? ")

if check_input(user_age) == True:
    if check_age_overstated(user_age) == True:
        do_main_check(user_age)
