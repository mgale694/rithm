"""
This module implements the merge sort algorithm.

Merge sort is a divide-and-conquer algorithm that sorts an array by recursively
dividing it into halves, sorting each half, and then merging the sorted halves
back together.

When merging, it compares the elements of the two halves and appends the smaller
element to the result list until all elements are merged. The remaining elements
from either half are then appended to the result, as they are already sorted.

Time Complexity:
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

Space Complexity:
- O(n) due to the use of additional space for the temporary arrays during merging.

Example:
array = [12, 8, 9, 3, 11, 5, 4]
[12, 8, 9] <> [3, 11, 5, 4]
[12] <> [8, 9] ~ [3, 11] <> [5, 4]
[12] ~ [8] <> [9] ~ [3] <> [11] ~ [5] <> [4]
Sort [8] <> [9]
[8, 9]
sort [12] <> [8, 9]
[8, 9, 12]

Sort [3] <> [11]
[3, 11]
Sort [5] <> [4]
[4, 5]
Sort [3, 11] <> [4, 5]
[3, 4, 5, 11]
Finally, merge [8, 9, 12] <> [3, 4, 5, 11]
[3, 4, 5, 8, 9, 11, 12]
"""


class MergeSort(object):
    def __init__(self, array: list) -> None:
        self.array: list = array

    def sort(self, debug: bool = False) -> list:
        """
        Sorts the array using the merge sort algorithm.

        This method recursively divides the array into halves, sorts each half,
        and then merges the sorted halves back together.

        :param debug: If True, prints debug information.

        :return: A new sorted list containing the elements of the original array.
        """
        if len(self.array) <= 1:
            return self.array

        _mid = len(self.array) // 2

        L = self.array[:_mid]
        R = self.array[_mid:]

        if debug:
            print(self.array)
            # print(L, R)
        _left = MergeSort(L).sort(debug=debug)
        _right = MergeSort(R).sort(debug=debug)

        return self.merge(_left, _right, debug=debug)

    def merge(self, left: list, right: list, debug: bool = False) -> list:
        """
        Merges two sorted lists into one sorted list.

        This method takes two sorted lists and merges them into a single sorted list.
        The merging process involves comparing the elements of both lists and
        appending the smaller element to the result list until all elements are merged.
        The remaining elements from either list are then appended to the result,
        as we know they are already sorted.

        :param left: The first sorted list.
        :param right: The second sorted list.
        :param debug: If True, prints debug information.

        :return: A new sorted list containing all elements from both input lists.
        """
        sorted_array = []
        i = j = 0

        if debug:
            print("Merging:", left, right)

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1

        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])

        if debug:
            print("Merged:", sorted_array)
        return sorted_array


if __name__ == "__main__":
    # Example usage
    array = [12, 8, 9, 3, 11, 5, 4]
    merge_sort = MergeSort(array)
    sorted_array = merge_sort.sort(debug=True)
    print("Sorted array:", sorted_array)
