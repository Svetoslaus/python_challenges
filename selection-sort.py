import random
import time


def selection_sort(unsorted_list):
    for index in range(len(unsorted_list)):
        minimum_index = index
        for i in range(minimum_index + 1, len(unsorted_list)):
            if unsorted_list[minimum_index] > unsorted_list[i]:
                minimum_index = i

        # switch start element with minimum value element
        cache = unsorted_list[index]
        unsorted_list[index] = unsorted_list[minimum_index]
        unsorted_list[minimum_index] = cache

    return unsorted_list


if __name__ == "__main__":
    l = []
    for i in range(9999):
        l.append(random.randint(0, 999))
    start = time.time()
    l = (selection_sort(l))
    print(l)
    end = time.time()
    for i in range(len(l)-1):
        assert l[i] <= l[i+1]
    print(end - start)
