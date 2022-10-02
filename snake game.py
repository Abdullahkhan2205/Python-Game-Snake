import random
Number_of_Attempt=0
com_point=0
plyr_point=0
while Number_of_Attempt<10:
    Number_of_Attempt+=1
    Number_of_Attempt_Left = 10-Number_of_Attempt
    ply=input('Enter Answer:s,w,g\n')
    com = ['s','w','g']
    com_Ans = random.choice(com)
    if ply==com_Ans:
        print(f'player got 0 & com got 0, com answer is {com_Ans},plyr point is {plyr_point},com point is {com_point}')
    elif ply=='s'and com_Ans=='g':
        com_point+=1
        print(f'com got 1 , com answer is {com_Ans},plyr point is {plyr_point},com point is {com_point}')
    elif ply=='w'and com_Ans=='g':
        plyr_point+=1
        print(f'Player got 1, com answer is {com_Ans},plyr point is {plyr_point},com point is {com_point}')
    elif ply=='g'and com_Ans=='s':
        plyr_point += 1
        print(f'Player got 1, com answer is {com_Ans},plyr point is {plyr_point},com point is {com_point}')
    elif ply=='w'and com_Ans=='s':
        com_point += 1
        print(f'com got 1, com answer is {com_Ans},plyr point is {plyr_point},com point is {com_point}')
    elif ply=='s'and com_Ans=='w':
        plyr_point += 1
        print(f'Player got 1, com answer is {com_Ans},plyr point is {plyr_point},com point is {com_point}')
    elif ply=='g'and com_Ans=='w':
        com_point += 1
        print(f'com got 1, com answer is {com_Ans},plyr point is {plyr_point},com point is {com_point}')
    else:
        print('You have Entered Wrong entry')

    print(f'Number of attempt left {Number_of_Attempt_Left}')

if com_point>plyr_point:
    print('You Lose')
elif com_point<plyr_point:
    print('You win')
else:
    print('Tied')
