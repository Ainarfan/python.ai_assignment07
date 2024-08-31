def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    name = input("Enter your name: ")
    num1 = int(input("Enter your first favorite number: "))
    num2 = int(input("Enter your second favorite number: "))
    num3 = int(input("Enter your third favorite number: "))

    # Store the numbers in a list
    numbers = [num1, num2, num3]

    # Greet the user
    print(f"\nHello, {name}! Let's explore the numbers you provided.")

    # Check if each number is even or odd
    even_odd_tuples = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]
    for num, eo in even_odd_tuples:
        print(f"The number {num} is {eo}.")

    # Create tuples with the number and its square
    squares = [(num, num**2) for num in numbers]
    for num, square in squares:
        print(f"The number {num} and its square are: {square}.")

    # Calculate the sum of the numbers
    total_sum = sum(numbers)
    print(f"\nAmazing! The sum of your numbers is: {total_sum}")

    # Check if the sum is a prime number
    if is_prime(total_sum):
        print("Wow! The sum is a prime number.")
    else:
        print("The sum is not a prime number.")

if __name__ == "__main__":
    main()