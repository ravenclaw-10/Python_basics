# Element with maximum occurence in a list=[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2] .
#Python program to check if the elements of a given list are unique or not.

n=int(input("Enter the no. of element in the list(size):"))
list1=[]
count=0
max=0
print("Enter the elements of the lists:")
for i in range(0,n):
    elem=input()
    list1.append(elem)
max_elem=list1[0]    
for i in range(0,n):
    count=0
    for j in range(0,n):
        if list1[i]==list1[j]:
            count+=1
    if max<=count:
        max=count
        max_elem=list1[i] 
if max==1:
    print("The given list have unique elements")
else:
    print("Maximum occered element:",max_elem)        