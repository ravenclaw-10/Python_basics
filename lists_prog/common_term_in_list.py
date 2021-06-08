'''Write a Python function that takes two lists and returns True if they have at least one common member. '''

n1=int(input("Enter the number of element in list 1="))
n2=int(input("Enter the number of element in list 2="))
list1=[]
list2=[]
flag=0
print("Enter the elements of  the list=")
for i in range(0,n1):
    elem1=input()
    list1.append(elem1)
print("Enter the elements of  the list=")
for i in range(0,n2):
    elem2=input()
    list2.append(elem2)
for i in range(0,n1):
    for j in range(0,n2):
        if list1[i]==list2[j]:
            flag=1
if flag==1:
    print("Yes there is a common element")
else:
    print("No there is not any similar element")    

