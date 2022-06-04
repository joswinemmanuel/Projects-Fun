'''A game of tic-tac-toe'''

import random
name=input('Enter your name:')
print()
a=[' ',' ',' ']
b=[' ',' ',' ']
c=[' ',' ',' ']  
print(a)
print(b)
print(c)
print()
print("Let's begin!")
print()
p_t=input('Choose X or O:').upper()
if p_t=='X':
    c_t='O'
else:
    c_t='X'
print()

l=list(range(1,10))
while True:
    if ' ' not in a and ' ' not in b and ' ' not in c:
        print('OUT OF CHOICES......Better luck next time!!')
        break
    else:          
        p_p=int(input('Position to mark:'))
        if p_p in [1,2,3]:
            a[p_p-1]=p_t
        elif p_p in [4,5,6]:
            b[p_p-4]=p_t
        else:
            c[p_p-7]=p_t
        print()
        print(a)
        print(b)
        print(c)
        print()
        l.remove(p_p)
        try:
            c_p=random.choice(l)
        except:
            print('OUT OF CHOICES.....Better luck next time!!')
            break
        l.remove(c_p)
        print('Computer chose',c_p)
        if c_p in [1,2,3]:
            a[c_p-1]=c_t
        elif c_p in [4,5,6]:
            b[c_p-4]=c_t
        else:
            c[c_p-7]=c_t
        print()
        print(a)
        print(b)
        print(c)
        print()
        if a[0]==a[1]==a[2]==p_t:
            print(name,'won. WOOOOW GREAT GAME!!!')
            break
        elif b[0]==b[1]==b[2]==p_t:
            print(name,'won. WOOOOW GREAT GAME!!!')
            break
        elif c[0]==c[1]==c[2]==p_t:
            print(name,'won. WOOOOW GREAT GAME!!!')
            break
        elif a[0]==b[0]==c[0]==p_t:
            print(name,'won. WOOOOW GREAT GAME!!!')
            break
        elif a[1]==b[1]==c[1]==p_t:
            print(name,'won. WOOOOW GREAT GAME!!!')
            break
        elif a[2]==b[2]==c[2]==p_t:
            print(name,'won. WOOOOW GREAT GAME!!!')
            break
        elif a[0]==b[1]==c[2]==p_t:
            print(name,'won. WOOOOW GREAT GAME!!!')
            break
        elif c[0]==b[1]==a[2]==p_t:
            print(name,'won. WOOOOW GREAT GAME!!!')
            break
        elif a[0]==a[1]==a[2]==c_t:
            print('Computer won...SORRY BETTER LUCK NEXT TIME')
            break
        elif b[0]==b[1]==b[2]==c_t:
            print('Computer won...SORRY BETTER LUCK NEXT TIME')
            break
        elif c[0]==c[1]==c[2]==c_t:
            print('Computer won...SORRY BETTER LUCK NEXT TIME')
            break
        elif a[0]==b[0]==c[0]==c_t:
            print('Computer won...SORRY BETTER LUCK NEXT TIME')
            break
        elif a[1]==b[1]==c[1]==c_t:
            print('Computer won...SORRY BETTER LUCK NEXT TIME')
            break
        elif a[2]==b[2]==c[2]==c_t:
            print('Computer won...SORRY BETTER LUCK NEXT TIME')
            break
        elif a[0]==b[1]==c[2]==c_t:
            print('Computer won...SORRY BETTER LUCK NEXT TIME')
            break
        elif c[0]==b[1]==a[2]==c_t:
            print('Computer won...SORRY BETTER LUCK NEXT TIME')
            break

    
        
    
    
        
        
            
        
    















