def string_to_brainfuck(input_string):
    brainfuck_code = ""

    for char in input_string:
        ascii_value = ord(char)
        brainfuck_code += "+" * ascii_value + ".>"

    return brainfuck_code

# Get input from the user
user_input = input("Enter a string: ")

# Convert input to Brainfuck code
brainfuck_code = string_to_brainfuck(user_input)

print("Brainfuck Code:")
print(brainfuck_code)
print("Original String:", user_input)
