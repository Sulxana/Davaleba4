# import random
# import string
#
# ამოცანა 4
strs = input("შემოიყვანე სიტყვა/რიცხვი: ")
r_str = strs[::-1]
if strs == r_str:
    print(True)
else:
    chance = True
    can = True
    mylist = list(strs)
    left = 0
    right = len(mylist)-1
    while left < right:
        if mylist[left] != mylist[-(left+1)] and chance:
            del mylist[right]
            chance = False
            continue
        elif mylist[left] != mylist[-(left+1)]:
            print("imposibble")
            can = False
            break
        left+=1
        right-=1
    if can:
        print("".join(mylist))


