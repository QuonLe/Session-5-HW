def get_even_list(list_number):
    for number in list_number:
        if number % 2 == 1:
            list_number.remove(number)
    return list_number

even_list = get_even_list([1, 2, 5, -10, 9, 6])
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
