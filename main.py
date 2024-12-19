# def mult(lst):
#     n = 1
#     for num in lst:
#         n *= num
#     return n
#
# print(mult([1, 2, 3, 4, 5]))


# task 2

# def minn(lst):
#     return min(lst)
#
#
# print(minn([2, 1, 3, 4, 5, 6]))


# task 3

# def prime_number(lst):
#     lst_prime_num = []
#     for num in lst:
#         for n in range(2, int(num**0.5)+1):
#             if num % n == 0:
#                 lst_prime_num.append(num)
#     return lst_prime_num
#
#
# print(prime_number([1, 2, 3, 4, 5, 6, 7]))


# task 4

# def remove_add_new(lst):
#     lst_removed_items = []
#     while True:
#         num = int(input("write a number: "))
#         var = lst[num]
#         lst_removed_items.append(var)
#
#         yes_no = input("continue, yes or no: ")
#         if yes_no == 'yes':
#             continue
#         else:
#             break
#
#     return f"quantity of removed items from list - {len(lst_removed_items)}"
#
# print(remove_add_new([1, 2, 3, 4, 5, 6]))



# task 5

# def add_lists(lst1, lst2):
#     return lst1 + lst2
#
# print(add_lists([1, 2, 3, 4], ["2", "3", "5"]))


# task 6

def power_of_lst(pow, lst):
    new_lst = []
    for number in lst:
        calc = number ** pow
        new_lst.append(calc)
    return new_lst

print(power_of_lst(2, [2, 3, 4, 5]))