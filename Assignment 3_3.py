numbers = []
while True :
    x = input("enter your numbers in order, when finished enter finish: ")
    if x != "finish":
        numbers.append(x)
    if x == "finish" :
        break
print(numbers)

