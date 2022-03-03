# Program to return prime numbers between 2 and 100
# Author: Éilis Sutton

primes = []
upto = 100

for candidate in range(2, upto):   # could put (2, 100) here but better to put 100 in as a variable insead
    #print (candidate)
    # assume that it's a prime
    isPrime = True   
    # only need to check if divisable by prime                   
    for divisor in range(2, candidate):      # range(2, candidate)-> switch to primes to speed up (Will only check primes
        # if divisible by an int it is not a prime number
        if(candidate % divisor == 0):
            isPrime = False
            # so there is no reason to keep checking
            break    
    if isPrime:                   # This will allow the program to jump out of the preceeding for loop
        primes.append(candidate)            # This appends the candidate (prime numbers) into the primes list

print (primes)