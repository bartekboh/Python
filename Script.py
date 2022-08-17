
admin = {
  "pas":("admin", "admin"),
  #"log": "admin",
  #"pas": "admin",
  "access": "full",
  "name": "admin"
}

bartek = {
  "pas":("bartek123","bartek123"),
  #"log": "bartek123",
  #"pas": "bartek123",
  "access": "limited",
  "age": "17",
  "height": "184",
}

log = input("Login:")
pas = input("Password:")

if log == admin["pas"][0] and pas == admin["pas"][1]:
  user = admin
elif log == bartek["pas"][0] and pas == bartek["pas"][1]:
  user = bartek

try:
  print("Hello " + user["pas"][0])
except:
  print("Invalid login or password!")

print("Your access is: " + user["access"])
