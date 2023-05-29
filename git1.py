from array import *

array = list(map(int, input("enter the number:").split())) #enter numnber in array

print(array)        #prints the elements of an array
print(len(array))   #display the length of an array

if (len(array)<5):
    num=list(map(int, input("enter the number:").strip().split()))
    array.extend(num)
    if len(array)<5:
        num = list(map(int, input("enter the number:").strip().split()))
        array.extend(num)

else:
    print("original input is:",array)

duplicate=[*set(array)]
print("the highest number is:",max(array)) #maximum value

print("unique inputs:",duplicate)
print("the sorted number is:",sorted(duplicate))#sorted

