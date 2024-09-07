# tell if a given number is prime number
# Prime number > 1 , divisible by itself only like 1, 2, 3, 5, 7, ..
n = int(input("Enter a number: "))

if n == 0 or n == 1:
    print(n, " It's not a prime number ")
elif n > 1:
    for i in range (2, n//2):
        if (n % i) == 0:
            print(n, "It's not a prime number")
            break
    else:
        print(n, "It's a prime number")

else:
    print("It's not a prime number")
