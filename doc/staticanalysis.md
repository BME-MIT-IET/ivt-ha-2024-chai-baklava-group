# Static Analysis Report

## Project Overview

- **Project Name:** IVTHomework
- **Language:** Python
- **Repository:** [GitHub - IVT Homework](https://github.com/BME-MIT-IET/ivt-ha-2024-chai-baklava-group.git)

## Summary

This report presents the results of static analysis performed on the IVT Homework codebase. Static analysis tools were used to inspect the source code for potential issues related to code quality, security vulnerabilities, and adherence to coding standards.

## Tools Used

The following static analysis tools were used:

- **Pylint:** A Python static code analysis tool that checks for errors, enforces coding standards, and detects code smells.

## Findings

### Pylint Analysis

- **Total Files Analyzed:** 49
- **Every file inside arrays,linkedlist and stack folders.**

#### Top Issues Identified Before fixes were made:
#### Overview:-
In the recent code quality analysis, several issues were identified across different modules and scripts. These issues encompass various aspects including documentation, coding standards, and optimization opportunities. This report provides a summary of the top issues identified before fixes were made, along with the respective ratings given by pylint.


1. **Arrays file:**
   - File `arrays.rotate`:
     - **Issue:** Unused variable 'i' and missing function/method docstring.
     - **Rating:** 9.29/10

   - File `arrays.init`:
     - **Issue:**  Missing final newline and missing module docstring.
     - **Rating:** 8.95/10

    - File `arrays.delete_nth`:
   - **Issue:** Missing function/method docstring.
   - **Rating:** 8.67/10

- File `arrays.flatten`:
   - **Issue:** Trailing whitespace and missing function/method docstring.
   - **Rating:** 8.57/10

- File `arrays.garage`:
   - **Issues:** Trailing whitespace, missing final newline, missing function/method docstring, using range and len instead of enumerate, and a pointless string statement.
   - **Rating:** 6.67/10

- File `arrays.longest_non_repeat`:
   - **Issue:** Redefining built-in 'dict' and consider using enumerate instead of range and len.
   - **Rating:** 9.21/10

- File `arrays.n_sum`:
   - **Issues:** Redefining name 'n_sum' from outer scope and unnecessary "elif" after "return".
   - **Rating:** 9.69/10

- File `arrays.max_ones_index`:
   - **Issue:** Missing function/method docstring.
   - **Rating:** 9.38/10

- File `arrays.merge_intervals`:
   - **Issues:** Disallow trailing comma tuple and formatting a regular string which could be an f-string.
   - **Rating:** 9.57/10

- File `arrays.josephus`:
   - **Issues:** Unnecessary parens after '=' keyword and missing function/method docstring.
   - **Rating:** 7.50/10

- File `arrays.two_sum`:
   - **Issues:** Missing function/method docstring and unnecessary "else" after "return".
   - **Rating:** Not provided

- File `arrays.top_1`:
   - **Issues:** Trailing whitespace, missing final newline, missing function/method docstring, and considerations for better dictionary iteration.
   - **Rating:** 5.71/10

- File `arrays.move_zeros`:
   - **Issues:** Bad indentation, trailing whitespace, missing final newline, missing function/method docstring, and using type() instead of isinstance().
   - **Rating:** 2.00/10

2. **Linkedlist file:**

- File `linkedlist.add_two_numbers`:
   - **Issues:** Missing docstrings, redefining built-in 'sum', inconsistent return statements.
   - **Rating:** 8.92/10

- File `linkedlist.copy_random_pointer`:
   - **Issues:** Missing class/docstring, useless object inheritance, too few public methods, and a recommendation for using '{}' instead of a call to 'dict'.
   - **Rating:** 8.52/10

- File `linkedlist.kth_to_last`:
   - **Issues:** Missing module/class/docstrings, unnecessary "else" after "return", use of eval, and formatting regular strings which could be f-strings.
   - **Rating:** 8.54/10

- File `linkedlist.linkedlist`:
   - **Issues:** Missing module/class/docstrings, useless object inheritance, and too few public methods.
   - **Rating:** 2.22/10

- File `linkedlist.remove_range`:
   - **Issues:** Unnecessary parens after 'assert', missing function/method docstring, comparison with None using '!=' instead of 'is not', and an unused variable.
   - **Rating:** Not provided

3. **Stack file:**

- File `stack.remove_min`:
   - **Issues:** Missing function/method docstring, redefining built-in 'min', unnecessary if block, and an unused variable.
   - **Rating:** 7.50/10

#### Top Issues After fixes were made:
### Arrays File:

#### arrays.rotate.py
- **Fixed:**
  - Added a missing function docstring.
- **Linting Score:** 9.64/10

#### __init__.py
- **Fixed:**
  - Added a module docstring and included a final newline.
- **Linting Score:** 10.00/10

#### delete_nth.py
- **Fixed:**
  - Added function docstrings to both functions.
- **Linting Score:** 10.00/10

#### flatten.py
- **Fixed:**
  - Added a function docstring and removed trailing whitespace.
- **Linting Score:** 10.00/10

#### garage.py
- **Fixed:**
  - Added a function docstring and removed trailing whitespace.
- **Linting Score:** 8.89/10

#### longest_non_repeat.py
- **Fixed:** Nothing.
- **Linting Score:** N/A

#### n_sum.py
- **Fixed:**
  - Removed unnecessary "elif" after return statement.
- **Linting Score:** 9.84/10

#### max_ones_index.py
- **Fixed:**
  - Added docstring for the max_ones_index function.
- **Linting Score:** 10.00/10

#### merge_intervals.py
- **Fixed:**
  - Consider using f-strings in the __repr__ method. Addressed the trailing comma tuple issue.
- **Linting Score:** 10.00/10

#### josephus.py
- **Fixed:**
  - Added missing function.
- **Linting Score:** 8.75/10

#### two_sum.py
- **Fixed:**
  - Added missing function and removed unnecessary "else”.
- **Linting Score:** 10.00/10

#### top_1.py
- **Fixed:**
  - Removed trailing whitespaces. Consider using .items() in line 30 to directly iterate over key-value pairs, and iterate over the dictionary directly instead of calling .keys().
- **Linting Score:** 10.00/10

#### move_zeros.py
- **Fixed:** Nothing.
- **Linting Score:** 10.00/10

### Linkedlist File:

#### copy_random_pointer.py
- **Fixed:**
  - Removed useless object inheritance, used '{}' instead of a call to 'dict’.
- **Linting Score:** 9.26/10

#### kth_to_last.py
- **Fixed:**
  - Removed eval usage and addressed too few public methods issue.
- **Linting Score:** 9.71/10

#### linkedlist.py
- **Fixed:**
  - Added missing module and class docstrings, and addressed the too few public methods issue.
- **Linting Score:** 7.78/10

#### remove_range.py
- **Fixed:**
  - Added missing function docstring.
- **Linting Score:** 9.23/10

### Stack File:

#### remove_min.py
- **Fixed:**
  - Added missing function docstring.
- **Linting Score:** 9.33/10


## Recommendations

Based on the findings from the static analysis, the following recommendations are provided:

1. **Address High Severity Issues Immediately:**
   - Resolve undefined variables, line length violations, and other high severity issues identified by Pylint.

2. **Review and Improve Coding Standards:**
   - Ensure consistency in naming conventions, import usage, and code formatting.
   - Use descriptive variable and function names to improve code readability.

3. **Regularly Perform Static Analysis:**
   - Integrate static analysis tools into the development workflow to catch issues early and maintain code quality over time.

## Conclusion

Static analysis is an essential part of the software development process, helping to identify potential issues and improve code quality. By addressing the findings highlighted in this report and adopting best practices for static analysis, the IVTHomework codebase can be strengthened and made more resilient to security threats and code defects.