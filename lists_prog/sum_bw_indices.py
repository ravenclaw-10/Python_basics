n=int(input("Enter the size of list:"))
list1=[]
sum=0
print("Enter the elements of the lists:")
for i in range(0,n):
    elem=int(input())
    list1.append(elem)
start=int(input("Enter the starting index:"))
stop=int(input("Enter the ending index:"))
for i in range(start,stop+1):
    sum+=list1[i]
print("Sum=",sum)        