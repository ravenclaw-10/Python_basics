'''Write a Python program that accepts a hyphen separated sequence of words as input and prints the 
words in a hyphen-separated sequence after sorting them alphabetically. 
Sample Items: green-red-yellow-black-white
Expected Result: black-green-red-white-yellow'''

seq=input("Enter the sequence:-")
upd_seq=[]
splitted_seq=seq.split('-')
splitted_seq.sort()
for i in range(0,len(splitted_seq)):
    print(splitted_seq[i], end="-")