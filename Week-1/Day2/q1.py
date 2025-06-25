items = []
while True:
    item = input("Enter Item or Enter Done to exit")
    if item == "done":
        break
    items.append(item)
for i in items:
    print(i, end = " ")