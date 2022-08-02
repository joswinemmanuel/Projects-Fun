''' A game of rock, paper and scissors aganist the computer '''

import random
import time
name=input('Player name : ')
print()
mark=int(input('Set the score limit to win : '))
print()
p_score=0
c_score=0

while True:
    if p_score==mark:
        print(name.upper(),'won the match!!!!!')
        print('CONGRATULATION!!!!')
        break
    elif c_score==mark:
        print('COMPUTER won the match!!!!!!')
        print('Better luck next time...',name.upper())
        break

    n=input('Rock, paper or scissors? : ').lower()
    while n not in ('rock','paper','scissors'):
        n=input('Choose rock, paper or scissors?? : ').lower()
    c=random.choice(['rock','paper','scissors'])
    print('Comptuer chose : ',c)
    time.sleep(1)

    if n==c:
        print("It's a tie!!!")
        time.sleep(1)
        print(name,':',p_score,'   ','Computer:',c_score)
        time.sleep(1)
    elif n=='paper':
        if c=='scissors':
            c_score+=1
            print('Computer scored')
            time.sleep(1)
            print(name,':',p_score,'   ','Computer:',c_score)
            time.sleep(1)
        else:
            p_score+=1
            print(name,'scored')
            time.sleep(1)
            print(name,':',p_score,'   ','Computer:',c_score)
            time.sleep(1)
    elif n=='rock':
        if c=='paper':
            c_score+=1
            print('Computer scored')
            time.sleep(1)
            print(name,':',p_score,'   ','Computer:',c_score)
            time.sleep(1)
        else:
            p_score+=1
            print(name,'scored')
            time.sleep(1)
            print(name,':',p_score,'   ','Computer:',c_score)
            time.sleep(1)
    elif n=='scissors':
        if c=='rock':
            c_score+=1
            print('Computer scored')
            time.sleep(1)
            print(name,':',p_score,'   ','Computer:',c_score)
            time.sleep(1)
        else:
            p_score+=1
            print(name,'scored')
            time.sleep(1)
            print(name,':',p_score,'   ','Computer:',c_score)
            time.sleep(1)
    else:
        break
    print()

    


    
