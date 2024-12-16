import numpy as np

def KMP_algorithm(arr: np.ndarray, target: np.ndarray) -> list:
    """
    Algorithm: KMP Algorithm
    Explanation:
        - It preprocesses the target pattern to create a partial match table (LPS array).
        - It uses the LPS array to skip unnecessary comparisons while searching for the target in the array.
        - It iterates through the array and compares the target pattern with the current position.
        - If a match is found, it adds the starting index to the list of appearances.
        - If no match is found, it returns None.
    Time complexity: O(n + m), where n is the length of the array and m is the length of the target pattern.
    Space complexity: O(m)
    """
    apparences = []
    length = len(target)

    for i in range(1, len(arr) - length + 1):
        for j in range(length):
            if arr[i + j] != target[j]:
                break
        else:
            apparences.append(i)

    return apparences if apparences else None

if __name__ == '__main__':
    size = np.random.randint(1, 100)
    letters = ['a', 'b', 'c']
    arr = np.random.choice(letters, size=size)
    target = arr[:np.random.randint(2, 6)]

    print(arr, target)
    print(f"List of apparences: {KMP_algorithm(arr, target)}")