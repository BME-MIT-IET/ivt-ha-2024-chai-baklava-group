# Results and Code Coverage analysis of Unit Tests

## Pre-requisites:
We will be using Coverage.py tool for code coverage analysis.

Install the tool "Coverage.py" of the Python library using the command:

`pip install coverage`

## Command ran
`coverage run -m unittest discover -s testIVT -p "*.py"`

`coverage run`: This command is part of the coverage tool. It's used to run a Python program while tracking which lines of code are executed.

`-m unittest discover`: This part tells Python to run the unittest module and discover tests automatically. Unittest is Python's built-in testing framework. The discover command recursively searches for test modules in the specified directory (-s testIVT) and runs them.

`-s testIVT`: This specifies the directory where the test modules are located. In this case, it's testIVT.

`-p "*.py"`: This option specifies a pattern to match the test module filenames. Here, it's matching all files with a .py extension, which typically indicates Python source code files.

## Initial output
`coverage run -m unittest discover -s testIVT -p "*.py"`
```
[False, 1, 1, 2, 1, 3, 'a', 0, 0]
................................F.F.....................
======================================================================
FAIL: test_palindrome_list (List_test_is_plindrome.TestPalindromeList.test_palindrome_list)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\testIVT\List_test_is_plindrome.py", line 31, in test_palindrome_list
    self.assertTrue(is_palindrome_stack(head))
AssertionError: False is not true

======================================================================
FAIL: test_two_element_non_palindrome_list (List_test_is_plindrome.TestPalindromeList.test_two_element_non_palindrome_list)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\testIVT\List_test_is_plindrome.py", line 60, in test_two_element_non_palindrome_list
    self.assertFalse(is_palindrome_stack(head))
AssertionError: True is not false

----------------------------------------------------------------------
Ran 56 tests in 0.040s

FAILED (failures=2)
```

2 tests fail.

Looking at the test cases, and the files being tested, the issue appears to be algorithm related.

## Code coverage analysis
```
Name                                           Stmts   Miss  Cover
------------------------------------------------------------------
algorithms\arrays\__init__.py                     19      0   100%
algorithms\arrays\delete_nth.py                   15      0   100%
algorithms\arrays\flatten.py                      14      0   100%
algorithms\arrays\garage.py                       18     16    11%
algorithms\arrays\josephus.py                      8      7    12%
algorithms\arrays\limit.py                         8      1    88%
algorithms\arrays\longest_non_repeat.py           63      4    94%
algorithms\arrays\max_ones_index.py               16      0   100%
algorithms\arrays\merge_intervals.py              48     34    29%
algorithms\arrays\missing_ranges.py               12     11     8%
algorithms\arrays\move_zeros.py                   10      0   100%
algorithms\arrays\n_sum.py                        64     63     2%
algorithms\arrays\plus_one.py                     30     27    10%
algorithms\arrays\remove_duplicates.py             6      5    17%
algorithms\arrays\rotate.py                       28     25    11%
algorithms\arrays\summarize_ranges.py             14     12    14%
algorithms\arrays\three_sum.py                    21     20     5%
algorithms\arrays\top_1.py                        14     13     7%
algorithms\arrays\trimmean.py                      9      8    11%
algorithms\arrays\two_sum.py                       7      6    14%
algorithms\linkedlist\__init__.py                  9      0   100%
algorithms\linkedlist\copy_random_pointer.py      27     22    19%
algorithms\linkedlist\is_cyclic.py                15      0   100%
algorithms\linkedlist\is_palindrome.py            64     11    83%
algorithms\linkedlist\is_sorted.py                 9      8    11%
algorithms\linkedlist\merge_two_list.py           23      0   100%
algorithms\linkedlist\remove_range.py             13     12     8%
algorithms\linkedlist\reverse.py                  22      0   100%
algorithms\linkedlist\rotate_list.py              19      0   100%
algorithms\linkedlist\swap_in_pairs.py            18     15    17%
algorithms\stack\__init__.py                      10      0   100%
algorithms\stack\is_consecutive.py                33     30     9%
algorithms\stack\is_sorted.py                     16      1    94%
algorithms\stack\ordered_stack.py                 24     16    33%
algorithms\stack\remove_min.py                    16     15     6%
algorithms\stack\simplify_path.py                 11     10     9%
algorithms\stack\stack.py                         82     53    35%
algorithms\stack\stutter.py                       23     20    13%
algorithms\stack\switch_pairs.py                  35     32     9%
algorithms\stack\valid_parenthesis.py             10      0   100%
testIVT\Array_Test_longest.py                     33      1    97%
testIVT\Array_limit_test.py                       16      1    94%
testIVT\Array_test_delete_nth.py                  57      1    98%
testIVT\Array_test_flatten.py                     22      2    91%
testIVT\Array_test_max_ones_index.py              21      1    95%
testIVT\List_is_cyclic_test.py                    32      1    97%
testIVT\List_test_is_plindrome.py                 52      9    83%
testIVT\List_test_merge_lists.py                  44      2    95%
testIVT\List_test_reverse.py                      44      2    95%
testIVT\List_test_rotate_list.py                  46      2    96%
testIVT\Stack_test_sorted_stack.py                26      1    96%
testIVT\Stack_test_valid_parenthesis.py           21      1    95%
------------------------------------------------------------------
TOTAL                                           1317    521    60%
```
Current coverage: 60%

