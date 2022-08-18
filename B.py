user = ""

names = open("names.txt", "r+")

name = names.readline()

print(name)

if name == "admin":
  user = "yes"
else:
  print("bruh")


names.close()

