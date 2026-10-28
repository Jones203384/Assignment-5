from collections import Counter
from io import StringIO
import unittest
from unittest import mock


# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    if not numbers:
        return None

    counts = Counter(numbers)
    highest_count = max(counts.values())
    return next(value for value, count in counts.items() if count == highest_count)


"""
Time and Space Analysis for problem 1:
- Best-case time: O(n); every value must be inspected to know its frequency.
- Worst-case time: O(n^2) in the pathological case of repeated hash collisions; expected O(n) with normal dictionary behavior.
- Average-case time: O(n), including the O(k) scan to select a most frequent value, where k is the number of distinct values.
- Space complexity: O(k) for the frequency map.
- Why this approach?: A frequency map counts values in one pass and makes it easy to return any value tied for the maximum.
- Could it be optimized?: If values have a small, known integer range, a fixed-size counting array may be faster, but it uses space based on the range rather than the number of distinct values.
- Trade-offs: The map uses extra memory, but avoids sorting (O(n log n)) or repeatedly scanning the list (O(n^2)); the answer to an empty list is defined here as None.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []

    for value in nums:
        if value not in seen:
            seen.add(value)
            result.append(value)

    return result


"""
Time and Space Analysis for problem 2:
- Best-case time: O(n); even if all values are equal, the function must inspect every item.
- Worst-case time: O(n^2) with pathological set hash collisions; expected O(n) with normal set behavior.
- Average-case time: O(n), as set membership and insertion take constant time on average for each of the n values.
- Space complexity: O(n) in the worst case for the set and returned list (O(k) distinct values).
- Why this approach?: One pass with a set preserves first-occurrence order while checking membership efficiently.
- Could it be optimized?: The time is asymptotically optimal because every input value must be examined. Returning a lazy iterator could avoid storing the full result, but would change the function's list-returning behavior.
- Trade-offs: The set uses extra memory to provide fast membership checks. A comparison against the growing result list would use less auxiliary memory but can take O(n^2) time.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []

    for value in nums:
        complement = target - value
        if complement in seen:
            pairs.append((min(value, complement), max(value, complement)))
        seen.add(value)

    return pairs


"""
Time and Space Analysis for problem 3:
- Best-case time: O(n); all n values still need to be checked, even if no pairs match.
- Worst-case time: O(n^2) with pathological set hash collisions; expected O(n) with normal set behavior.
- Average-case time: O(n), using one complement lookup and insertion per value.
- Space complexity: O(n) for the seen set and the output pairs combined.
- Why this approach?: A set of previously seen values lets each value find its complement in one pass without nested loops.
- Could it be optimized?: For already-sorted input, a two-pointer scan also takes O(n) time and can use O(1) auxiliary space, excluding the output.
- Trade-offs: The hash-set approach avoids sorting and works on unsorted input, at the cost of O(n) auxiliary memory; sorting first adds O(n log n) time but can reduce auxiliary memory.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n, initial_capacity=4):
    if n < 0:
        raise ValueError("n must be non-negative")

    values = []
    capacity = initial_capacity

    for index in range(1, n + 1):
        if len(values) == capacity:
            new_capacity = capacity * 2
            print(f"Resizing from {capacity} to {new_capacity}")
            new_values = values.copy()
            values = new_values
            capacity = new_capacity

        values.append(index)

    return values


"""
Time and Space Analysis for problem 4:
- Best-case time: O(n) for n appends when the starting capacity is sufficient and no values need copying.
- Worst-case time: O(n) total across n appends, including all copies during doubling; an individual append that triggers a resize takes O(n).
- Average-case time: O(n) total, or O(1) amortized per append, because the occasional linear copy is spread across many inexpensive appends.
- Space complexity: O(n) for the stored values; during a resize, the old and copied lists coexist temporarily, still using O(n) peak space.
- Why this approach?: Doubling is a simple dynamic-array strategy that demonstrates how occasional expensive resizes yield constant amortized append cost.
- Could it be optimized?: A smaller growth factor can reduce unused capacity, while a larger factor can reduce resize frequency. Python's built-in list already manages capacity for production use.
- Trade-offs: Doubling keeps total copying linear and resizing infrequent, but can leave nearly half the allocated capacity unused after growth and temporarily requires memory for both lists.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    running_sum = 0
    result = []

    for value in nums:
        running_sum += value
        result.append(running_sum)

    return result


"""
Time and Space Analysis for problem 5:
- Best-case time: O(n); each input value contributes to an output value and must be visited.
- Worst-case time: O(n) under the usual constant-time arithmetic assumption, since the loop performs one addition and append per input value.
- Average-case time: O(n) under the same assumption.
- Space complexity: O(n) for the new output list and O(1) auxiliary space.
- Why this approach?: A running accumulator computes all prefixes in one pass without recalculating each prefix from the beginning.
- Could it be optimized?: The runtime cannot be asymptotically improved because the input must be read and the n-element result must be created. An in-place variant could avoid a separate output list but would mutate the input.
- Trade-offs: Returning a new list preserves the original input but requires O(n) additional memory; in-place accumulation saves that memory at the cost of changing the caller's list.
"""


class TestPerformanceLab(unittest.TestCase):
    def test_most_frequent_basic(self):
        self.assertEqual(most_frequent([1, 3, 2, 3, 4, 1, 3]), 3)

    def test_most_frequent_tie(self):
        result = most_frequent([2, 1, 2, 1, 3])
        self.assertIn(result, {1, 2})

    def test_most_frequent_empty(self):
        self.assertIsNone(most_frequent([]))

    def test_remove_duplicates_preserves_order(self):
        self.assertEqual(remove_duplicates([4, 5, 4, 6, 5, 7]), [4, 5, 6, 7])

    def test_remove_duplicates_edge_cases(self):
        self.assertEqual(remove_duplicates([]), [])
        self.assertEqual(remove_duplicates([7, 7, 7]), [7])
        self.assertEqual(remove_duplicates([1, 2, 3, 1, 2, 4]), [1, 2, 3, 4])

    def test_find_pairs_basic(self):
        self.assertEqual(find_pairs([1, 2, 3, 4], 5), [(2, 3), (1, 4)])

    def test_find_pairs_no_pairs(self):
        self.assertEqual(find_pairs([1, 2, 3, 4], 10), [])

    def test_find_pairs_empty(self):
        self.assertEqual(find_pairs([], 5), [])

    def test_add_n_items_resizes(self):
        with mock.patch("sys.stdout", new_callable=StringIO) as output:
            result = add_n_items(6, initial_capacity=4)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])
        self.assertIn("Resizing from 4 to 8", output.getvalue())

    def test_add_n_items_zero_and_negative(self):
        self.assertEqual(add_n_items(0, initial_capacity=4), [])
        with self.assertRaises(ValueError):
            add_n_items(-1, initial_capacity=4)

    def test_running_total_basic(self):
        self.assertEqual(running_total([1, 2, 3, 4]), [1, 3, 6, 10])

    def test_running_total_edge_cases(self):
        self.assertEqual(running_total([]), [])
        self.assertEqual(running_total([5, -2, 3]), [5, 3, 6])
        self.assertEqual(running_total([0, 0, 0]), [0, 0, 0])


if __name__ == "__main__":
    unittest.main()