# Iteration 2: After adding more tests

## Tests added
List_Delete_node.py
List_Partition_test.py
List_duplicates_test.py
List_intersection_test.py
List_test_copy_random_pointer.py
List_test_is_sorted.py

## Output
`coverage run -m unittest discover -s testIVT -p "*.py"`
```
[False, 1, 1, 2, 1, 3, 'a', 0, 0]
A -> B -> C -> D -> F -> G
A -> B -> C -> D -> F -> G
..........................F............F.F......................
======================================================================
FAIL: test_partition (List_Partition_test.TestPartition.test_partition)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\testIVT\List_Partition_test.py", line 29, in test_partition
    self.assertEqual(current.val, val)
AssertionError: 8 != 5

======================================================================
FAIL: test_palindrome_list (List_test_is_plindrome.TestPalindromeList.test_palindrome_list)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\testIVT\List_test_is_plindrome.py", line 31, in test_palindrome_list
    self.assertTrue(is_palindrome_stack(head))
AssertionError: False is not true

======================================================================
FAIL: test_two_element_non_palindrome_list (List_test_is_plindrome.TestPalindromeList.test_two_element_non_palindrome_list)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\testIVT\List_test_is_plindrome.py", line 60, in test_two_element_non_palindrome_list
    self.assertFalse(is_palindrome_stack(head))
AssertionError: True is not false

----------------------------------------------------------------------
Ran 64 tests in 0.053s

FAILED (failures=3)
```

