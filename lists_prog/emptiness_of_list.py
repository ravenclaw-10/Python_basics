n=int(input("Enter the number element of the list="))
list1=[]
print("Enter the elements=")
for i in range(0,n):
    elem=input()
    list1.append(elem)
if len(list1)==0:
    print("List is empty")
else:
    print("List is not empty")        

