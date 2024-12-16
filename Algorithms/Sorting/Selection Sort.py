import numpy as np

def selectionSort(arr: np.ndarray) -> int:
    """
    Algorithm: Selection Sort
    Explanation:
        - Divides the array into two parts: sorted and unsorted.
        - Iteratively selects the smallest element from the unsorted part and swaps it with the first element of the unsorted part.
        - This process ensures that the smallest elements are placed in their correct positions in the sorted portion.
        - Repeats until the entire array is sorted.

    Time Complexity: O(n^2) in the worst, average, and best cases (due to nested loops).
    Space Complexity: O(1) (in-place sorting).
    """
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    
    return arr

if __name__ == '__main__':
    size = np.random.randint(1, 100)
    arr = np.random.choice(range(100), size=size, replace=False)
    print(f"Array: {arr}")
    print(f"Sorted Array: {selectionSort(arr)}")