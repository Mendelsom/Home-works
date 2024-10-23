numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
is_prime = True
non_primes = []
primes = numbers
primes.remove(1)
for i in range(3,16):
    for j in range(2,i):
        if i % j == 0:
            non_primes.append(i)
            primes.remove(i)
            break
print('Primes: ', primes)
print('Not primes: ', non_primes)




