# напишіть функцію, яка перевірить, чи передане їй число є парним чи непарним (повертає True False)

def check_paired(num):
    if num % 2 == 0:
        return True
    else:
        return False

num = 12
my_primes = [2, 3, 5, 7]

print(check_paired(num))

# напишіть функцію. яка приймає стрічку, і визначає, чи дана стрічка відповідає результатам роботи
# методу capitalize() (перший символ є верхнім регістром, а решта – нижнім.) (повертає True False)

def check_capitalized(my_str):
    new_str = my_str.lower()
    new_str = new_str.capitalize()
    if my_str == new_str:
        return True
    else:
        return False

my_str = "RavO"

print(check_capitalized(my_str))

# написати декоратор, який добавляє принт з результатом роботи отриманої функції + текстовий параметр,
# отриманий ним (декоратор з параметром - це там, де три функції)

# при цьому очікувані результати роботи функції не змінюються (декоратор просто добавляє принт)

def my_decor():
    func1 = check_paired(num)
    func2 = check_capitalized(my_str)

    print("My 1-st result is", func1, ": ", num)
    print("My 2-nd result is", func2, ": ", my_str)

    return func1
    return func2

my_decor()
