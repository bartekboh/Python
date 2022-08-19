import passes

def log_in():
  log = input("Login:")
  pas = input("Password:")

  passes_in = {"pas_in": (log, pas)}

  global user

  if passes.admin["pas"] == passes_in["pas_in"]:
    user = "admin"
    return user
  if passes.bartek["pas"] == passes_in["pas_in"]:
    user = "bartek"
    return user
  else:
    print("Incorrect login or password!")



