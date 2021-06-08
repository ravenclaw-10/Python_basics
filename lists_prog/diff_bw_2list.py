#Python program to get the difference and Summition between the two lists

n1=int(input("Enter the no. of elements in list1="))
n2=int(input("Enter the no. of elements in list2="))
list1=[]
list2=[]
final_list=[]
diff_list=[]
flag=0
print("Enter the elements of list1=",end='')
for i in range(0,n1):
    elem1=input()
    list1.append(elem1)
print("Enter the elements of list2=",end='')   
for  i in range(0,n2)  :
    elem2=input()
    list2.append(elem2)

#Summition of list
    
final_list=list1+list2   

#Difference between lists

for i in list1:
    for j in list2:
        if i==j:
            flag=1
            list2.remove(j) 
    if flag==0:
        diff_list.append(i)    
diff_list=diff_list+list2
print("Difference between list={}".format(diff_list))
print("Addition of List={}".format(final_list))