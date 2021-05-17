num=int(input("Enter the number:-"))
count=0
arm_num=0
check=num
temp=num
while(temp):
    count+=1
    temp//=10
while(num):
    lst_dig=num%10
    num//=10
    arm_num+=lst_dig**count
arm_num+=num**count
if arm_num==check:
    print("Armstrong number")
else:
    print("Not an Armstring number")    