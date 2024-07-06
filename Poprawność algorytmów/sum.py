""" Specification and algorithm correctness proof.
# Specification:

    Name and arguments: sum_array(array, length)

    Initial condition: 
        array - an array of integers.
        length - a natural number representing the declared length of the array.

    Final condition: 
        The algorithm should return an integer
        that is the sum of the elements of this array,
        or zero if the array is empty.


# Algorithm correctness:

    Termination property:
        - The algorithm will terminate whenever i >= length.
        - length is a constant and finite natural number.
        - The variable i increments by 1 in each iteration.

    Partial correctness:
        - Invariant: (∀0≤j<i x ≥ Arr[j]) ∧ (∃0≤j<len(x == Arr[j]))
        - If it was true in iteration i 
          it will be true after iteration i 
          due to the conditional update of variable x in the 'if' statement
        - The invariant is also true just before the first iteration of the loop 
          so it will be true after any number of iterations.
"""

def sum_array(array: list[int], len: int) -> int:
    """
    Return the sum of numbers in the given array.

    Args:
        array (list[int]): array of integers.
        length (int): a natural number representing the declared length of the array.

    Returns:
        The sum of the elements of 'array'.
        If 'array' is empty or 'length' is 0, returns 0.
    """
    
    sum: int = 0
    i: int = 0

    while i < len:
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
