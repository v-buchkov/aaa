"""Task 1"""
class Stack:
    def __init__(self, initial_stack: list):
        self.stack = initial_stack

    def push(self, n: int):
        self.stack.append(n)

    def pop(self):
        return self.stack.pop(-1)

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def check(self):
        try:
            return self.stack[-1]
        except IndexError:
            return False


def validate_pushed_popped(pushed: list, popped: list) -> bool:
    if len(pushed) != len(popped) or set(pushed) != set(popped):
        return False

    pushed.reverse()
    popped.reverse()

    stack = Stack([pushed[-1]])
    pushed.pop(-1)
    while len(pushed) > 0 and len(popped) > 0:
        if not stack.is_empty():
            if popped[-1] != stack.check():
                stack.push(pushed[-1])
                pushed.pop(-1)
            else:
                stack.pop()
                popped.pop(-1)
        else:
            stack.push(pushed[-1])
            pushed.pop(-1)

    final_stack = stack.stack
    if len(final_stack) != len(popped) or set(final_stack) != set(popped):
        return False
    else:
        if final_stack == popped:
            return True
        else:
            return False


def solution():
    pushed = list(map(int, input().split()))
    popped = list(map(int, input().split()))
    result = validate_pushed_popped(pushed, popped)
    print(result)


solution()

"""Task 2"""
# def calculate_stock_spans(prices: list) -> list:
#     spans = []
#     for i in range(1, len(prices) + 1):
#         span = 1
#         j = 1
#         while j < i:
#             if prices[i - 1] >= prices[i - j - 1]:
#                 previously_higher = spans[-j]
#                 span += previously_higher
#                 j += previously_higher
#             else:
#                 break
#         spans.append(span)
#     return spans
#
#
# def solution():
#     prices = list(map(int, input().split()))
#     spans = calculate_stock_spans(prices)
#     print(' '.join(map(str, spans)))
#
#
# solution()
