for i in range(1, 16):
        if i%3 == 0:
            print('Fizz')
        else:
            if i%5 == 0 and i%3==0:
                print('FizzBuzz')
            else:
                if i%5 == 0:
                    print('buzz')
            print(i)
