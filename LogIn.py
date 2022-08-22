import passes
global user
def log_in():

  log = input("Login:")
  pas = input("Password:")


  global user
  global user_log

  if passes.admin.log == log and passes.admin.pas == pas:
    user = passes.admin
  if passes.bartek.log == log and passes.bartek.pas == pas:
    user = passes.bartek
  # if passes.User3.log == log and passes.User3.pas == pas:
  #   user = passes.User3

  try:
    print("Hello " + user.log)
  except:
    print("Incorrect login or password!")







