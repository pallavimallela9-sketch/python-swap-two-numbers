# Program: Swap Two Numbers
# Author: M.Pallavi

def swap_numbers():
    print("================================")
    print("       SWAP TWO NUMBERS")
    print("================================")

    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        print("\nBefore Swapping:")
        print("First Number  :", num1)
        print("Second Number :", num2)

        # Swapping without using a third variable
        num1, num2 = num2, num1

        print("\nAfter Swapping:")
        print("First Number  :", num1)
        print("Second Number :", num2)

    except ValueError:
        print("\nInvalid input!")
        print("Please enter valid integer numbers.")


if __name__ == "__main__":
    swap_numbers()
