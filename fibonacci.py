# Fibonacci Sequence
# Wallis

def fibonacci(x):
    y = 0
    result = [0, 1]
    while y < x:
        z = result[y] + result[y + 1]
        y += 1
        result.append(z)
    return result


print('Fibonacci Sequence generator by Wallis')
while True:
    try:
        num = (int(input('Up to what number do you want the sequence to go?: ')))
        if num <= 0:
            print('Please input only positive integers')
            continue
        fibo = fibonacci(num)
        print(fibo[:num])
    except ValueError:
        print('The program only accepts integers as input')
        continue
