#Python program to add unique values into a list L2 from a list L1

n1=int(input("Enter the no. of elements in list1="))
n2=int(input("Enter the no. of elements in list2="))
list1=[]
list2=[]
flag=0
print("Enter the elements of list1=",end='')
for i in range(0,n1):
    elem1=input()
    list1.append(elem1)
print("Enter the elements of list2=",end='')   
for  i in range(0,n2)  :
    elem2=input()
    list2.append(elem2)
for i in list2:
    for j in list1:
        if i==j:
            flag=1
    if flag==0:
        list1.append(i) 
    flag=0           
print(list1)