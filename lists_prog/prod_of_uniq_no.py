'''Write a Python program to calculate the product of the unique numbers of a given list. 
Original List : [10, 20, 30, 40, 20, 50, 60, 40]
Product of the unique numbers of the said list: 720000000
'''

list1=[10,20,30,40,20,50,60,40]
list2=list1
print(list2)
prod=1
for i in range(0,len(list1)):
    for j in range(0,len(list1)):
        if (list1[i]==list1[j]) and (i!=j):
            list1[j]=1
    prod*=list1[i]   
print("Product=",prod)            
print(list2)    
