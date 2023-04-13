import random
import time

def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        for j in range(0, len(unsorted_list) -1 - i):
            if unsorted_list[j] > unsorted_list[j + 1]:
                #change positions of elements when element 1 is bigger than element 2
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    return unsorted_list


#code to run
if __name__ == "__main__":
    l = []
    for i in range(9999):
        l.append(random.randint(0,999))
    start = time.time()
    l = bubble_sort(l)
    print(l)
    end = time.time()
    for i in range(len(l) - 1):
        assert l[i] <= l[i + 1]
    print(end-start)
