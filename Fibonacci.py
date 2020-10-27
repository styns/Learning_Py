
for i in range(1, 16):
        if i%3 == 0 and i%5 == 0:
            print('FizzBuZZ')
        else:
            if i%3==0:
                print('Fizz')
            else:
                if i%5 == 0:
                    print('Buzz')
                print(i)

F = 3 #Fizz divider
B = 5 #Buzz divider
for i in range(1,16):
    print ('Fizz'*(i%F<1)+(i%B<1)*'Buzz' or i)

def Fizz_Buzz(input):
    if (input%3==0 and input%5==0):
        return ('fizzbuzz')
    if input%3==0:
        return('Fizz')
    if input%5==0:
        return('Buzz')
    return input

for i in range(1,101):
    print(Fizz_Buzz(i))

def seven_add(n):
    return n+7
numbers = range(1,16)
for n in numbers:
    print(seven_add(n))

F = 3
B = 5
Numbers = range(1,100,1)
def function(n):
    if n%F==0 and n%B==0:
        return 'Fizz_Buzz'
    if n%F==0:
        return 'Fizz'
    if n%B==0:
        return 'Buzz'
    return n

Result = list(map(function, Numbers))
print(Result)