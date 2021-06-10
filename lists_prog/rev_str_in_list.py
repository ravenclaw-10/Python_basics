'''Write a Python program to reverse strings in a given list of string values. 
Original lists:
['Red', 'Green', 'Blue', 'White', 'Black']
Reverse strings of the said given list:
['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
'''

list1=['Red', 'Green', 'Blue', 'White', 'Black']
list2=[]
for i in list1:
    string="".join(reversed(i))
    list2.append(string)
print(list2)    