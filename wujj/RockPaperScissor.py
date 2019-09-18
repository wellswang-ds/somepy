import random
print("Hey, I am Kayvan!")
user=input("What is your name?")

check=input("Do you want to play paper/rock/scissor game with me? (yes/no)")
kayvanC=0
userC=0
while check=="yes":
  userpick=input("Please select one of the Rock(r)/Paper(p)/Scissor(s).")
  items=["p","r","s"]
  kayvanpick=random.choice(items)
  print("Kayvan selected", kayvanpick)
  print("User selected", userpick)
  if kayvanpick==userpick:
    print("It is a tie.")
  elif(kayvanpick=='p' and userpick=='s')or(kayvanpick=='r' and userpick=='p')or(kayvanpick=='s' and userpick=='r'):
    print("User won!")
    userC+=1 #add one to the variable userC
  else:
    print("Kayvan won!")
    kayvanC+=1 #add one to the variable kayvanC
  print('Kayvan won: ', kayvanC)
  print('You won: ', userC)
  check=input("Do you want to play again? (yes/no)")
print("Good game! See you next time!")