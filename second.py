# import random
# import string
#
# # ამოცანა 4
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
# # ამოცანა 5
# strs = input("შემოიყვანე სიტყვა: ")
# while strs.count(" ")!=0:
#     strs = input("შემოიყვანე მხოლოდ ერთი სიტყვა: ")
#
# mylist = list(strs)
# for i in range(5):
#     new = "".join(random.sample(mylist,k=len(mylist)))
#     print(new)
#
# # ამოცანა 6
# st = set()
# while True:
#     strs = input("შემოიყვანე რიცხვი:")
#     newlist = strs.split()
#
#     for i in range(len(newlist)):
#         st.add(int(newlist[i]))
#
#     mylist = list(st)
#     mylist = sorted(mylist)
#
#     r_mylist = mylist.copy()
#     r_mylist.reverse()
#
#     rand_mylist = random.sample(mylist,k=len(mylist))
#     q = input("როგორ გსურთ რომ დავასორტიროთ? (კლებადობით/ზრდადობით/რანდომად): ")
#
#     if q == "ზრდადობით":
#         print(st)
#     elif q == "კლებადობით":
#         print(r_mylist)
#     else:
#         print(rand_mylist)

