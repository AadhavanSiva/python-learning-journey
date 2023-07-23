import re


def names():
    simple_string = "Amy is 5 years old, and her sister Mary is 2 years old. Ruth and Peter, their parents, have 3 kids."

    pattern = r"\b[A-Z][a-zA-Z]+\b"  # Pattern to match capitalized words

    name_list = re.findall(pattern, simple_string)
    return name_list

assert len(names()) == 4, "There are four names in the simple_string"

print(names())
len(names()) == 4
