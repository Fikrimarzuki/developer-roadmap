# WORKING WITH STRINGS

# Bersifat immutable
name = "John"


# CARA MENULIS
# Single Quotes
name = 'Single'

# Double Quotes
name = "Double"

# Triple Quotes
bio = """
Halo, nama saya adalah Triple Quotes.
Saya sedang belajar bahasa Python.
"""


# STRING CONCATENATION
first = "Hello"
last = "World"
full = first + " " + last


# STRING INTERPOLATION
name = "Pythonia"
age = 25

greeting = f"Hello {name}, you are {age} years old"
print(greeting)
# Output: Hello Pythonia, you are 25 years old


# STRING LENGTH
# len()
text = "Hello"
print(len(text)) # 5


# ACCESS CHARACTER BY INDEX
text = "Python"
print(text[0]) # P
print(text[-1]) # n (last char)


# STRING SLICING
text = "Python"
# variabel[start : end : step]
# start -> mulai dari index ke berapa
# end -> sampai index ke berapa (Tidak inklusif)
# step -> melangkah berapa karakter per langkah (default 1)
print(text[0:3]) # Pyt -> mulai dari index 0 sampai sebelum index 3
print(text[2:]) # thon -> mulai dari index 2 sampai terakhir
print(text[-3:]) # hon -> mulai dari karakter ke 3 terakhir sampai terakhir
print(text[:4]) # Pyth -> mulai dari index 0 sampai sebelum index 4
print(text[::-1]) # nohtyP -> reverse string
# mulai dari index 0, sampai index terakhir, step -1 berarti mulai dari belakang mundur tiap 1 karakter
print(text[::-2]) # nhy -> reverse string
# mulai dari index 0, sampai index terakhir, step -1 berarti mulai dari belakang mundur tiap 2 karakter
# karena step -2, maka mulai dari index terakhir n, karena step 2 maka huruf o akan dilewati, lalu berikutnya huruf h, dst...


# IMPORTANT STRING METHODS
# Lowercase/Uppercase
"HELLO".lower()
"hello".upper()

# Replace
"Hello guys".replace("guys", "world")

# Split
"apple,banana,orange".split(",")

# Join
",".join(["a","b","c"])


# CHECK SUBSTRING
if "py" in "python":
  print("found")


# STRING WHITESPACE
"    hello    ".strip()
"hello\n".strip()


# ESCAPE CHARACTERS
text = "He said \"Hello\""
text = 'He said "Hello"'


