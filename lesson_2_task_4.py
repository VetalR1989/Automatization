#Напишите функцию fizz_buzz, которая принимает один аргумент — n (число).
#Функция должна печатать числа от 1 до n. При этом:
#    1. если число делится на 3, печатать `Fizz`;
#    2. если число делится на 5, печатать `Buzz`;
#    3. если число делится на 3 и на 5, печатать `FizzBuzz`.

def fizz_buzz(num):
    for n in range(1, num + 1):
        if (n % 3 == 0) and (n % 5 == 0):
            print('FizzBuzz')
        else:
            if (n % 5 == 0):
                print('Buzz')
            else:
                if (n % 3 == 0):
                     print('Fizz')
                else:
                    print(n)
                
fizz_buzz(48)
            