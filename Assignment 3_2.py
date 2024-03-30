import random

n = random.randint(1, 100)

numbers = []
for i in range(n):
    x = random.randint(0, 100)
    if x not in numbers:
        numbers.append (x)
    
print(numbers)
