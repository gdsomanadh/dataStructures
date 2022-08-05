import stack


def reverse_string_stack():
    input_string = "Dheeraj is Great"
    reversed_string = ""
    s = stack.Stack()

    for char in input_string:
        s.push(char)
    while not s.isEmpty():
        reversed_string += s.pop()
    return reversed_string


if __name__ == "__main__":
    rev_string = reverse_string_stack()
