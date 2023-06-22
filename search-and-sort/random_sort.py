from random import randint

unsorted_array = []
for i in range(5):
    unsorted_array.append(randint(1, 100))

def random_sort(array):
    new_array = []
    for element in array:
        new_array.insert(randint(0, len(new_array)), element)
    for index, element in enumerate(new_array):
        if index == len(new_array)-1:
            return new_array
        if element >= new_array[index+1]:
            return random_sort(new_array)

sorted_array = random_sort(unsorted_array)
print(unsorted_array)
print(sorted_array)