#task
user_Role = "user"
security_Clearance = 4
watch_List = True
if user_Role == "admin" or security_Clearance > 4 and watch_List == False:
  print("Access Granted")
else:
  print("Access Denied")