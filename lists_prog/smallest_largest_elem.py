#Python program to find the smallest and largest number

n=int(input("Enter the no. of elements of list="))
list1=[]
print("Enter the values of list=",end='')
for i in range(0,n):
    elem=input()
    list1.append(elem)
list1.sort()
print("Smallest Element={} and Largest Element={}".format(list1[0],list1[-1]))    