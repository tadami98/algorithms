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

def find(arr: list[int], len: int, key: int) -> int:
    """
    Finds the index of the specified key in the array up to the given len.
    
    Returns:
        The index of the specified key in the array 'arr' up to index 'len'.
        If the key is not found among the first 'len' elements, return -1.
    """
    while i < len:
        if arr[i] == key:
            return i
        i += 1
    return -1

def main() -> None:
    arr: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    len = len(arr)
    key: int = 8

    key_index: int = find(arr, len, key)

    if key_index == -1:
        print(f"The key {key} not found in the array.")
    else:
        print(f"The key {key} found at index {key_index}.")

if __name__ == '__main__':
    main()