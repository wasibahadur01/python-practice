# walrus operator :=
# The walrus operator allows you to assign values to variables as part of an expression.
# It is useful in situations where you want to use a value that is computed within an expression


if (n:=len([1, 2, 3, 4, 5]))  > 3:
    print(f"The list has ({n} elements  is les then >3.")


# This example reads lines from a file until it reaches the end of the file (EOF).
# Example 1: Using the walrus operator in a while loop
while (line := input("Enter a line (or 'exit' to quit): ")) != "exit":
    print(f"You entered: {line}")
