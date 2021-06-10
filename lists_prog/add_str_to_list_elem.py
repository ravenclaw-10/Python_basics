'''Write a Python program to insert a given string at the beginning of all items in a list. 
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
'''

list1=[1,2,3,4]
list2=[]
string='emp'
for i in range(0,len(list1)):
    str1=str(list1[i])
    elem=string+str1
    list2.append(elem)
print(list2)    
