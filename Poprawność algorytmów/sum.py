"""
# Task:
    Return the sum of numbers in the given sequence 
    up to the specified length.

# Specification:
    Name and arguments: 
        sum(sequence, length)

    Initial condition: 
        sequence - an iterable of integers
        length - a natural number representing the declared length of the sequence

    Final condition: 
        The algorithm should return an integer
        that is the sum of the first length elements of this sequence,
        or zero if the sequence is empty.


# Algorithm correctness:
    Termination property:
        - the algorithm will terminate whenever i >= len
        - len is a constant and finite natural number
        - the variable i increments by 1 in each iteration

    Partial correctness:
        - invariant: (∀0≤j<i x ≥ Arr[j]) ∧ (∃0≤j<len(x == Arr[j]))
        - if it was true in iteration i 
          it will be true after iteration i 
          due to the conditional update of variable x in the 'if' statement
        - the invariant is also true just before the first iteration of the loop 
          so it will be true after any number of iterations.    
"""

from typing import Iterable

def sum(sequence: Iterable[int], length: int) -> int:
    """
    Calculates the sum of the first 'length' elements in 'sequence'.
    
    Returns:
        The sum of the first 'length' elements of 'sequence'.
        If 'sequence' is empty or 'length' is 0, returns 0.
    """
    total: int = 0
    count: int = 0
    
    for num in sequence:
        if count < length:
            total += num
            count += 1
        else:
            break
            
    return total

def main() -> None:
    array1: list[int] = [1, 2, 3]
    array2: tuple[int] = (4, 5, 6)
    array3: set[int] = {7, 8, 9}
    
    print(sum(array1, len(array1)))
    print(sum(array2, 2))
    print(sum(array3, len(array3)))

if __name__ == "__main__":
    main()
