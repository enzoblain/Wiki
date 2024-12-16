import numpy as np

def bubbleSort(arr: np.ndarray) -> int:
    """
    Algorithm: Bubble Sort
    Explanation:
        - Repeatedly iterates through the array, comparing adjacent elements.
        - Swaps adjacent elements if they are in the wrong order to "bubble" the largest unsorted element to its correct position.
        - Reduces the range of comparison after each pass, as the largest elements are placed in their correct positions.
        - Stops early if no swaps are made during a pass, indicating the array is already sorted.
    Time Complexity: O(n^2) in the worst and average case, O(n) in the best case (when the array is already sorted).
    Space Complexity: O(1) (in-place sorting).
    """
    for pass_num in range(len(arr)):
        swapped = False

        for i in range(len(arr) - pass_num - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

    return arr

if __name__ == '__main__':
    size = np.random.randint(1, 100)
    arr = np.random.choice(range(100), size=size, replace=False)
    print(f"Array: {arr}")
    print(f"Sorted Array: {bubbleSort(arr)}")