
admin = {
  "log": "admin",
  "pas": "admin",
  "access": "full"
}

bartek = {
  "log": "bartek123",
  "pas": "bartek123",
  "age": "17",
  "height": "184"
}

log = input("Login:")
pas = input("Password:")

if log == admin["log"] and pas == admin["pas"]:
  user = admin
elif log == bartek["log"] and pas == bartek["pas"]:
  user = bartek

try:
  print(user["log"])
except:
  print("Invalid login or password!")
  
print("Hello World!")
