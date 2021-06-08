#frequency of element

n=int(input("Enter the number of elements in the list="))
list1=[]
list2=[]
count=1
counted=-1
print("Enter the elements:")
for i in range(0,n):
    elem=input()
    list1.append(elem)
list1.sort() 
dist_elem=len(set(list1))
list(list1)
for i in range(0,n):
    for j in range(i+1,n):
        if list1[i]==list1[j] and list1[i]!=counted:
            count+=1
            list1[j]=counted 
        else:
            continue           
    if list1[i]!=counted:
        list2.append(count)
    count=1
print(list2)    




