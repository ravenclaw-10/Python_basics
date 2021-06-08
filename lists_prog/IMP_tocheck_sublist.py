#Python program to check whether a list contains a sublist.

n=int(input("Enter the ni. of element in the list:"))
list1=[]
k=1
flag=0
print("Enter the element of the list:")
for i in range(0,n):
    elem=input()
    list1.append(elem)
n1=int(input("Enter the length of sublist:"))
sub_list=[]
print("Enter the element of sublist:")
for i in range(0,n1):
    elem1=input()
    sub_list.append(elem1)
for i in range(0,n):
    if list1[i]==sub_list[0] and i<=n-n1:
        for j in range(i+1,i+n1):
            if list1[j]==sub_list[k]:
                flag=1
            else:
                flag=2  
            k+=1   
    if n1==1:
        if sub_list[0]==list1[i]:
            flag=1               
if flag==1:
    print("Your given sublist is present in the list")
else:
    print("Your given sublist is not in the list")    
    




#code to find any list in a list but not working properly
'''
flag=0
for i in list1:
    if type(i)==list:
        print("Yes there is a sublist present in the list")
        flag=1
        break 
if flag==0:
    print("No there is not any sublist present in the list")
    
'''