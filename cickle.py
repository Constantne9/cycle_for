print('поиск простых и составных положительных чисел')
number = int(input('введите число: '))
number += 1
numbers = []
for i in range(1, number):
    numbers.append(i)
print(f'диапазон поиска:{numbers}')
primes = []
not_primes = []
for i in numbers:
    is_prime = True
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print(f'простые:{len(primes)} шт. {primes}')
print(f'составные:{len(not_primes)} шт. {not_primes}')
