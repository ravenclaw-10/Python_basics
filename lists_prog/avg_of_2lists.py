'''Write a Python program to compute average of two given lists. 
Original list:
[1, 1, 3, 4, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 4, 5, 7, 8]
Average of two lists:
3.823529411764706
'''

list1=[1,1,3,4,4,5,6,7]
list2=[0,1,2,3,4,4,5,7,8]
sum=0
for i in list1:
    sum+=i
for i in list2:
    sum+=i
avg=sum/(len(list1)+len(list2))      
print(avg)  