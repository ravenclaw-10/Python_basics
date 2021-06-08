'''Write a Python program to generate and print a list of first and last 5 elements 
where the values are square of numbers between 1 and 30 (both included).'''

list1=[]
final_list=[]
for i in range(1,31):
    list1.append(i*i)
for i in range(0,5):
    elem1=list1[i]
    final_list.append(elem1)
for i in range(-1,-6,-1):
    elem2=list1[i]
    final_list.append(elem2)
print(final_list)    

