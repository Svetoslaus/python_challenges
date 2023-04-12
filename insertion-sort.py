import random
import time

def insertion_sort(unsorted_list):
    sorted_list = []
    while(len(unsorted_list) > 0):
        smallest = unsorted_list[0]
        smallest_index = 0
        for index, element in enumerate(unsorted_list):
            if element < smallest:
                smallest = element
                smallest_index = index
        # remove the first smallest element from the list
        unsorted_list.pop(smallest_index)
        # include the first smallest element to the empty sorted_list
        sorted_list.append(smallest)

    return sorted_list


if __name__ == "__min__":
    l = []
    for i in range(9999):
        l.append(random.randint(0, 999))
    start = time.time()
    print(insertion_sort(l))
    end = time.time()
    print(end-start)
