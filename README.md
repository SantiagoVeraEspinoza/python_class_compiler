# Syntax and Lexical Analyzer

This project contains a simple **LL(1) syntax analyzer** and a corresponding **lexical analyzer** for a subset of Python-like code. The tools parse code files or directories and identify tokens such as function headers, class headers, and general code blocks. With this it effectively differentiates between classful and classless Python code.

---

## Features

- **Lexical Analyzer:**
  - Uses prioritized regular expressions to tokenize input.
  - Supports detection of function headers (`dfhdr`), class headers (`clshdr`), and generic code (`code`).
  - Handles file input or raw code strings.
  - Manages overlapping matches and fills gaps with `'code'` tokens.
  
- **Syntax Analyzer:**
  - Implements an LL(1) parser using a parsing table.
  - Supports non-terminals and terminals with epsilon (`ε`) productions.
  - Can parse individual files or entire directories.
  - Configurable output and error message visibility.
  
---

## Usage

### Lexical Analyzer

- **Tokenize a file or string**

```python
import lexical_analizer as lexer

# Tokenize from a file
tokens = lexer.tokenize('examples/sample.py', is_path=True)

# Tokenize from a string
code_string = '''
def foo(x, y):
    return x + y
'''
tokens = lexer.tokenize(code_string, is_path=False)
```

#### Token output

- By default, returns a list of token types, e.g. ['dfhdr', 'code', ...]
- To include token lexemes, use include_code=True.

### Syntax Analyzer

- **Parse a single file**

```python
import sintax_analizer as parser

result = parser.parse('examples/sample.py', is_path=True)
if result:
    print("Syntax accepted!")
else:
    print("Syntax error found.")
```

- **Parse all files in a directory**

```python
import sintax_analizer as parser

results = parser.parse_directory('examples/')
for filename, accepted in results.items():
    print(f"{filename}: {'Accepted' if accepted else 'Rejected'}")
```

## Implementation Notes

### Lexical Analyzer Details

- Uses regex patterns with priority to match tokens.
- Handles non-overlapping matches to prevent conflicting tokens.
- Currently strips all whitespace before tokenizing — this can be adjusted for better accuracy.
- Overlapping and unmatched code segments are labeled as 'code'.
- Regexes are designed for simplified detection of Python function and class headers.

### Syntax Analyzer Details

- Implements a stack-based LL(1) parser with a parsing table.
- Uses epsilon ('e') to represent empty productions.
- Checks token matches step-by-step and reports errors when no matching rule is found.
- Supports optional verbose output and error display.
- Works with tokens produced by the lexical analyzer.

## Potential Improvements

- Preserve whitespace in lexical analyzer to better support Python syntax.
- Simplify and modularize regexes for maintainability.
- Include token lexeme values consistently for richer parsing.
- Add line and column tracking for better error messages.
- Write unit tests for both lexical and syntax analyzers.
- Consider leveraging Python's built-in tokenize or ast modules for more robust parsing.

## Installation

This project requires Python 3 and no external dependencies.

Clone the repository or copy the source files at the level of your desired code:
```
git clone <repository_url>
cd <repository_dir>
```
