"""
Task:
    Find the index of the specified key in the array up to the given length.

Specification:
    Name and arguments:
        find(arr, len, key)

    Initial condition:
        arr - an array of integers
        len - a natural number representing the declared length of the array
        key - an integer that is being searched for in the array

    Final condition:
        The algorithm should return a natural number < len,
        which is the index where the key first appears in the array 'arr' up to index 'len'.
        If the key is not found among the first 'len' elements, it should return -1.

"""

def find(arr: list[int], length: int, key: int) -> int:
    """
    Finds the index of the specified key in the array up to the given length.
    
    Returns:
        The index of the specified key in the array 'arr' up to index 'len'.
        If the key is not found among the first 'len' elements, return -1.
    """
    for i in range(length):
        if arr[i] == key:
            return i
    return -1
def main() -> None:
    pass

if __name__ == '__main__':
    main()