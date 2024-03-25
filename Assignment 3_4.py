n = int(input("enter your number"))

snake = []
for i in range (n) :
    if i % 2 == 0 :
        snake.append ("*")
        print (snake[i], end = "")
    else :
        snake.append ("#")
        print (snake[i], end = "")