## Code coverage
```
Name                                           Stmts   Miss  Cover
------------------------------------------------------------------
algorithms\arrays\__init__.py                     19      0   100%
algorithms\arrays\delete_nth.py                   15      0   100%
algorithms\arrays\flatten.py                      14      0   100%
algorithms\arrays\garage.py                       18     16    11%
algorithms\arrays\josephus.py                      8      7    12%
algorithms\arrays\limit.py                         8      1    88%
algorithms\arrays\longest_non_repeat.py           63      4    94%
algorithms\arrays\max_ones_index.py               16      0   100%
algorithms\arrays\merge_intervals.py              48     34    29%
algorithms\arrays\missing_ranges.py               12     11     8%
algorithms\arrays\move_zeros.py                   10      0   100%
algorithms\arrays\n_sum.py                        64     63     2%
algorithms\arrays\plus_one.py                     30     27    10%
algorithms\arrays\remove_duplicates.py             6      5    17%
algorithms\arrays\rotate.py                       28     25    11%
algorithms\arrays\summarize_ranges.py             14     12    14%
algorithms\arrays\three_sum.py                    21     20     5%
algorithms\arrays\top_1.py                        14     13     7%
algorithms\arrays\trimmean.py                      9      8    11%
algorithms\arrays\two_sum.py                       7      6    14%
algorithms\linkedlist\__init__.py                  9      0   100%
algorithms\linkedlist\copy_random_pointer.py      27      0   100%
algorithms\linkedlist\delete_node.py              33     20    39%
algorithms\linkedlist\intersection.py             57     25    56%
algorithms\linkedlist\is_cyclic.py                15      0   100%
algorithms\linkedlist\is_palindrome.py            64     11    83%
algorithms\linkedlist\is_sorted.py                13      0   100%
algorithms\linkedlist\merge_two_list.py           23      0   100%
algorithms\linkedlist\partition.py                30      6    80%
algorithms\linkedlist\remove_duplicates.py        48      0   100%
algorithms\linkedlist\remove_range.py             13     12     8%
algorithms\linkedlist\reverse.py                  22      0   100%
algorithms\linkedlist\rotate_list.py              19      0   100%
algorithms\linkedlist\swap_in_pairs.py            18     15    17%
algorithms\stack\__init__.py                      10      0   100%
algorithms\stack\is_consecutive.py                33     30     9%
algorithms\stack\is_sorted.py                     16      1    94%
algorithms\stack\ordered_stack.py                 24     16    33%
algorithms\stack\remove_min.py                    16     15     6%
algorithms\stack\simplify_path.py                 11     10     9%
algorithms\stack\stack.py                         82     53    35%
algorithms\stack\stutter.py                       23     20    13%
algorithms\stack\switch_pairs.py                  35     32     9%
algorithms\stack\valid_parenthesis.py             10      0   100%
testIVT\Array_Test_longest.py                     33      1    97%
testIVT\Array_limit_test.py                       16      1    94%
testIVT\Array_test_delete_nth.py                  57      1    98%
testIVT\Array_test_flatten.py                     22      2    91%
testIVT\Array_test_max_ones_index.py              21      1    95%
testIVT\List_Delete_node_test.py                  27      1    96%
testIVT\List_Partition_test.py                    21      1    95%
testIVT\List_duplicates_test.py                   51      1    98%
testIVT\List_intersection_test.py                 26      1    96%
testIVT\List_is_cyclic_test.py                    32      1    97%
testIVT\List_test_copy_random_pointer.py          36      1    97%
testIVT\List_test_is_plindrome.py                 52      9    83%
testIVT\List_test_is_sorted.py                    19      1    95%
testIVT\List_test_merge_lists.py                  44      2    95%
testIVT\List_test_reverse.py                      44      2    95%
testIVT\List_test_rotate_list.py                  46      2    96%
testIVT\Stack_test_sorted_stack.py                26      1    96%
testIVT\Stack_test_valid_parenthesis.py           21      1    95%
------------------------------------------------------------------
TOTAL                                           1669    548    67%
```

More test coverage is required.

# Iteration 3: After adding more tests

