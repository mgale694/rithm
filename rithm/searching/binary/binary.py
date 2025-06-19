"""
This module implements a binary search algorithm.

Binary search is an efficient algorithm for finding an item from a sorted list
of items. It works by repeatedly dividing the search interval in half.
If the value of the search key is less than the item in the middle of the interval,
narrow the interval to the lower half. Otherwise, narrow it to the upper half.
Repeatedly check until the value is found or the interval is empty.

Time Complexity: O(log n)
Space Complexity: O(1)

e.g. 1billion elements in simple search would take 1 billion comparisons,
while in binary search it would take only about 30 comparisons. (log2(1 billion) ≈ 30)

log2(32) = 5 # because 2^5 = 32
"""


class BinarySearch(object):
    def __init__(self, array: list) -> None:
        # Ensure that the array is sorted for binary search to work correctly.
        if array != sorted(array):
            print("Input wasn't sorted, sorting it now.")
        self.array: list = sorted(array)

    def search(self, target: int) -> int:
        left = 0
        right = len(self.array) - 1

        # Loop until the left index is greater than the right index
        while left <= right:
            mid = (left + right) // 2

            # Check if the middle element is the target
            if self.array[mid] == target:
                return mid
            # If the target is greater, ignore the left half
            elif self.array[mid] < target:
                left = mid + 1
            # If the target is smaller, ignore the right half
            else:
                right = mid - 1

        return None  # Target not found in the array


if __name__ == "__main__":
    # Example usage
    binary_search = BinarySearch([3, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    index = binary_search.search(5)
    print(f"Index of target: {index}")  # Output: Index of target: 4
    index = binary_search.search(10)
    print(f"Index of target: {index}")  # Output: Index of target: None
