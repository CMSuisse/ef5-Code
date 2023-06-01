from random import randint
import operator

ops =   {"ascend": operator.le,
        "descend": operator.ge}

array = []
for i in range(20):
    array.append(randint(1, 100))
print(array)

def own_sort(unsorted_array, mode):
    sorted_array = []
    element = unsorted_array[0]
    del unsorted_array[0]
    sorted_array.append(element)
    while len(unsorted_array) > 0:
        element = unsorted_array[0]
        del unsorted_array[0]
        for index, comparison in enumerate(sorted_array):
            if ops[mode](element, comparison):
                sorted_array.insert(index, element)
                break
            elif index == len(sorted_array)-1:
                sorted_array.append(element)
                break

    return sorted_array

mode = input("Sort the list ascending or descending (type 'ascend' or 'descend'): ")
print(own_sort(array, mode))