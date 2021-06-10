'''Write a Python program to compute the sum of digits of each number of a given list. 
Original list:
[10, 2, 56]
Sum of digits of each number of the said list of integers:
14
Original list:
[10, 20, 4, 5, 'b', 70, 'a']
Sum of digits of each number of the said list of integers:
19
Original list:
[10, 20, -4, 5, -70]
Sum of digits of each number of the said list of integers:
19
'''

list1=[10, 20, 4, 5, 'b', 70, 'a']
sum=0
for i in range(0,len(list1)):
    if type(list1[i])==str:
        continue
    if type(list1[i])==int:
        if list1[i]<0:
            list1[i]=(-list1[i])
        while(list1[i]>0):
            if list1[i]>=10:
                temp=list1[i]%10
            else:
                temp=list1[i]    
            sum+=temp 
            list1[i]//=10           
print(sum)