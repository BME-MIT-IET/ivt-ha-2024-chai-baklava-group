# Unit Testing Documentation

## Introduction

Unit testing is a crucial aspect of software development that involves testing individual units or components of a program in isolation to ensure they behave as expected. In this document, we'll discuss the unit testing approach used for our project and highlight functions that are not working properly along with their error logs.

## Testing Approach

Our unit testing approach follows a systematic process to verify the correctness of individual functions and methods within our codebase. We utilize the Python `unittest` framework to create test cases for each function or method, ensuring comprehensive coverage of our codebase.

### Test Cases
- Each test case is designed to cover different scenarios, including normal inputs, edge cases, and error conditions.
- We aim to achieve high code coverage to minimize the risk of undetected bugs.

## Functions Not Working Properly

### 1. `remove_range` Function
- **Error Description:** The `remove_range` function is not properly raising an `IndexError` when provided with invalid start or end indexes.
- **Error Log:**
``` FAIL: test_remove_range_invalid_index (main.TestRemoveRange.test_remove_range_invalid_index)
Traceback (most recent call last):
File "List_Remove_range.py", line 67, in test_remove_range_invalid_index
with self.assertRaises(IndexError):
AssertionError: IndexError not raised
``` 


### 2. `is_palindrome` Function
- **Error Description:** The `is_palindrome` function is failing for certain test cases.
- **Error Log:**`

```FAIL: test_palindrome_list (main.TestPalindromeList.test_palindrome_list)
Traceback (most recent call last):
File "List_test_is_plindrome.py", line 31, in test_palindrome_list
self.assertTrue(is_palindrome_stack(head))
AssertionError: False is not true
```


### 3. `Ordered_stack` Function

- **Error Log:**`

```
algorithms\stack\ordered_stack.py", line 33, in peek
    return self.items[len(self.items) - 1]
           ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
IndexError: list index out of range
```


### 4. `find_shortest_path` Function

- **Error Log:**`

```
\Stack_test_remove.py", line 65, in test_remove_min_with_zero
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

```



## Conclusion

Unit testing plays a critical role in ensuring the reliability and correctness of our software. By identifying and addressing issues with specific functions, we can improve the overall quality of our codebase and deliver a more robust product to our users.
