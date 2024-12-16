import numpy as np

def kadane_algorithm(arr: np.ndarray) -> int:
    """
    Algorithm: Kadane's Algorithm
    Explanation:
        - It iterates through the array and keeps track of the maximum sum of the subarray ending at the current position.
        - It updates the maximum sum encountered so far.
        - It returns the maximum sum of any subarray found.
    Time complexity: O(n), where n is the number of elements in the array.
    Space complexity: O(1)
    """
    max_sum = 0

    for length in range(len(arr), 0, -1):
        for start in range(len(arr) - length + 1):
            end = start + length
            sub_arr = arr[start:end]

            if sum(sub_arr) > max_sum:
                max_sum = sum(sub_arr)

    return max_sum

if __name__ == '__main__':
    size = np.random.randint(1, 100)
    arr = np.random.choice(range(-100, 100), size=size, replace=False)
    target = arr[np.random.randint(0, size)]

    print(arr)
    print(f"Best sub array sum: {kadane_algorithm(arr)}")