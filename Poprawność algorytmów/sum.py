from typing import Iterable

def sum(array: list[int], len: int) -> int:
    """
    Task:
        Return the sum of numbers in the given array 
        up to the specified len.

    Specification:
        Name and arguments: 
            sum(array, len)

        Initial condition: 
            array - an array of integers
            len - a natural number representing the declared len of the array

        Final condition: 
            The algorithm should return an integer
            that is the sum of the first len elements of this array,
            or zero if the array is empty.

    Algorithm correctness:
        Termination property:
            - The algorithm will terminate whenever i >= len.
            - len is a constant and finite natural number.
            - The variable i increments by 1 in each iteration.

        Partial correctness:
            - Invariant: the sum variable correctly accumulates the sum of the elements 
              in the array up to the current index.
            - If it was true in iteration i, it will be true after iteration i due to 
              the unconditional update of the sum variable.
            - The invariant is also true just before the first iteration of the loop 
              so it will be true after any number of iterations.
    
    Returns:
        The sum of the first 'len' elements of 'array'.
        If 'array' is empty or 'len' is 0, returns 0.
    """
    sum: int = 0
    i: int = 0

    while i < len and i < len(array):
        sum += array[i]
        i += 1

    return sum

def main() -> None:
    array1: list[int] = [1, 2, 3]
    array2: tuple[int] = (4, 5, 6)
    array3: set[int] = {7, 8, 9}
    
    print(sum(array1, len(array1)))
    print(sum(array2, 2))
    print(sum(array3, len(array3)))

if __name__ == "__main__":
    main()
