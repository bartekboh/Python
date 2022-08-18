admin = {
  "pas": ("admin", "admin"),
  "access": "full",
  "username": "admin"
}

bartek = {
  "pas": ("bartek123", "bartek123"),
  "access": "limited",
  "username": "Bartek"
}


def log_in():
  log = input("Login:")
  pas = input("Password:")

  passes_in = {"pas_in": (log,pas)}
  
  global user

  if admin["pas"] == passes_in["pas_in"]:
    user = admin
  if bartek["pas"] == passes_in["pas_in"]:
    user = bartek


log_in()

try:
  print("Hello " + user["pas"][0])
  print("Your access is: " + user["access"])
except:
  print("Incorrect login or password!")

