from random import choice    #importing choice from random module
from datetime import datetime  #importing datetime from datetime module

print("Project: Rock Paper Scissor Game")  #showing date and time of creation
print("Project Created On:",datetime(2024,9,9,13,36))
print("")

l=["Rock", "Paper", "Scissor"]  # defining list to be choosen by choice function

while True:   #running a loop infinitly untill break is not used

  c=int(input('''Game Start....
           1.Play
           2.Exit
        '''))
  
  if c == 2:
   break

  elif c != 1 and c != 2:
   print("Error - choose from 1 & 2 only")
  
  elif c == 1:
   ucount=0
   ccount=0
   for a in range(1,6):
    uc=int(input('''
            1. Rock
            2. Paper
            3. Scissor
        Note - Only Input integer Value as choice
'''))
    if uc==1:
     uchoice="Rock"
    elif uc==2:
     uchoice="Paper"
    elif uc==3:
     uchoice="Scissor"
    
    cchoice=choice(l)
   
    if uchoice==cchoice:
     print("Match DRaW")
     print("Your Choice: ", uchoice)
     print("Computer Choice: ", cchoice)
     ucount+=1
     ccount+=1

    elif (uchoice=="Rock" and cchoice=="Scissor") or (uchoice=="Paper" and cchoice=="Rock") or (uchoice=="Scissor" and cchoice=="Paper"):
     print("YOu Win>...!")
     print("Your Choice: ", uchoice)
     print("Computer Choice: ", cchoice)
     ucount+=1

    else:
     print("Computer Won...!")
     print("Your Choice: ", uchoice)
     print("Computer Choice: ", cchoice)
     ccount+=1

   print(" ")
   if ucount == ccount:
    print("Game is Draw")
    print("Your Winnings: ", ucount)
    print("Computer Winnings: ", ccount)

   elif ucount > ccount:
    print("Hurrey..! You Won the Game")
    print("Your Winnings: ", ucount)
    print("Computer Winnings: ", ccount)

   elif ucount < ccount: 
    print("Computer Won the Game")
    print("Computer Winnings: ", ccount)
    print("Your Winnings: ", ucount)

  