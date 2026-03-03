# Example 3: Using the walrus operator in a list comprehension
squared_numbers = [x**2 for x in range(10) if (square := x**2) > 10]
print(squared_numbers)  # Output: [16, 25, 36, 49, 64, 81,]

# Example 4: Using the walrus operator in a while loop
n = 0
while (n := n + 1) < 10:
    print(n)  # Output: 1, 2, 3, 4, 5, 6, 7, 8, 9

from typing import List, Tuple , Dict
# Example 5: Using type hints with the walrus operator
def process_numbers(numbers: List[int]) -> Tuple[List[int], Dict[int, int]]:
    squared = []
    squares_dict = {}
    for num in numbers:
        if (square := num ** 2) > 10:
            squared.append(square)
            squares_dict[num] = square
    return squared, squares_dict
process_numbers([1, 2, 3, 4, 5]) # Output: ([16, 25], {4: 16, 5: 25})
