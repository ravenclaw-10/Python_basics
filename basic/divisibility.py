'''Write a program to make a list of all such numbers which are divisible by 7 but are not a multiple of 
5, between 2000 and 3200 (both included). The final list should be printed as a comma-separated 
sequence on a single line.'''

lst=[]
for x in range(2000,3201):
    if x%7==0:
        if x%5!=0:
           lst.append(x) 
        else:
            continue;    
    else:
        continue;        
print(lst)        