## Output
`coverage run -m unittest discover -s testIVT -p "*.py"`
```
[False, 1, 1, 2, 1, 3, 'a', 0, 0]
A -> B -> C -> D -> F -> G
A -> B -> C -> D -> F -> G
............................F.F...................F.F...........................EEEE......F....FF...........................
======================================================================
ERROR: test_order_maintenance (Stack_test_ordered.TestOrderedStack.test_order_maintenance)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\testIVT\Stack_test_ordered.py", line 56, in test_order_maintenance
    self.stack.push(elem)
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\algorithms\stack\ordered_stack.py", line 21, in push
    while item < self.peek() and not self.is_empty():
                 ^^^^^^^^^^^
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\algorithms\stack\ordered_stack.py", line 33, in peek
    return self.items[len(self.items) - 1]
           ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
IndexError: list index out of range

======================================================================
ERROR: test_pop (Stack_test_ordered.TestOrderedStack.test_pop)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\testIVT\Stack_test_ordered.py", line 37, in test_pop
    self.stack.push(1)
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\algorithms\stack\ordered_stack.py", line 21, in push
    while item < self.peek() and not self.is_empty():
                 ^^^^^^^^^^^
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\algorithms\stack\ordered_stack.py", line 33, in peek
    return self.items[len(self.items) - 1]
           ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
IndexError: list index out of range

======================================================================
ERROR: test_push_and_peek (Stack_test_ordered.TestOrderedStack.test_push_and_peek)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\testIVT\Stack_test_ordered.py", line 25, in test_push_and_peek
    self.stack.push(1)
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\algorithms\stack\ordered_stack.py", line 21, in push
    while item < self.peek() and not self.is_empty():
                 ^^^^^^^^^^^
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\algorithms\stack\ordered_stack.py", line 33, in peek
    return self.items[len(self.items) - 1]
           ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
IndexError: list index out of range

======================================================================
ERROR: test_size (Stack_test_ordered.TestOrderedStack.test_size)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\testIVT\Stack_test_ordered.py", line 47, in test_size
    self.stack.push(1)
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\algorithms\stack\ordered_stack.py", line 21, in push
    while item < self.peek() and not self.is_empty():
                 ^^^^^^^^^^^
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\algorithms\stack\ordered_stack.py", line 33, in peek
    return self.items[len(self.items) - 1]
           ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
IndexError: list index out of range

======================================================================
FAIL: test_partition (List_Partition_test.TestPartition.test_partition)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\testIVT\List_Partition_test.py", line 29, in test_partition
    self.assertEqual(current.val, val)
AssertionError: 8 != 5

======================================================================
FAIL: test_remove_range_invalid_index (List_Remove_range.TestRemoveRange.test_remove_range_invalid_index)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\testIVT\List_Remove_range.py", line 67, in test_remove_range_invalid_index
    with self.assertRaises(IndexError):
AssertionError: IndexError not raised

======================================================================
FAIL: test_palindrome_list (List_test_is_plindrome.TestPalindromeList.test_palindrome_list)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\testIVT\List_test_is_plindrome.py", line 31, in test_palindrome_list
    self.assertTrue(is_palindrome_stack(head))
AssertionError: False is not true

======================================================================
FAIL: test_two_element_non_palindrome_list (List_test_is_plindrome.TestPalindromeList.test_two_element_non_palindrome_list)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\testIVT\List_test_is_plindrome.py", line 60, in test_two_element_non_palindrome_list
    self.assertFalse(is_palindrome_stack(head))
AssertionError: True is not false

======================================================================
FAIL: test_remove_min_all_same (Stack_test_remove.TestRemoveMin.test_remove_min_all_same)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\testIVT\Stack_test_remove.py", line 40, in test_remove_min_all_same
    self.assertEqual(result, expected, "Should remove only one instance of the same element.")
AssertionError: Lists differ: [] != [4, 4, 4]

Second list contains 3 additional elements.
First extra element 0:
4

- []
+ [4, 4, 4] : Should remove only one instance of the same element.

======================================================================
FAIL: test_remove_min_with_duplicates (Stack_test_remove.TestRemoveMin.test_remove_min_with_duplicates)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\testIVT\Stack_test_remove.py", line 22, in test_remove_min_with_duplicates
    self.assertEqual(result, expected, "Failed to remove only the first occurrence of the minimum value.")
AssertionError: Lists differ: [2, 3, 7, 3] != [2, 3, 1, 7, 3, 1]

First differing element 2:
7
1

Second list contains 2 additional elements.
First extra element 4:
3

- [2, 3, 7, 3]
+ [2, 3, 1, 7, 3, 1]
?        +++    +++
 : Failed to remove only the first occurrence of the minimum value.

======================================================================
FAIL: test_remove_min_with_zero (Stack_test_remove.TestRemoveMin.test_remove_min_with_zero)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\bhask\Desktop\IVTProject\repo\ivt-ha-2024-chai-baklava-group\testIVT\Stack_test_remove.py", line 65, in test_remove_min_with_zero
    self.assertEqual(result, expected, "Failed to correctly remove the first zero.")
AssertionError: Lists differ: [2, 3, 4] != [2, 3, 0, 4]

First differing element 2:
4
0

Second list contains 1 additional elements.
First extra element 3:
4

- [2, 3, 4]
+ [2, 3, 0, 4]
?        +++
 : Failed to correctly remove the first zero.

----------------------------------------------------------------------
Ran 124 tests in 0.032s

FAILED (failures=7, errors=4)
```

