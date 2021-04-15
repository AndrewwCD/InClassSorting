import csv
import time
def insertion_sort(list):
    for i in range(1,len(list)):
        k = list[i]
        prev = i-1
        while prev >= 0 and len(k) < len(list[prev]):
            list[prev+1] = list[prev]
            prev = prev - 1
        list[prev + 1] = k
    return list

def quicksort(list):
    low = []
    equal = []
    high = []
    if len(list) > 1:
        prev = list[0]
        for i in list:
            if len(i) < len(prev):
                low.append(i)
            elif len(i) == len(prev):
                equal.append(i)
            elif len(i) > len(prev):
                high.append(i)
        return quicksort(low) + equal + quicksort(high)
    else:
        return list

def merge_sort(list):
    list.sort(reverse = True)
    if len(list) > 1:
        middle = len(list)//2
        left = list[:middle]
        right = list[middle:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if len(left[i]) < len(right[j]):
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
    return list


data = open("20k.txt")
data = data.read().splitlines()
print("predicted execution time: insertion sort > quicksort = merge sort")
print("insertion sort = O(N^2), quicksort = O(NlogN), merge sort = O(NlogN) ")
print("data:\n",data[:30] + [". . ."])
data.sort()
time_start = time.time()
insertion_sorted = insertion_sort(data)
exec_time = time.time() - time_start
print("insertion sort sorted:\n",insertion_sorted[:30] + [". . ."])
print(exec_time)
time_start = time.time()
quicksort_sorted = quicksort(data)
exec_time = time.time() - time_start
print("quicksort sorted:\n",quicksort_sorted[:30] + [". . ."])
print(exec_time)
time_start = time.time()
merge_sort_sorted = merge_sort(data)
exec_time = time.time() - time_start
print("merge sort sorted:\n",merge_sort_sorted[:30] + [". . ."])
print(exec_time)