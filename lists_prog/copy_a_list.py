n=int(input("Enter the number of elements of list="))
list1=[]
list2=[]
print("Enter the elements of the list=",end='')
for i in range(0,n):
    elem=input()
    list1.append(elem)
for i in range(0,n):
    elem2=list1[i]
    list2.append(elem2)
print("Copied list= {}".format(list2))    
        