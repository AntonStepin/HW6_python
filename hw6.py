# 1- Определить, присутствует ли в заданном списке строк, некоторое число
import math



def number_in_list(user_list, number):
    return list(filter(lambda element: str(number) in element, user_list))

# user_lst = ["главн5ое", "верить", "в", "себ5"]
# print(number_in_list(user_lst, 5))

# 2- Найти сумму чисел списка стоящих на нечетной позиции
def int_value(user_number):
    result = user_number
    if not result.isdigit():
        return False
    else:
        return int(result)

def create_list():
    return list(range(1, int(int_value(input("Введите число: "))+1)))

def sum_odd():
    user_list = create_list()
    result = list(filter(lambda x: user_list.index(x)%2, user_list))
    return sum(result)

# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)

def check_for_positions():
    positions_txt = input("Enter positions for all points(exm: x1 y1 x2 y2): ")
    while 1:
        positions_txt_test = positions_txt.split(" ")
        positions = list(filter(lambda x: x.isdigit(),positions_txt_test))
        if len(positions) != 4:
            positions_txt = input(f"You enter {len(positions)} numbers, enter again no more or less 4 numbers: ")
        else:
            break
    return positions

def distance_btw_dots():
    positions = check_for_positions() #format [x1 y1 x2 y2] 
    return math.ceil(((int(positions[0]) - int(positions[2]))**2 + (int(positions[3])-int(positions[1]))**2)**0.5)

# print(distance_btw_dots())

# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3

def second_in_lst(user_lst:list):
    # return  list(filter(lambda x: x for i, element in user_lst if element in user_lst[i]))
    second_match = []
    count= 0
    history = []
    for x in user_lst:
        count = 0
        for i in range(0,len(user_lst)):
            if x in user_lst[i] and not x in history:
                count += 1
                if count == 2:
                    history.append(x)
                    second_match.append((i, user_lst[i]))
    return second_match

# user_lst = ["qwe", "asd", "zxc", "qwe", "ertqwe", "qwe", "asd", "bbb"]
# print(second_in_lst(user_lst))

# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def check_list_digit(user_lst):
    check = list(filter(lambda element: str(element).isdigit(),user_lst))
    if len(check) == len(user_lst):
        return check
    print ("Your list has not digit element")
    return exit ()


def sum_pair_in_side(user_lst):
    user_lst_test = check_list_digit(user_lst)
    result = [user_lst_test[i] * user_lst_test[-i-1] for i in range (math.ceil(len(user_lst_test)/2))]
    return result

# print (sum_pair_in_side([1, 2, 3, 4, 5]))

# 6-Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

def chek_int_value(user_number):
    user_number = int_value(str(user_number))
    if not user_number:
        print ("Your atribute not a digit")
        exit()
    else:
        return user_number
def n_sequence(n):
    n = chek_int_value(n)
    return [int(-3)**i for i in range (n+1)]

# print(n_sequence(5))
