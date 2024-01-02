def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i ==0:
            is_prime =False
            break
    if is_prime:
            print("its a prime number")
    else: print("this is not a prime number")

n= int(input("put in a number to check: "))
prime_checker(number=n)
