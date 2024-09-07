#One of the easiest methods to determine whether a number is prime is to divide
# it by integers from 2 up to the square root of the number.
# If none of these divisions results in an integer, then the number is prime.

def is_num_prime(num):
    if  num <= 1:
        return False
    for i in range(2, int(num**0.5) +1):
        if num % i == 0:
            return False
    else:
            return True

number=int(input(f"Please enter a number : "))
result=is_num_prime(number)
if result:
    print(f"This number {number} is Prime number")
else:
    print(f"This number {number} is Not Prime number")
