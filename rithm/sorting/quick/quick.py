"""
Module for Quick Sort algorithm implementation.

The Quick Sort algorithm is a divide-and-conquer algorithm that sorts an array
by selecting a 'pivot' element and partitioning the other elements into two
sub-arrays, according to whether they are less than or greater than the pivot.

The sub-arrays are then sorted recursively. This implementation includes both
an inplace sorting method and a non-inplace sorting method that returns a new
sorted list.

Time Complexity:
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n^2) (when the smallest or largest element is always chosen as pivot)

Space Complexity:
- O(log n) for the recursive stack space in the inplace version
- O(n) for the non-inplace version due to the creation of new lists

Example:

arr = [11, 9, 12, 7, 3]
pivot = 3 # Choose the last element as pivot

step 1: [11, 9, 12, 7, 3]
step 2: [3, 9, 12, 7, 11] # Swap pivot with the first element greater than it
step 3: choose 11 as pivot
step 4: [3, 9, 7, 12, 11] # Move elements less than 11 to the left
step 5: [3, 9, 7, 11, 12] # Swap pivot with the first element greater than it
step 6: choose 7 as pivot
step 7: [3, 7, 9, 11, 12] # Move elements less than 7 to the left

return [3, 7, 9, 11, 12]

When you do quick sort inplace the concept of pivot is a bit misleading. This
is because when you non-inplace, you literally sort array either side of the
pivot then glue it back together (lower, pivot, higher).

However, when you choose a pivot, then you move all less than or equal elements
to the left, then glue back on the pivot just after the less than elements (as
you track the index that you are at). Then you do the same to left and right of
the final pivot index.

[3, 7, 2, 1, 5] with pivot 5
3 replaces 3
2 replaces 7
1 replaces 7
thats 3 operations so index will be 2 (start at -1)
so 5 goes into index 3
[3, 2, 1, 5, 7]
now we do the same on [3, 2, 1] and [7] (which is already sorted)
so we choose 1 as pivot
none are less than or equal so 0 operations
so 1 goes into index 0
[1, 2, 3, 5, 7] -> sorted
"""


class QuickSort(object):
    def __init__(self, array: list) -> None:
        self.array: list = array

    def inplace_sort(
        self, low: int, high: int, debug=False, _partition_count=0
    ) -> None:
        """
        This is an inplace sorting method that sorts the array in place.
        Being inplace, it modifies the original array therefore it is suitable
        for cases where memory usage is a concern, but it may not preserve
        the original order of elements, including duplicates.

        :param low: The starting index of the array to sort.
        :param high: The ending index of the array to sort.
        :param debug: If True, prints debug information during sorting.

        :return: None
        """
        if low < high:
            if debug:
                print(
                    f"\nPartition count: {_partition_count}, low: {low}, high: {high}"
                )
                print(self.array, f"Sub-array: {self.array[low : high + 1]}")

            # Partition the array and get the pivot index
            pivot_index = self.partition(low, high, debug=debug)
            if debug:
                print(
                    f"Pivot index: {pivot_index}, Pivot value: {self.array[pivot_index]}"
                )
            _partition_count += 1
            self.inplace_sort(
                low, pivot_index - 1, debug=debug, _partition_count=_partition_count
            )
            self.inplace_sort(
                pivot_index + 1, high, debug=debug, _partition_count=_partition_count
            )

    def partition(self, low: int, high: int, debug=False) -> int:
        """
        This is the core method for inplace quick sort.
        It partitions the array into two halves based on the pivot element.
        Elements less than or equal to the pivot are moved to the left,
        and elements greater than the pivot are moved to the right.

        This uses Lomuto partition scheme, which is a common approach in quick
        sort that tracks the index as it moves the elements to the left.

        Hoare's partition scheme is another approach that is more efficient
        but is more complex to implement. This would use two pointers from
        either end of the array and swap elements until they meet in the middle.

        :param low: The starting index of the array to partition.
        :param high: The ending index of the array to partition.
        :param debug: If True, prints debug information during partitioning.

        :return: The index of the pivot element after partitioning.
        """
        # Start with the last element as the pivot and move all elements
        # less than or equal to the pivot to the left of it
        pivot = self.array[high]

        # Initialize the index of the smaller element
        # and iterate through the array to partition it, starting from low - 1
        # to ensure the first element is considered
        i = low - 1
        for j in range(low, high):
            # If the current element is less than or equal to the pivot,
            # increment the index of the smaller element and swap it with the
            # current element
            if self.array[j] <= pivot:
                i += 1
                if debug:
                    print(
                        f"Element {self.array[j]} at index {j} is less than or equal to pivot {pivot}. "
                        f"Incrementing index i to {i}."
                    )
                    print(
                        f"Swapping {self.array[i]} and {self.array[j]} at indices {i} and {j}"
                    )
                self.array[i], self.array[j] = self.array[j], self.array[i]

        # After the loop, swap the pivot element with the first element
        # greater than it to place the pivot in its correct position
        if debug:
            print(
                f"Placing pivot {pivot} at index {i + 1}. Swapping with {self.array[high]} at index {high}."
            )
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        return i + 1

    def non_inplace_sort(
        self,
        pivot_index: int | None = None,
        debug: bool = False,
    ) -> list:
        """
        This is a non-inplace sorting method that returns a new sorted list.

        Being non-inplace, it does not modify the original array therefore
        it is suitable for cases where the original order of elements needs
        to be preserved, including duplicates. However, it may use
        additional memory for the new list.

        :param pivot_index: The pivot index to use for sorting.
        :param debug: If True, prints debug information during sorting.

        :return: A new sorted list.
        """
        # Early exit
        # If the array is empty, return an empty list
        if not self.array:
            return []
        # If the array has one element, return it as is
        if len(self.array) == 1:
            return self.array

        if pivot_index is None:
            # If no pivot is provided, choose the middle element as pivot
            pivot_index = len(self.array) // 2

        # Check pivot_index is in bounds
        if pivot_index < 0 or pivot_index >= len(self.array):
            raise ValueError("Pivot index is out of bounds.")

        pivot = self.array[pivot_index]
        rest = self.array[:pivot_index] + self.array[pivot_index + 1 :]
        _low = [x for x in rest if x <= pivot]
        _high = [x for x in rest if x > pivot]

        if debug:
            print(_low, [pivot], _high)

        return (
            QuickSort(_low).non_inplace_sort(debug=debug)
            + [pivot]
            + QuickSort(_high).non_inplace_sort(debug=debug)
        )


if __name__ == "__main__":
    array = [3, 6, 8, 10, 1, 2, 1]
    quick_sort = QuickSort(array)
    sorted_array = quick_sort.non_inplace_sort(debug=True)
    print("Sorted array (non-inplace):", sorted_array)
    # For inplace sorting, you can use:
    # quick_sort.inplace_sort(0, len(array) - 1, debug=True)
    # print("Sorted array (inplace):", quick_sort.array)
