import numpy as np

def binarySearch(arr: np.ndarray, target: int) -> int:
    """
    Algorithm: Binary Search
    Explanation:
        - It repeatedly divides the array in half and compares the middle element with the target.
        - If a match is found, it returns the index of the element.
        - If the middle element is less than the target, it searches the right half.
        - If the middle element is greater than the target, it searches the left half.
        - If no match is found, it returns -1.
    Time complexity: O(log n)
    Space complexity: O(1)
    """
    while True:
        if len(arr) == 1:
            return 0 if arr[0] == target else -1
        
        mid = len(arr) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            arr = arr[mid:]

        else:
            arr = arr[:mid]

def binarySearchRecursivity(arr: np.ndarray, target: int, left: int, right: int) -> int:
    """
    Algorithm: Binary Search (Recursivity)
    Explanation:
        - It repeatedly divides the array in half and compares the middle element with the target.
        - If a match is found, it returns the index of the element.
        - If the middle element is less than the target, it searches the right half.
        - If the middle element is greater than the target, it searches the left half.
        - If no match is found, it returns -1.
    Time complexity: O(log n)
    Space complexity: O(log n)
    """
    if left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            return binarySearchRecursivity(arr, target, mid + 1, right)
        
        else:
            return binarySearchRecursivity(arr, target, left, mid - 1)
        
    return -1

if __name__ == '__main__':
    size = np.random.randint(1, 100)
    arr = np.sort(np.random.choice(range(100), size=size, replace=False))
    target = arr[np.random.randint(0, size)]
    print(f"Array: {arr}, Target: {target}")
    
    print(f"Index: {binarySearch(arr, target)}")
    print(f"Index (Recursivity): {binarySearchRecursivity(arr, target, 0, len(arr) - 1)}")