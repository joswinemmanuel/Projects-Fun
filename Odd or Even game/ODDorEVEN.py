'''A game of classic odd or even cricket game palyed by kids'''

import random
import time
name=input('Enter your name : ')
time.sleep(1)
print()
p_c=input('Choose odd or even : ')
time.sleep(1)
print()
if p_c=='even':
    c_c='odd'
else:
    c_c='even'
print(name,'chose',p_c)
time.sleep(1)
print('Computer chose',c_c)
time.sleep(1)
print()
p_n=int(input('Choose a number between 1 and 10 : '))
time.sleep(1)
while p_n>10:
    p_n=int(input('Number should be between 1 and 10 : '))
c_n=random.choice(range(1,11))
print()
print(name,'chose',p_n)
time.sleep(.5)
print('Computer chose',c_n)
time.sleep(1)
print()
check=p_n+c_n
if check%2==0:
    w='even'
else:
    w='odd'
print(w,'won')
time.sleep(1)
if p_c==w:
    print(name,'won the toss')
    time.sleep(1)
    won=name
else:
    print('Computer won the toss')
    time.sleep(1)
    won='Computer'
print()

if won==name:
    p_cho=input('Choose bating or balling:')
    if p_cho=='bating':
        c_cho='balling'
    else:
        c_cho='bating'
else:
    c_cho=random.choice(['bating','balling'])
    print('Computer chose',c_cho)
    time.sleep(1)
    if c_cho=='bating':
        p_cho='balling'
    else:
        p_cho='bating'
print("It's",name,p_cho,'and Computer',c_cho)
time.sleep(1)
print()

p_score=0
c_score=0

if p_cho=='bating' or c_cho=='balling':
    while True:
        p_put=int(input('Choose number between 1 and 10:'))
        while p_put>10:
            p_put=int(input('Number should be between 1 and 10:'))            
        c_put=random.choice(range(1,11))
        print(name,':',p_put,'   Computer :',c_put)
        time.sleep(1)
        if p_put!=c_put:
            p_score+=p_put
            print(name,'-',p_score)
            time.sleep(1)
        else:
            print('OHHHH Nooo Compute took your wicket')
            time.sleep(1)
            print('Final score of',name,':',p_score)
            time.sleep(1)
            print()
            print("It's Computer's bating now")
            time.sleep(1)
            break
    while True:
        if c_score>p_score:
            break
        print()
        p_put=int(input('Choose number between 1 and 10:'))
        while p_put>10:
            p_put=int(input('Number should be between 1 and 10:'))
        c_put=random.choice(range(1,11))
        print('Computer :',c_put,'  ',name,':',p_put)
        time.sleep(1)
        if p_put!=c_put:
            c_score+=c_put
            print('Computer -',c_score)
            time.sleep(1)
        else:
            print(name,"took Computer's wicket..GOOD JOB")
            time.sleep(1)
            print('Final score of computer :',c_score)
            time.sleep(1)
            break
    print()
    if p_score>c_score:
        print(name,'you WON THE GAME by',abs(p_score-c_score),'runs !!!!! WELL DONE......GREAT GAME')
        time.sleep(1)
    elif c_score>p_score:
        print('SORRY!! Computer won the game by',abs(p_score-c_score),'runs ...good luck next....anyway great game')
        time.sleep(1)
    else:
        print("WOOOW it's a tie....GREAT GAME...try again later")
        time.sleep(1)
else:
    print('Computer is bating now....Beat him!!!')
    time.sleep(1)
    while True:        
        print()
        p_put=int(input('Choose number between 1 and 10:'))
        while p_put>10:
            p_put=int(input('Number should be between 1 and 10:'))
        c_put=random.choice(range(1,11))
        print('Computer :',c_put,'  ',name,':',p_put)
        time.sleep(1)
        if p_put!=c_put:
            c_score+=c_put
            print('Computer -',c_score)
            time.sleep(1)
        else:
            print(name,"took Computer's wicket..GOOD JOB")
            time.sleep(1)
            print('Final score of computer :',c_score)
            time.sleep(1)
            print()
            print("It's your turn outscore him to win")
            time.sleep(1)
            break
    while True:
        if p_score>c_score:
            break
        print()
        p_put=int(input('Choose number between 1 and 10:'))
        while p_put>10:
            p_put=int(input('Number should be between 1 and 10:'))
        c_put=random.choice(range(1,11))
        print(name,':',p_put,'   Computer :',c_put)
        time.sleep(1)
        if p_put!=c_put:
            p_score+=p_put
            print(name,'-',p_score)
            time.sleep(1)
        else:
            print('OHHHH Nooo Computer took your wicket')
            time.sleep(1)
            print('Final score of',name,':',p_score)
            time.sleep(1)
            break
    print()
    if p_score>c_score:
        print(name,'you WON THE GAME by',abs(p_score-c_score),'runs !!!!! WELL DONE......GREAT GAME')
        time.sleep(1)
    elif c_score>p_score:
        time.sleep(1)
        print('SORRY!! Computer won the game by',abs(p_score-c_score),'runs ...good luck next....anyway great game')
    else:
        time.sleep(1)
        print("WOOOW it's a tie....GREAT GAME...try again later")
    

    
    
        
        
            
        
    















