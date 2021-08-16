# Print personality acording to your blood type
dict1 = {"A":"有趣","B":"無聊","O":"果斷","AB":"天真"}
bloodtype = input("輸入血型: ").upper()

if bloodtype == "A":
   print(dict1["A"])
elif bloodtype == "B":
   print(dict1["B"])
elif bloodtype == "O":
   print(dict1["O"])
elif bloodtype == "AB":
   print(dict1["AB"])
else:
   print("沒有此血型")
