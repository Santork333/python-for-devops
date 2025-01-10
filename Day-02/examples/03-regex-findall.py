import re

text = "Python is great. Python is fun."
pattern = r"Python"

# Using re.findall to find all occurrences of the pattern
matches = re.findall(pattern, text)

# Adding an if-else condition to handle matches
if matches:
    print("Matches found:", matches)
else:
    print("No matches found.")
