import numpy as np

def insertionSort(arr: np.ndarray) -> int:
    """
    Algorithm: Insertion Sort
    Explanation:
        - Iterates through the array and places each element in its correct position within the sorted portion.
        - Compares the current element with the previous elements and shifts them to make space for the current element.
        - This process is repeated until the entire array is sorted.
    Time Complexity: O(n^2) in the worst and average case, O(n) in the best case.
    Space Complexity: O(1) (in-place sorting).
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

if __name__ == '__main__':
    size = np.random.randint(1, 100)
    arr = np.random.choice(range(100), size=size, replace=False)
    print(f"Array: {arr}")
    print(f"Sorted Array: {insertionSort(arr)}")