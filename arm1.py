n=int(input(" "))
r=0
s=0
while n>0:
    r=n%10
    s=s+r**3
    n=n//10
print(s)



method 2


n=input(" ")
d=len(n)
h=int(n)
t=h
s=0
while h>0:
    r=h%10
    s=s+r**3
    h=h//10
if t==s:
    print("Armstrong number")
else:
    print("not a Armstrong numnber")

