for num in range(30):
    num += 1
    if num % 3 == 0:
        if num % 5 == 0:
            print('Fizz Buzz')
        else:
            print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
