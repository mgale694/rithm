"""
This module implements the Selection Sort algorithm.

Selection Sort is a simple, in-place comparison sorting algorithm. It works
by repeatedly selecting the smallest (or largest) element from the unsorted
portion of the array and moving it to the end of the sorted portion.

Time Complexity:
- Best Case: O(n^2)
- Average Case: O(n^2)
- Worst Case: O(n^2)

Space Complexity:
- O(1) for the in-place version, as it only requires a constant amount of

Example:
arr = [64, 25, 12, 22, 11, 4]
Two pointers are used to track the current index and the minimum index.
Loop through to find the minimum element in the unsorted part of the array, and
this becomes the min index.
Then swap this index with the current index.
Found min of 4, swap to front
[4, 25, 12, 22, 11, 64]
Now look at remaining unsorted part [25, 12, 22, 11, 64]
found 11, swap to front
[4, 11, 12, 22, 25, 64]
When rest is sorted then it continues to loop over and min index won't change
so nothing gets swapped.
"""


class SelectionSort(object):
    def __init__(self, array: list) -> None:
        self.array: list = array

    def sort(self, dubug: bool = False) -> list:
        """
        Sorts the array using the selection sort algorithm.

        Selection sort is an in-place comparison sorting algorithm. It divides
        the input list into two parts: a sorted and an unsorted part. The
        sorted part is built up from left to right, and the unsorted part is
        reduced by selecting the smallest (or largest) element from the
        unsorted part and moving it to the end of the sorted part.
        """
        n = len(self.array)

        # Loop through the array
        for i in range(n):
            # Set the minimum index to the current index
            min_index = i
            # Loop through the unsorted part of the array
            for j in range(i + 1, n):
                # If the current element is smaller than the current minimum,
                # update the minimum index. Therefore moving the smallest
                # element to the front of the unsorted part.
                if self.array[j] < self.array[min_index]:
                    if dubug:
                        print(
                            f"Found new minimum {self.array[j]} at index {j}, "
                            f"previous minimum was {self.array[min_index]} at index {min_index}"
                        )
                    min_index = j
            if min_index != i:
                if dubug:
                    print(self.array)
                    print(
                        f"Swapping {self.array[i]} at index {i} with {self.array[min_index]} at index {min_index}"
                    )
                self.array[i], self.array[min_index] = (
                    self.array[min_index],
                    self.array[i],
                )
        return self.array


if __name__ == "__main__":
    # Example usage
    arr = [64, 25, 12, 22, 11]
    sorter = SelectionSort(arr)
    sorted_arr = sorter.sort(dubug=True)
