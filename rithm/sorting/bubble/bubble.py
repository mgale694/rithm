"""
Module for the Bubble Sort algorithm implementation.

The Bubble Sort algorithm is a simple sorting algorithm that repeatedly steps through
the list, compares adjacent elements, and swaps them if they are in the wrong order.
The pass through the list is repeated until the list is sorted.

Time Complexity:
- Best Case: O(n) (when the array is already sorted)
- Average Case: O(n^2)
- Worst Case: O(n^2) (when the array is sorted in reverse order)

Space Complexity:
- O(1) for the inplace version (no additional space used)

Example:
arr = [64, 34, 25, 12, 22, 11, 90]
[64, 34, 25, 12, 22, 11, 90]
[34, 64, 25, 12, 22, 11, 90]
[34, 25, 64, 12, 22, 11, 90]
[34, 25, 12, 64, 22, 11, 90]
[25, 34, 12, 22, 64, 11, 90]
[25, 12, 22, 34, 64, 11, 90]
[12, 22, 25, 34, 64, 11, 90]
[12, 22, 25, 34, 11, 64, 90]
[12, 22, 25, 11, 34, 64, 90]
[12, 22, 11, 25, 34, 64, 90]
[12, 11, 22, 25, 34, 64, 90]
[11, 12, 22, 25, 34, 64, 90] -> sorted

Bubble Sort is not the most efficient sorting algorithm for large datasets,
but it is easy to understand and implement.
"""


class BubbleSort(object):
    def __init__(self, array: list) -> None:
        self.array: list = array

    # def sort(self) -> list:
    #     n = len(self.arr)
    #     for i in range(n):
    #         # Track if a swap was made
    #         swapped = False
    #         for j in range(0, n-i-1):
    #             # Compare adjacent elements
    #             if self.arr[j] > self.arr[j+1]:
    #                 # Swap if they are in the wrong order
    #                 self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
    #                 swapped = True
    #         # If no two elements were swapped, the array is sorted
    #         if not swapped:
    #             break
    #     return self.arr

    def sort(self, debug: bool = False) -> None:
        """
        Sorts the array using the bubble sort algorithm.

        This method is an inplace sorting algorithm that repeatedly steps through
        the list, compares adjacent elements, and swaps them if they are in the
        wrong order. The pass through the list is repeated until the list is sorted.

        :return: None
        """
        n = len(self.array)

        # Loop through the array n times
        for i in range(n):
            # Additional early exit optimization
            # Track if a swap was made
            swapped = False

            # Loop through the array up to the last unsorted element
            # Each pass places the largest unsorted element at the end
            # of the unsorted section
            for j in range(0, n - i - 1):
                # Compare adjacent elements
                if self.array[j] > self.array[j + 1]:
                    if debug:
                        print(self.array)
                        print(
                            f"Swapping {self.array[j]} and {self.array[j + 1]} at indices {j} and {j + 1}"
                        )
                    # Swap if they are in the wrong order
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    swapped = True

            # If no two elements were swapped, the array is sorted
            if not swapped:
                break


if __name__ == "__main__":
    # Example usage
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sorter = BubbleSort(arr)
    print("Original array:", bubble_sorter.array)
    bubble_sorter.sort(debug=True)  # Assuming a sort method is implemented
    print("Sorted array:", bubble_sorter.array)
