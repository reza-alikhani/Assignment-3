first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

for i in range (max(first_number, second_number), 1 + (first_number * second_number)) :
    if i % first_number == i % second_number == 0:
        lcm = i  
        break

print("lcm =", lcm)

