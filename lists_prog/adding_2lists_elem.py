'''Write a Python program to add two given lists of different lengths, start from left. 
Original lists:
[2, 4, 7, 0, 5, 8]
[3, 3, -1, 7]
Add said two lists from left:
[5, 7, 6, 7, 5, 8]
'''

list1=[2,4,7,0,5,8]
list2=[3,3,-1,7]
if len(list1)>=len(list2):
    for i in range(0,len(list2)):
        list1[i]+=list2[i]
    print("Resulted List=",list1)    
else:
    for i in range(0,len(list1)):
        list2[i]+=list1[i]
    print("Resulted List=",list2)    