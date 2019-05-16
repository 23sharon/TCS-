	***"Armstrong number"***
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




	method 3
	***"Find armstrong in between 100 to 2000"***

l=100
u=2000
for i in range (l,u+1):
    d=len(str(i))
    s=0
    t=i
    while t>0:
        r=t%10
        s=s+r**d
        t=t//10
    if i==s:
        print(i) 


o/p
153
370
371
407
1634





	
	***"Palindrome"***
	method1
s="mda"
pr=1
for i in range(0,len(s)//2):
    if s[i]!=s[len(s)-i-1] :
        pr=0
    else:
        pr=1
print(pr)




	***"Reverse method"***

'''reverse a num'''
n=input(" ")
t=int(n)
r=0
while t>0:
    re=t%10
    r=r*10+re
    t=t//10
print(r)


n=input(" ")
print(n[::-1])



	***"Sum of Digits"***

n=input(" ")
t=int(n)
r=0
while t>0:
    re=t%10
    r=r+re
    t=t//10
print(r)


	***"Number of digits"***

n=input(" ")
t=int(n)
c=0
while t>0:
    t=t//10
    c=c+1
print(c)

	***"Factors printing factors"***

p=input(" ")
n=int(p)
c=0
for i in range(1,n+1):
    if n%i==0:
        print(i)
        
   ******"counting factors"******


p=input(" ")
n=int(p)
c=0
for i in range(1,n+1):
    if n%i==0:
        c=c+1
print(c)
    

   ***"multiplication"***

n=input(" ")
t=input(" ")
w=int(n)
j=int(t)
for i in range(1,j+1):
   print(w,'x',i,'=',w*i)

  method 2
for i in range(1,11):
    print("17","*",i,"=",1*i )




    ***"natural number printing"***

p=input(" ")
n=int(p)
s=0
s=(n*(n+1))//2
print(s)

	**"method2"***

for i in range(1,11):
    print("17","*",i,"=",1*i )


	**"Sum of natural numbers"***

p=input(" ")
n=int(p)
s=0
for i in range(1,n+1):
    s+=i
print(s)






