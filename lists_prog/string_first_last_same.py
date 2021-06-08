'''Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''


list1=['abc','xyz','aba','1221']
list2=[]
for i in range(0,len(list1)):
        if list1[i][0]==list1[i][-1]:
            list2.append(list[i])
print(len(list2))