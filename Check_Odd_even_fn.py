def check_even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

number = int(input("Enter the number "))
result = check_even_odd(number)
print("Result is: ", result)
print(f"The number {number} is {result}")