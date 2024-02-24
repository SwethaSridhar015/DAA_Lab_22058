from datetime import datetime
import time
import random

def Bubble(array):
    n=len(array)
    count=0
    for i in range(n):
        for j in range(n-1-i):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
                count=count+1
    return array,count

def Selection(array):
    n=len(array)
    for i in range(n):
        maximum=array[0]
        pos=0
        for j in range(n-i):
            if array[j]>maximum:
                maximum=array[j]
                pos=j
        array[pos]=array[n-i-1]
        array[n-i-1]=maximum
    return array

def Insertion(array):
    n=len(array)
    for i in range(1,n):
        key=array[i]
        j=i-1
        while(j>=0 and array[j]>key):
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key
    return array

array=[]
for i in range(10000):
    array.append(random.randint(0,10000))
bubble_start=time.time_ns()
bubble=Bubble(array)
bubble_end=time.time_ns()
print("Bubble Sort Output:",bubble[0])
print("Number of swaps:",bubble[1])
bubble_time=(bubble_end-bubble_start)
print(f"Bubble Sort Execution Time:{(bubble_time)/1000000:.06f}ms")

insertion_start=time.time_ns()
insertion=Insertion(array)
print("Insertion Sort Output:",insertion)
insertion_end=time.time_ns()
insertion_time=(insertion_end-insertion_start)
print(f"Insertion Sort Execution Time:{(insertion_time)/1000000:.06f}ms")

selection_start=time.time_ns()
selection=Selection(array)
selection_end=time.time_ns()
print("Selection Sort Output:",selection)
selection_time=(selection_end-selection_start)
print(f"Selection Sort Execution Time:{(selection_time)/1000000:.06f}ms")
