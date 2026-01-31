# CONDITIONALS

# if tidak pakai kurung
# setelah kondisi ada :
# indentasi if else harus sejajar

# BASIC IF
age = 20
if age >= 18:
  print("Dewasa")


# IF + ELSE
age = 20
if age >= 18:
  print("Dewasa")
else:
  print("Dibawah umur")


# ELIF
score = 75
if score >= 90:
  print("A")
elif score >= 80:
  print("B")
elif score >= 70:
  print("C")
else:
  print("D")


# BOOLEAN EXPRESSIONS
# and, or, not
x = 15
if x > 10 and x < 20:
  print("x is between 10 and 20")


# TERNARY OPERATOR
status = "Adult" if age >= 18 else "Minor"


# COMPARING STRINGS
# case sensitive
name = "alex"
if name == "alex":
  print("yes")


# IN
# cek substring
# cek elemen list
if "py" in "python":
  print("found")

if 3 in [1,2,3]:
  print("found")


# MATCH/CASE (Python 3.10+)
# menggunakan match
# menggunakan _ untuk defaultnya
command = "start"
match command:
  case "start":
    print("Starting...")
  case "stop":
    print("Stopping...")
  case "restart":
    print("Restarting...")
  case _:
    print("Uknown command")

# match tipe data
value = "string"
match value:
  case int():
    print("integer")
  case str():
    print("string")

# match tuple
x = 0
y = 0
match (x, y):
  case (0, 0):
    print("origin")
  case (0, y):
    print("on-x-axis")

# match dict
user = { "role": "admin" }
match user:
  case {"role": "admin"}:
    print("admin user")


# ALTERNATIF MATCH CASE (Python 3.9 atau lebih lama)
# if-elif
status = "loading"
if status == "loading":
  print("loading")
elif status == "done":
  print("done")

# dictionary mapping
actions = {
  "start": lambda: print("Starting..."),
  "stop": lambda: print("Stopping...")
}
action = actions.get("start", lambda: print("Unknow"))
action()