#!/usr/bin/env python3

import lexical_analizer as lexer
import os

# Token types
tokens = ['dfhdr', 'clshdr', 'code', '$']

# Parsing table
parse_table = {
    'S': {
        'dfhdr': ['Pre', 'Cls', 'Post'],
        'clshdr': ['Pre', 'Cls', 'Post'],
        'code': ['Pre', 'Cls', 'Post']
    },
    'Pre': {
        'dfhdr': ['Stmt', 'Pre'],
        'clshdr': ['e'],
        'code': ['Stmt', 'Pre']
    },
    'Post': {
        'clshdr': ['Cls', 'Post'],
        '$': ['e']
    },
    'Cls': {
        'clshdr': ['clshdr', 'Blck']
    },
    'Blck': {
        'dfhdr': ['Stmt', 'Blckrst'],
        'code': ['Stmt', 'Blckrst'],
    },
    'Blckrst': {
        'dfhdr': ['Stmt', 'Blckrst'],
        'clshdr': ['e'],
        'code': ['Stmt', 'Blckrst'],
        '$': ['e']
    },
    'Stmt': {
        'dfhdr': ['Func'],
        'code': ['code']
    },
    'Func': {
        'dfhdr': ['dfhdr', 'code']
    }
}

# LL(1) Parser
def parse(content, is_path=True, print_log=False):
    tokens = lexer.tokenize(content, is_path) + ['$']

    stack = ['$', 'S']
    input_pos = 0

    if print_log: print(f"{'Stack':<35} {'Input':<80} {'Action'}")
    while stack:
        top = stack.pop()
        current_token = tokens[input_pos]

        if print_log: print(f"{str(stack):<35} {str([token[0:2] for token in tokens[input_pos:]]):<80} ", end='')

        if top == current_token == '$':
            if print_log: print("ACCEPT")
            return True

        elif top in tokens:  # Terminal
            if top == current_token:
                if print_log: print(f"Match {top}")
                input_pos += 1
            else:
                if print_log: print(f"Error: expected {top}, got {current_token}")
                return False

        elif top in parse_table:  # Non-terminal
            rule = parse_table[top].get(current_token)
            if rule:
                if rule[0] != 'e':
                    stack += reversed(rule)
                if print_log: print(f"{top} → {' '.join(rule)}")
            else:
                if print_log: print(f"Error: no rule for {top} with lookahead {current_token}")
                return False
        else:
            if print_log: print(f"Unknown symbol on stack: {top}")
            return False

    return False

def parse_directory(path):
    if not os.path.exists(path or not os.path.isdir(path)):
        raise FileNotFoundError(f"Unable to find path '{path}'. Provide a valid directory path")
    
    parse_results = {}
    for file in os.listdir(path):
        full_path = os.path.join(path, file)

        if not os.path.exists(full_path) or not os.path.isfile(full_path):
            continue

        parse_results[file] = parse(full_path, is_path=True)

    return parse_results

print(parse_directory('examples'))