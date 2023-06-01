from random import randint

array = []
for i in range(2000):
    array.append(randint(1, 10000))
array.sort()
print(array)

def binary_search(array, target, min, max):
    test_index = (min+max)//2
    comparison = array[test_index]
    print(min, max)
    if comparison == target:
        return test_index
    elif min == max:
        return -1
    elif comparison < target:
        min = test_index + 1
        return binary_search(array, target, min, max)
    else:
        max = test_index - 1
        return binary_search(array, target, min, max)

target = int(input("Number to search for: "))
target_index = binary_search(array, target, 0, len(array)-1)
print("{} found at index: {}".format(target, target_index))