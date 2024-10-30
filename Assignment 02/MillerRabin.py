# Write a Python program which will test if the given number is a prime number or no.
# In order to achieve this you have to implement the Miller-Rabin Algorithm as shown below
# TEST (n)

# 1. Find integers k, g, with k>0, g odd, so that (n - 1 = 2^k q) ;
# 2. Select a random integer a, 1<a<n- 1;
# 3. if amod n = 1 then return ("inconclusive") ;
# 4. for j= 0 to k - 1 do
# 5. if a^q mod n= n - 1 then return ("inconclusive") ;
# 6. return ("composite") ;

import random


def millerRabin(n, trials=5):

    # Check for base cases (easy solutions)
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # # Decompose n - 1 into the form 2^k * q
    k, q = 0, n - 1

    while q % 2 == 0:
        k += 1
        q //= 2  # floor out q

    # Miller-Rabin Algorithm
    for _ in range(trials):

        # Select a random integer 'a' in the range (2, n-2)
        a = random.randint(2, n - 2)

        # Compute x = a^q mod n
        x = pow(a, q, n)

        # Check if x is equal to 1 or n-1 (inconclusive)
        if x == 1 or x == n - 1:
            continue

        # Repeat squaring for k-1 times
        for _ in range(k - 1):
            x = pow(x, 2, n)

            # If x is congruent to n-1, break the loop (inconclusive)
            if x == n - 1:
                break
        else:
            return False  # Composite

    return True  # Inconclusive


# Test the function
input = int(input("Enter a number to test for primality: "))
result = millerRabin(input)

if result:
    print(f"{input} is inconclusive, it may be prime.")
else:
    print(f"{input} is not a prime number")
