import time
import matplotlib.pyplot as plt
import random

def iterative_sum(N):
    Sum_N=0
    for i in range(1,N+1):
        Sum_N=Sum_N+i
    return Sum_N

def recursive_sum(N):
    if N==0:
        return 0
    else:
        return N+recursive_sum(N-1)

def time_taken(function, N):
    start_time = time.time()
    function(N)
    end_time = time.time()
    return end_time - start_time

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def time_taken(search_func, arr, key):
    start_time = time.time()
    search_func(arr, key)
    end_time = time.time()
    return end_time - start_time

def string_to_integer(s):
    if len(s) <= 3:
        return s
    return string_to_integer(s[:-3]) + "," + s[-3:]

def reverse_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[1:-1]) + s[0]

def is_palindrome(s):
     if len(s) <= 1:
        return True
     if s[0]==s[-1]:
         is_palindrome(s[1:-1])
         print('Palindrome')
     else:
        print('Not a palindrome')

#Q1

N=int(input("Enter a number:"))
n_values=list(range(1,N))
Iter_sum=iterative_sum(N)
Recur_sum=recursive_sum(N)

print("Iterative Sum:",Iter_sum)
print("Recursive Sum:",Recur_sum)

time_iter=[]
time_recur=[]

for i in range(1,N):
    time_iter.append(time_taken(iterative_sum,i))
    time_recur.append(time_taken(recursive_sum,i))

print('Iterative times:',time_iter)
print('Recursive times:',time_recur)

plt.plot(n_values,time_iter,label='Iterative')
plt.plot(n_values,time_recur,label='Recursive')
plt.xlabel('N')
plt.ylabel('Time')
plt.title('Time complexity of functions')
plt.legend()
plt.show()


#Q2

random_int=random.sample(range(1, 10001), 10000)

search_keys = random.sample(range(1, 10000),5)

linear_times = []
binary_times = []
for key in search_keys:
    linear_times.append(time_taken(linear_search, random_int, key))
    binary_times.append(time_taken(binary_search, sorted(random_int), key))

print("Linear times:",linear_times)
print("Binary times:",binary_times)
    
plt.plot(range(1, 6), linear_times, label='Linear Search')
plt.plot(range(1, 6), binary_times, label='Binary Search')
plt.xlabel('Search')
plt.ylabel('Time (s)')
plt.title('Time Taken for Linear and Binary Searches')
plt.xticks(range(1, 6))
plt.legend()
plt.show()



#Q3
string = input("Enter a string of digits: ")
result = string_to_integer(string)
print("converted string:",result)



#Q4
Str=input('Enter a string:')
reverse=reverse_string(Str)
print("Reversed string:",reverse)

#Q5
String=input('Enter a string:')
palindrome=is_palindrome(String)
