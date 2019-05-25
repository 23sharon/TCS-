assignment 50 day 7


#PF-Assgn-50

def sms_encoding(data):
    #start writing your code here
    s=data.split()
    for i,x in  enumerate(s):
        if not all(y in 'aeiou' for y in x.lower()):
            s[i]=''.join([y for y in x if y.lower() not in'aeiou'])
    return ' '.join(s)
    
data="I love Python"
print(sms_encoding(data))




*************DAY 9**********

assign 58


def check_prime(number):
    return number > 1 and all(number % i != 0 for i in range(2, number))
    
def rotations(num):
    rotated = []
    m = str(num)
    for i in m:
        rotated.append(int(m))
        m = m[1:] + m[0]
    return rotated

def get_circular_prime_count(limit):
    counter = 0 

    for number in range(1, limit):
        if all(check_prime(number) for number in rotations(number)): 
            counter += 1 
    return counter
#Provide different values for limit and test your program
print(get_circular_prime_count(1000))


assign***59 simple...

number=int(input(""))
s=0
for i in range(1,number):
    if(number%i==0):
        s=s+i
if(s==number):
    print("perfect number")
else:
    print("not a perfect number")


assignment*****************59************

def check_perfect_number(number):
    #start writing your code here
    r=number
    s=0
   
    for i in range(1,r):
        if(r%i==0):
            s+=i
    if(s==r):
        return True
    else:
        return False


def check_perfectno_from_list(no_list):
    #start writing your code here
    l=[]
    for i in range(0,len(no_list)):
        if no_list[i]!=0 and check_perfect_number(no_list[i])==True:
            l.append(no_list[i])
        else:
            continue
    return l
            
perfectno_list=check_perfectno_from_list([18,6,4,2,1,28])
print(perfectno_list)


#PF-Assgn-60*********************************
from collections import OrderedDict
def remove_duplicates(value):
    #start writing your code here
    return"".join(OrderedDict.fromkeys(value))

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))











