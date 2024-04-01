first_number = int(input("Enter first number: "))
second_number = int(input("enter second number: "))

for i in range (1 , (min(first_number, second_number)+ 1)):
    if first_number % i == 0 and second_number % i == 0:
        gcd = i

print("gcd =", gcd )

