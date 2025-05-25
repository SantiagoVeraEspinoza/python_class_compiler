#!/usr/bin/env python3

import os
import re

# Define token patterns
TOKEN_PRIORITY  = [
    # Define header
    ('dfhdr',   r'(@([a-zA-Z_][a-zA-Z0-9_]*)(\.[a-zA-Z_][a-zA-Z0-9_]*)*(\(([^()]*)\))?)*def([a-zA-Z_][a-zA-Z0-9_]*)\(((\*{0,2}[a-zA-Z_][a-zA-Z0-9_]*(:[a-zA-Z_][a-zA-Z0-9_]*)?(=[\w\d\"\'\{\}\[\],]+)?)(,(\*{0,2}[a-zA-Z_][a-zA-Z0-9_]*(:[a-zA-Z_][a-zA-Z0-9_]*)?(=[\w\d\"\'\{\}\[\],]+)?))*)?\):'),
    # Class header
    ('clshdr',  r'class([a-zA-Z_][a-zA-Z0-9_]*)(\((,?([a-zA-Z_][a-zA-Z0-9_]*)(\.([a-zA-Z_][a-zA-Z0-9_]*))*(=([a-zA-Z_][a-zA-Z0-9_]*)(\.([a-zA-Z_][a-zA-Z0-9_]*))*)?)+\))?:'),
    ('code',    r'.+'),                                                                     # Code blocks
]

# Compile regexes for each token type
TOKEN_REGEXES = [(kind, re.compile(pattern)) for kind, pattern in TOKEN_PRIORITY]

def obtain_stripped_python_code(content, is_path=True):
    raw_code = content
    if is_path:
        if not os.path.exists(content) or not os.path.isfile(content):
            raise FileNotFoundError(f"File at '{content}' does not exist or is not a file")
    
        with open(content, 'r') as file:
            raw_code = file.read()
            file.close()
    
    clean_code = raw_code.replace(" ", "").replace("\t", "").replace("\n", "")
    return clean_code
    
def tokenize(content, is_path=True, include_code=False):
    text = obtain_stripped_python_code(content, is_path)

    matches = []
    matched_indices = set()

    # Match tokens in priority order
    for kind, regex in TOKEN_REGEXES:
        for match in regex.finditer(text):
            start, end = match.span()

            # Skip overlapping matches
            if any(i in matched_indices for i in range(start, end)):
                continue

            value = match.group()
            matches.append((start, end, kind, value))
            matched_indices.update(range(start, end))

    # Sort matches by start position
    matches.sort()

    # Now fill the code gaps
    tokens = []
    last_end = 0
    for start, end, kind, value in matches:
        if start > last_end:
            gap_value = text[last_end:start]
            tokens.append(('code', gap_value))
        tokens.append((kind, value))
        last_end = end

    # If there's trailing code after the last match
    if last_end < len(text):
        tokens.append(('code', text[last_end:]))

    if not include_code:
        tokens = [token[0] for token in tokens]

    return tokens

# code = obtain_stripped_python_code('examples/classful.py')
# for token in tokenize(code):
#     print(token[0], end=" ")


    