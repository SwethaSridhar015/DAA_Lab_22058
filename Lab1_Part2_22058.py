from datetime import datetime
import time
import random
import matplotlib.pyplot as plt
import heapq

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

#Q1

array=[]
for i in range(1000):
    array.append(random.randint(0,1000))
bubble_start=time.time_ns()
bubble=Bubble(array)
bubble_end=time.time_ns()
print("Number of swaps:",bubble[1])
bubble_time=(bubble_end-bubble_start)
print(f"Bubble Sort Execution Time:{(bubble_time)/1000000:.06f}ms")

insertion_start=time.time_ns()
insertion=Insertion(array)
insertion_end=time.time_ns()
insertion_time=(insertion_end-insertion_start)
print(f"Insertion Sort Execution Time:{(insertion_time)/1000000:.06f}ms")

selection_start=time.time_ns()
selection=Selection(array)
selection_end=time.time_ns()
selection_time=(selection_end-selection_start)
print(f"Selection Sort Execution Time:{(selection_time)/1000000:.06f}ms")

sort_names = ['Bubble Sort', 'Insertion Sort', 'Selection Sort']
times = [bubble_time, insertion_time, selection_time]

plt.figure(figsize=(10, 6))
plt.bar(sort_names, times, color=['blue', 'green', 'red'])
plt.title('Sort Execution Time Comparison')
plt.xlabel('Sort Algorithm')
plt.ylabel('Execution Time (ms)')
plt.show()

print()

#Q2
m=int(input("Enter the number of sorted arrays:"))
arr=[]
for i in range(m):
    a=eval(input("Enter the array:"))
    arr.append(a)

for i in range(m):
    for j in range(m-1-i):
        if arr[j][0]>arr[j+1][0]:
            a=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=a

print("Output:")
for i in arr:
    print(i)

print()

#Q3

arr = eval(input("Enter the array:"))
K = int(input("Enter K :"))
min_heap = arr[:K]
heapq.heapify(min_heap)
for i in range(K, len(arr)):
    if arr[i] > min_heap[0]:
        heapq.heappop(min_heap)
        heapq.heappush(min_heap, arr[i])
        
print("K-largest elements:",min_heap)

print()

#Q4

activities = eval(input("Enter the list of activities:"))
activities.sort(key=lambda x: x[1])
selected_activities = []
last_finish_time = float('-inf')
for activity in activities:
    start_time, finish_time = activity
    if start_time >= last_finish_time:
        selected_activities.append(activity)
        last_finish_time = finish_time

print("Maximum number of activities:", len(selected_activities))
print("Selected activities:", selected_activities)

print()

#Q5
intervals = eval(input("Enter the list of intervals:"))
intervals.sort(key=lambda x: x[0])
merged_intervals=[intervals[0]]
for interval in intervals[1:]:
        current_start, current_end = interval
        last_merged_start, last_merged_end = merged_intervals[-1]
        if current_start <= last_merged_end:
            merged_intervals[-1] = (last_merged_start, max(last_merged_end, current_end))
        else:
            merged_intervals.append(interval)

print("Merged Intervals:", merged_intervals)

print()
