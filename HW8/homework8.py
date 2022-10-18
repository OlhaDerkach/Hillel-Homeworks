def my_decor(func):
    ''' Оголошений декоратор '''

    def wrapper():
    ''' Обгортка, яка:

    1) змінює тип змінної, яку поверне функція,на str;
    2) друкує новий тип змінної
    '''

        new_res = str(func)
        print(type(new_res))
    return wrapper

@my_decor
def add_nums():
    ''' Декорована функція '''
    res = int(5)
    return res

add_nums()
