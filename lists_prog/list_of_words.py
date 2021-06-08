'''Write a Python program to find the list of words that are longer than n from a given list of words. '''

n=int(input("Enter the number of words in the list="))
list1=[]
count=0
list2=[]
print("Enter the words=")
for i in range(0,n):
    elem=input()
    list1.append(elem)
length=int(input("Enter the mininmum length of words allowed="))
for i in range(0,n):
    if len(list1[i])>=length:
        wrd=list1[i]
        list2.append(wrd)
print("Words greater than the given length={}".format(list2))        