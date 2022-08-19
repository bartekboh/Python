import LogIn

LogIn.log_in()

user = LogIn.user

try:
  print("Hello " + user)
except:
  print("Incorrect login or password!")
