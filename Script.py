admin = {
  "pas": ("admin", "admin"),
  "access": "full",
  "name": "admin"
}

bartek = {
  "pas": ("bartek123", "bartek123"),
  "access": "limited",
  "age": "17",
  "height": "184",
}


def log_in():
  log = input("Login:")
  pas = input("Password:")

  global user

  if log == admin["pas"][0] and pas == admin["pas"][1]:
    user = admin
  elif log == bartek["pas"][0] and pas == bartek["pas"][1]:
    user = bartek


log_in()

try:
  print("Hello " + user["pas"][0])
  print("Your access is: " + user["access"])
except:
  print("Invalid login or password!")
