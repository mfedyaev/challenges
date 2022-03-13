# Convert input string from underscore_notation or dash-notation to camelCaseNotation, leaving the 1st letter case as is

# This is purely algorithmic, bulky, hard to read, hello from 70's
def algo(text):
    print(f'Input: {text}')
    text_out: list = []
    # Create the iterator outside the loop, so it can be accessed from the loop
    i = 0
    while i < len(text):
        if text[i] == "_" or text[i] == "-":
            # Check for duplicate/sequence of "_" and "-", then skip
            while (text[i] == "_" or text[i] == "-") and i < len(text) - 1:
                i += 1
            # This is to check if the very last character in the text is "_" or "-"
            # Not quite optimal, cause the check will run many times
            if text[i] != "_" and text[i] != "-":
                text_out.append(text[i].upper())
            i += 1
        else:
            text_out.append(text[i])
            i += 1
    # Builds a string from a list
    return ''.join(text_out)


# This is using just string replace methods, no fancy RegExp
def replace(text):
    str_out = text.replace("_", " ").replace("-", " ").title().replace(" ", "")
    return str_out


# This is more contemporary (and more pythonic?) with re (RegExp)
from re import sub


def regexp(text):
    str_out = sub("_|-", " ", text).title().replace(" ", "")
    return str_out
