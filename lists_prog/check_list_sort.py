# Check whether the list is sorted or not 

n=int(input("Enter the size of list:"))
list1=[]
list2=[]
print("Enter the list Elements:")
for i in range(0,n):
    elem=input()
    list1.append(elem)
    list2.append(elem)
list1.sort()
if list1==list2:
    print("The given list is sorted")
else:
    print("The given list is not sorted and the sorted list is",list1)    