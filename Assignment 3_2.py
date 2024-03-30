numbers = []
while True :
    x = input("enter your numbers in order, when finished enter finish: ")
    if x != "finish":
        numbers.append(x)
    if x == "finish" :
        break

if numbers == sorted(numbers):
    print ("Numbers are in order!")
else:
    print("Numbers aren't in order")
    
