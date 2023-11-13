import math 
n=eval(input("Dati  n:"))
s1=0
s2=0
s3=0
s4=0
i=1
while i<=n:
    s1+=pow(i,3)
    s2+=i
    s3+=pow(i,2)
    i+=1
s3=3*s3
s4=pow(n,3)+pow(n,2)+s2
print("s1 =",s1)
print("s2 =",s2)
print("s3 =",s3)
print("s4 =",s4)
