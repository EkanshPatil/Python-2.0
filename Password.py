Users = {
    "ghost":"boo",
    "warewolf":"woof",
    "vampire":"blood",
    "reaper":"slash",
    "zombie":"brains",
    "witch":"potions",
    "skeleton":"bones"
}

wrong = 5
while True:
 hallo = input("Enter username ")
 if hallo in Users:
  ween = input("Enter password ")
  if ween == Users[hallo]:
   print("Login succesfull!")
  else:
   print("incorrect password",wrong,"tries left!")
   wrong = wrong - 1
 else:
  print("invalid username,",wrong,"tries left!")
  wrong = wrong - 1
 if wrong == 0:
  print("Wrong password/username limit reached,closing program")
  break