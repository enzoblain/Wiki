import numpy as np

def linearSearch(arr: np.ndarray, target: int) -> int:
    """
    Algorithm: Linear Search
    Explanation:
        - A simple search algorithm that checks each element of the array in sequence.
        - Works by iterating through the array from the first element to the last, comparing each element to the target value.
        - If a match is found, the index of the element is returned.
        - If the target is not found after checking all elements, it returns `-1` to indicate the target is not present in the array.
    
    Time Complexity: O(n), where `n` is the number of elements in the array.
    Space Complexity: O(1), as it uses a constant amount of extra space.
    """
    for index, val in enumerate(arr):
        if val == target:
            return index
        
    return -1

if __name__ == '__main__':
    size = np.random.randint(1, 100)
    arr = np.sort(np.random.choice(range(100), size=size, replace=False))
    target = arr[np.random.randint(0, size)]
    print(f"Array: {arr}, Target: {target}")
    
    print(f"Index: {linearSearch(arr, target)}")