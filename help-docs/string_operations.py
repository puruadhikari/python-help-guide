# Basic String Operations
s = "Hello, World!"

len(s)                 # Get length of string
s.lower()              # Convert to lowercase
s.upper()              # Convert to uppercase
s.title()              # Convert to title case
s.capitalize()         # Capitalize first letter
s.strip()              # Remove leading/trailing whitespace
s.replace("World", "Python")  # Replace substring
s.split(", ")          # Split string by delimiter
",".join(["Hello", "World"])  # Join list into string with delimiter

# String Indexing and Slicing
s[0]                   # Access first character
s[-1]                  # Access last character
s[0:5]                 # Slice string (from index 0 to 4)
s[:5]                  # Slice from start to index 4
s[7:]                  # Slice from index 7 to end
s[::-1]                # Reverse string

# String Formatting
name = "Alice"
age = 30
f"Name: {name}, Age: {age}"  # f-string formatting
"Name: {}, Age: {}".format(name, age)  # format() method
"Name: %s, Age: %d" % (name, age)      # Old-style formatting

# String Checks
s.startswith("Hello")  # Check if string starts with substring
s.endswith("!")        # Check if string ends with substring
s.isalpha()            # Check if all characters are alphabetic
s.isdigit()            # Check if all characters are digits
s.isalnum()            # Check if all characters are alphanumeric

# Finding Substrings
s.find("World")        # Find index of first occurrence
s.rfind("o")           # Find index of last occurrence
s.count("l")           # Count occurrences of substring

# String Encoding and Decoding
s.encode('utf-8')      # Encode string to bytes
b = b"Hello, World!"
b.decode('utf-8')      # Decode bytes to string