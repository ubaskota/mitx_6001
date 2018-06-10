def genPrimes():
    primes = []   
    new = 1      
    while True:
        new += 1
        for i in primes:
            if new % i == 0:
                break
        else:
            primes.append(new)
            yield new
            
genPrimes().__next__()
