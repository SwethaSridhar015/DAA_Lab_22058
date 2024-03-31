#Q1
arr=eval(input("Enter an array of integers:"))
s=int(input("Enter the required sum:"))
pairs=[]
for i in arr:
    for j in arr:
        if i+j==s and j!=i and (j,i) not in pairs:
            pairs.append((i,j))
if len(pairs)>0:
    print("Pairs giving required sum:",pairs)
else:
    print("Pair not found")

print()

#Q2

arr=eval(input("Enter an array of integers:"))
pro=float('-inf')
val=()
for i in arr:
    for j in arr:
        if j*i>pro and j!=i:
            pro=j*i
            val=(i,j)

print("Maximum Product :",pro)
print("Values :",val)

print()

#Q3

arr=eval(input("Enter an array of integers:"))
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if arr[j]<arr[i]:
            a=arr[i]
            arr[i]=arr[j]
            arr[j]=a
print("Sorted array:",arr)

print()

#Q4

arr=eval(input("Enter a binary array:"))
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if arr[j]<arr[i]:
            a=arr[i]
            arr[i]=arr[j]
            arr[j]=a
print("Output array:",arr)

print()

#Q5

arr=eval(input("Enter an array of positive integers:"))
count=0
pairs=[]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if arr[j]<arr[i]:
            pairs.append((arr[i],arr[j]))
            count=count+1
print("Inversions:",pairs)
print("Inversion count :",count)

print()

#Q6

#a.

arr=eval(input("Enter an array of integers:"))
s=int(input("Enter the required sum:"))
pairs=[]
for i in arr:
    for j in arr:
        if i+j==s and (j,i) not in pairs:
            pairs.append((i,j))
if len(pairs)>0:
    print("Yes",pairs)
else:
    print("Pair not found")

print()

#b.

arr.sort() 
left = 0
right = len(arr) - 1
pairs = []

while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == s:
        pairs.append((arr[left], arr[right]))
        left += 1
        right -= 1
        while left < right and arr[left] == arr[left - 1]:
            left += 1
        while left < right and arr[right] == arr[right + 1]:
            right -= 1

    elif current_sum < s:
        left += 1
    else:
        right -= 1

if pairs:
    print("Yes", pairs)
else:
    print("Pair not found")



