# for char in ("hello world"):
#     print(char)


password = "brodiewindle"
count = 0
count1 = 0
for char in password:
    if  char.islower():
        count = count + 1
    elif char.isupper():
        count1 = count1 + 1

if count1 == 0:
    print("hello")
else:
    print("goodbye")





print(count)
print(count1)