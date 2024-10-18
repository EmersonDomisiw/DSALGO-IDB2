#Part 1 Code:
def validate_brackets(expression):
    stack = []
    bracket_set = {'(': ')', '{': '}', '[': ']'}
    encountered_brackets = []

    if expression and expression[0] in bracket_set.values():
        return False, expression[0]

    for char in expression:
        if char in bracket_set:
            stack.append(char)
            encountered_brackets.append(char)
        elif char in bracket_set.values():
            if not stack or bracket_set[stack.pop()] != char:
                encountered_brackets.append(char)
                return False, encountered_brackets
            encountered_brackets.append(char)

    return len(stack) == 0, encountered_brackets

user_expression = input("Enter a mathematical expression: ")

is_valid, brackets = validate_brackets(user_expression)
status_message = "Input is valid!" if is_valid else "Input is invalid!"
print(f"\n{status_message}: {''.join(brackets)}")


# Part 2 Code
def reverse_file_contents(source_path, destination_path):
    lines = []
    with open(source_path, 'r') as source_file:
        for line in source_file:
            lines.append(line.strip())

    with open(destination_path, 'w') as dest_file:
        for line in reversed(lines):
            dest_file.write(line + '\n')

output_file_path = 'Output.txt'
input_file_path = 'Input.txt'
reverse_file_contents(input_file_path, output_file_path)

print(f"Reversed lines from {input_file_path} have been saved to {output_file_path}.")