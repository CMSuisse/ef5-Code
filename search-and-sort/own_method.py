from random import randint
array = []
for i in range(20):
    array.append(randint(1, 100))
print(array)

def own_sort(unsorted_array):
    sorted_array = []
    element = unsorted_array[0]
    del unsorted_array[0]
    sorted_array.append(element)
    while len(unsorted_array) > 0:
        element = unsorted_array[0]
        del unsorted_array[0]
        for index, comparison in enumerate(sorted_array):
            if element <= comparison:
                sorted_array.insert(index, element)
                break

    return sorted_array

print(own_sort(array))