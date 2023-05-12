from time import sleep
from colorama import Fore 
import random
import sys

# starting text
print(
    "----------------------------------------\n")
    
for char in "         welcome to 🤜 🫱 ✌️\n":
  sleep(0.1)
  sys.stdout.write(char)
  sys.stdout.flush()
print("\n----------------------------------------\n"
      )



def game(): #game system
  
# defining another global variable 
  global victory
  victory = 0
  
  user_move = str(input("----------------------------------------\n" + "what do you choose? (rock/paper/scissors): "))
  print("----------------------------------------\n")

  if user_move == "rock" or user_move == "paper" or user_move == "scissors": #input validator
    pass
  else: #invalid input handler
    print(
      """\n    --------------------------\n
        thats not possible! 🚩\n
      --------------------------\n"""
        )
    game()
    return
        

#cpu move picker
  moves = ["rock", "paper", "scissors"]

  cpu_move = random.choice(moves)

  for char in ("\nopponent chose: " + cpu_move):
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()


# deciding the result 
  if user_move == cpu_move:
    print(Fore.BLUE +
      "\n--------------------------\n"
            "Thats a draw 🖖\n"
      "--------------------------\n" + Fore.RESET
        )
    return
  elif user_move == "rock" and cpu_move == "paper" or user_move == "paper" and cpu_move == "scissor" or user_move == "scissor" and cpu_move == "rock":
      victory = False
      
  else:
      victory = True
      
# Displaying the results for the round 
  if victory != False and victory == True:
    print(Fore.GREEN +
      "\n--------------------------\n"
            "you win 🎊\n"
      "--------------------------\n" + Fore.RESET
        )
    return
  elif victory != True and victory == False:
    print(Fore.RED +
      "\n--------------------------\n"
            "you lost 💀\n"
      "--------------------------\n" + Fore.RESET
        )
    return
  else:
    print("\nsomething went wrong")
    quit()

# round selection system
print("----------------------------------------\n"
    "   How many rounds do you wanna play?\n"
    "----------------------------------------\n")
round_no = str(input("   (3 rounds/5 rounds/15 rounds): "))
      
print("\n----------------------------------------\n")

#input validator
if str(round_no) == "3" or str(round_no) == "5" or str(round_no) == "15":
  pass
else:
  print("\nsorry invalid input...\n")
  quit()

pr1 =  "you are playing " + str(round_no) + " rounds\n" + "3... 2... 1... Start!"
for char in pr1: #fancy character delay system
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
print("\n")

#defining some global variables for the user and the cpu 
global user
global cpu

user = 0
cpu = 0
c = 0

#game handler and score collector
def run():
  game()
  if victory == True:
    return 1
  elif victory == False:
    return 0
  else:
    pass

score = 0

# score collector
for i in range(0, int(round_no)):
  result = int(run())
  score = score + result #gets the return output from run() and adds it to the score

for char in (Fore.YELLOW + "calculating ........" + Fore.RESET):
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

sleep(2)

t = int(round_no)

#prints the final scores for the two players
print("\nuser: " + str(score))
print(" cpu: " + str(t - score))

#prints the final decision
if score > (t - score):
  fin = "\n🎊 VICTORY 🎊"
elif score < (t - int(score)):
  fin = "\n☠️ you lost ☠️"
else:
  fin = "\nIts a draw.. Tough luck"
  
for char in (Fore.LIGHTBLACK_EX + "\n-------------------------" + "\n" +Fore.MAGENTA + fin +Fore.LIGHTBLACK_EX +
      "\n \n-------------------------" + Fore.RESET):
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
