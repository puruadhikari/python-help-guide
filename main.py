s = "3[a]12[bc]"
# Output: "aaabcbc"

count_stack = []
string_stack = []

current_string = ""
current_count = 0

for char in s:
    if char.isdigit():
        current_count = int(current_count)*10+int(char)
    elif char == "[":
        string_stack.append(current_string)
        count_stack.append(current_count)

        current_count = 0
        current_string = ""
    elif char == "]":
        number = count_stack.pop()
        previous_string = string_stack.pop()
        current_string = previous_string + current_string * number
    else:
        current_string += char

print(current_string)