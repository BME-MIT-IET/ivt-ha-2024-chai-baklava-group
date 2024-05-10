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
Current coverage: 60%.