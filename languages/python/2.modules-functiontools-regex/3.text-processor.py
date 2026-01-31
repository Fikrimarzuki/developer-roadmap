# TEXT PROCESSING

# REGULAR EXPRESSIONS
# Regex - pola untuk mencocokkan text
# Menggunakan builtin module re


# Match Pattern
import re

text = "My email is pythonia@example.com"

pattern = r"\w+@\w+\.\w+"

match = re.search(pattern, text)
print(match.group())

# Output:
# pythonia@example.com


# REPLACE TEXT
re.sub(r"\d+", "[NUMBER]", "Item 123 costs 456")
# Output
# Item [NUMBER] costs [NUMBER]


# FIND ALL MATCHES
re.findall(r"[A-Za-z]+", "Hello 123 World")
# Output
# ['Hello', 'World']


# PATTERNS
"""
| Pattern | Meaning         |
| ------- | --------------- |
| `\d`    | digit           |
| `\w`    | letter/number   |
| `\s`    | whitespace      |
| `+`     | one or more     |
| `*`     | zero or more    |
| `{n}`   | exactly n       |
| `{n,m}` | between n and m |
| `^`     | start           |
| `$`     | end             |
| `.`     | any char        |
"""


# CONTOH VALIDASI
# Validasi Email
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

# Validasi username
r"^[a-zA-Z0-9_]{3,20}$"

# Validasi nomor HP
r"^08[0-9]{8,10}$"

