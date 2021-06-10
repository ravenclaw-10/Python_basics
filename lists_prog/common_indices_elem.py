'''Write a Python program to extract common index elements from more than one given list. 
Original lists:
[1, 1, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 7]
[0, 1, 2, 3, 4, 5, 7]
Common index elements of the said lists:
[1, 7]
'''


list1=[1,1,3,4,5,6,7]
list2=[0,1,2,3,4,5,7]
list3=[0,1,2,3,4,5,7]
list4=[]
for i in range(0,len(list1)):
    for j in range(0,len(list2)):
        for k in range(0,len(list3)):
            if i==j==k and list1[i]==list2[j]==list3[k]:
                list4.append(list1[i])
print(list4)                