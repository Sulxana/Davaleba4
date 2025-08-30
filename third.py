# # ამოცანა 7
# #
# strs = input("შეიყვანე ტექსტი: ")
# mylist = []
# for s in strs:
#     if s.isalpha() or s.isspace():
#         mylist.append(s)
# print("".join(mylist))
#
# # ზუსტად იგივე ლოგიკაა უბრალოდ თავიდან ესე გავაკეთე ლისტებად შემოვიტანე და მერე მივხვდები რო პირდაპირ შემეძლო
#
# strs = list(input("შეიყვანე ტექსტი: "))
# mylist = []
# for i in range(len(strs)):
#     if strs[i].isalpha() or strs[i].isspace():
#         mylist.append(strs[i])
# print("".join(mylist))
#
# # ამოცანა 8
# strs = input("შემოიტანეთ სია: ")
# mylist = strs.split()
# mylist = [int(s) for s in mylist]
#
# for i in range(len(mylist)-1):
#     newlist = []
#     for j in range(len(mylist)-1):
#         newlist.append(mylist[j]+mylist[j+1])
#     mylist = newlist
#     print(newlist)
#
# # ამოცანა 9
# strs = input("შეიყვანე ტექსტი:").lower()
# mylist = strs.split()
# word = []
# mx = 0
#
# for s in mylist:
#     total = mylist.count(s)
#
#     if total > mx:
#         mx = total
#         while word:
#             word.pop()
#         word.append(s)
#
#     elif total == mx and word.count(s)==0:
#         word.append(s)
# print(word)
#
# # ამოცანა 10
# strs = input("შეიყვანე წინადადება:")
# mylist = strs.split()
# mydict = {}
# for s in mylist:
#     mydict[s] = len(s)
# print(mydict)