## Code coverage
```
Name                                           Stmts   Miss  Cover
------------------------------------------------------------------
algorithms\arrays\__init__.py                     19      0   100%
algorithms\arrays\delete_nth.py                   15      0   100%
algorithms\arrays\flatten.py                      14      0   100%
algorithms\arrays\garage.py                       18      0   100%
algorithms\arrays\josephus.py                      8      7    12%
algorithms\arrays\limit.py                         8      1    88%
algorithms\arrays\longest_non_repeat.py           63      4    94%
algorithms\arrays\max_ones_index.py               16      0   100%
algorithms\arrays\merge_intervals.py              48     34    29%
algorithms\arrays\missing_ranges.py               12     11     8%
algorithms\arrays\move_zeros.py                   10      0   100%
algorithms\arrays\n_sum.py                        62     61     2%
algorithms\arrays\plus_one.py                     30     27    10%
algorithms\arrays\remove_duplicates.py             6      5    17%
algorithms\arrays\rotate.py                       28     25    11%
algorithms\arrays\summarize_ranges.py             14     12    14%
algorithms\arrays\three_sum.py                    21     20     5%
algorithms\arrays\top_1.py                        13     12     8%
algorithms\arrays\trimmean.py                      9      8    11%
algorithms\arrays\two_sum.py                       7      6    14%
algorithms\linkedlist\__init__.py                  9      0   100%
algorithms\linkedlist\copy_random_pointer.py      27      0   100%
algorithms\linkedlist\delete_node.py              33     20    39%
algorithms\linkedlist\intersection.py             57     25    56%
algorithms\linkedlist\is_cyclic.py                15      0   100%
algorithms\linkedlist\is_palindrome.py            64     11    83%
algorithms\linkedlist\is_sorted.py                13      0   100%
algorithms\linkedlist\merge_two_list.py           23      0   100%
algorithms\linkedlist\partition.py                30      6    80%
algorithms\linkedlist\remove_duplicates.py        48      0   100%
algorithms\linkedlist\remove_range.py             17      0   100%
algorithms\linkedlist\reverse.py                  22      0   100%
algorithms\linkedlist\rotate_list.py              19      0   100%
algorithms\linkedlist\swap_in_pairs.py            18      0   100%
algorithms\stack\__init__.py                      10      0   100%
algorithms\stack\is_consecutive.py                33      4    88%
algorithms\stack\is_sorted.py                     16      1    94%
algorithms\stack\ordered_stack.py                 24      3    88%
algorithms\stack\remove_min.py                    15      0   100%
algorithms\stack\simplify_path.py                 11      0   100%
algorithms\stack\stack.py                         82     53    35%
algorithms\stack\stutter.py                       23      0   100%
algorithms\stack\switch_pairs.py                  35      0   100%
algorithms\stack\valid_parenthesis.py             10      0   100%
testIVT\Array_Test_longest.py                     33      1    97%
testIVT\Array_garage_test.py                      23      1    96%
testIVT\Array_limit_test.py                       16      1    94%
testIVT\Array_test_delete_nth.py                  57      1    98%
testIVT\Array_test_flatten.py                     22      2    91%
testIVT\Array_test_max_ones_index.py              21      1    95%
testIVT\List_Delete_node_test.py                  27      1    96%
testIVT\List_Partition_test.py                    21      1    95%
testIVT\List_Remove_range.py                      52      8    85%
testIVT\List_duplicates_test.py                   51      1    98%
testIVT\List_intersection_test.py                 26      1    96%
testIVT\List_is_cyclic_test.py                    32      1    97%
testIVT\List_swap_pairs_test.py                   52      1    98%
testIVT\List_test_copy_random_pointer.py          36      1    97%
testIVT\List_test_is_plindrome.py                 52      9    83%
testIVT\List_test_is_sorted.py                    19      1    95%
testIVT\List_test_merge_lists.py                  44      2    95%
testIVT\List_test_reverse.py                      44      2    95%
testIVT\List_test_rotate_list.py                  46      2    96%
testIVT\Stack_test_is_consecutive.py              54      1    98%
testIVT\Stack_test_ordered.py                     51     19    63%
testIVT\Stack_test_path.py                        22      1    95%
testIVT\Stack_test_remove.py                      53      1    98%
testIVT\Stack_test_sorted_stack.py                26      1    96%
testIVT\Stack_test_stutter.py                     38      1    97%
testIVT\Stack_test_switch.py                      69      1    99%
testIVT\Stack_test_valid_parenthesis.py           21      1    95%
------------------------------------------------------------------
TOTAL                                           2083    420    80%
```

Satisfactory code coverage. 80%

# Conclusion

The Errors in test cases, and the failures hint for required code changes in the repository.