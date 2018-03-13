name = str(input("Enter name"))
if name == "":
    print("You cannot leave your name blank")
    name = input("Enter name")
for i in range(1, 2, len(name)):
    print(name(i))
