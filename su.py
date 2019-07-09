ju=int(input())
if ju > 1:
    for dj in range(2,ju):
        if(ju%dj==0):
            print('no')
            break
    else:
            print('yes')
else:
            print('no')
