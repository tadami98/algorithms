"""
Task:
    Return the sum of numbers in the given sequence 
    up to the specified length.

Specification:
    Name and arguments: 
        calculate_sum(sequence, length)

    Initial condition: 
        sequence - an iterable of integers
        length - a natural number representing the declared length of the sequence

    Final condition: 
        The algorithm should return an integer
        that is the sum of the first length elements of this sequence,
        or zero if the sequence is empty.


    Poprawność algorytmu:
        Własność stopu:
            - algorytm zatrzyma się, kiedykolwiek zajdzie i >= len
            - len jest stałą i skończoną liczbą naturalną
            - wartość zmiennej i rośnie o 1 w każdej iteracji
"""

from typing import Iterable

def calculate_sum(sequence: Iterable[int], length: int) -> int:
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
    
    print(calculate_sum(array1, len(array1)))
    print(calculate_sum(array2, 2))
    print(calculate_sum(array3, len(array3)))

if __name__ == "__main__":
    main()
