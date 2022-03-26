from random import *

a=0
b=0
c=0


com_a=randint(0,9)
com_b=randint(0,9)
com_c=randint(0,9)


strike=0
ball=0

count=10

while count!=0:

    a=int(input("첫번째:"))
    b=int(input("두번째:"))
    c=int(input("세번째:"))

    if a==com_a:
        strike=strike+1

    if a!=com_a:
        if com_b==a or com_c==a:
            ball=ball+1
#-------------------------------------------------------------

    if b==com_b:
        strike=strike+1

    if b!=com_b:
        if com_a==b or com_c==b:
            ball=ball+1
#-------------------------------------------------------------------------


    if c==com_c:
        strike=strike+1

    if c!=com_c:
        if com_b==c or com_c==c:
            ball=ball+1

    print("%d strike %d ball"%(strike,ball))
    if strike==3:
        print("승리!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        break
    
    count=count-1
    strike=0
    ball=0

if count==0:
    print("패배")
