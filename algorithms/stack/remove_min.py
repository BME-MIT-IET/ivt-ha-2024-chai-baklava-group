"""
Given a stack, a function remove_min accepts a stack as a parameter
and removes the smallest value from the stack.

For example:
bottom [2, 8, 3, -6, 7, 3] top
After remove_min(stack):
bottom [2, 8, 3, 7, 3] top

"""


def remove_min(stack):
    storage_stack = []
    if len(stack) == 0:  # Stack is empty
        return stack
    # Find the smallest value
    min_val = stack.pop()
    stack.append(min_val)
    for _ in range(len(stack)):
        val = stack.pop()
        min_val = min(min_val, val)
        storage_stack.append(val)
    # Back up stack and remove min value
    for _ in range(len(storage_stack)):
        val = storage_stack.pop()
        if val != min_val:
            stack.append(val)
    return stack
