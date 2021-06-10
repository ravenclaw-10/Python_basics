'''Write a Python program to sort a given mixed list of integers and strings. Numbers must be sorted before strings. 
Original list:
[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
Sort the said mixed list of integers and strings:
[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
'''

list1=[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
list2=[]
list3=[]
for i in list1:
    elem=i
    if type(i)==int:
        list2.append(elem)
    elif type(i)==str:
        list3.append(elem)    
list2.sort()
list3.sort()    
print(list2+list3)