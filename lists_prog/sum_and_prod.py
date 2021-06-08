'''1. Write a Python program to sum all the items in a list. 

2. Write a Python program to multiplies all the items in a list. 

3. Write a Python program to get the largest number from a list. 

4. Write a Python program to get the smallest number from a list.'''


n=int(input("Enter the no. of elements in a list="))
list1=[]
sum=0
mult=1
print("Enter the elements of the list=",end="")
for i in range(0,n):
    elem=int(input())
    list1.append(elem)   
    sum+=elem
    mult*=elem
print("Sum={} \nProduct={} \nLargest Number={} \nSmallest Number={}".format(sum,mult,max(list1),min(list1)))

