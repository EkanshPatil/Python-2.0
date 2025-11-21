import random

tries = 1
column  = random.randint(1,10)
row = random.randint(1,10)
column2 = random.randint(1,10)
row2 = random.randint(1,10)
column3 = random.randint(1,10)
row3 =random.randint(1,10)
score = 30
treasure1 = 0
treasure2 = 0
treasure3 = 0

print("Welcome to the treasure hunt game!")
while True:
    
 print("_ _ _ _ _ _ _ _ _ _") 
 print("_ _ _ _ _ _ _ _ _ _") 
 print("_ _ _ _ _ _ _ _ _ _")   
 print("_ _ _ _ _ _ _ _ _ _")   
 print("_ _ _ _ _ _ _ _ _ _")   
 print("_ _ _ _ _ _ _ _ _ _")
 print("_ _ _ _ _ _ _ _ _ _")
 print("_ _ _ _ _ _ _ _ _ _")
 print("_ _ _ _ _ _ _ _ _ _")
 print("_ _ _ _ _ _ _ _ _ _")
 
        

 col = int(input("Enter your guess for the column (enter a number from 1-10) "))
 ro = int(input("Enter your guess for the row (Enter a number from 1-10) "))

 if col > 10 or col < 1 or ro > 10 or ro < 1:
    print("Invalid number entered PLEASE ENTER A NUMBER BETWEEN 1 AND 10 WHICH IS 1,2,3,4,5,6,7,8,9 OR 10 AND DO NOT INCLUDE THE COMMAS")
 
 if ro == row and col == column: 
    print("Congratulations you found the first treasure in",tries,"tries! Find the rest to win!")
    treasure1 = treasure1 + 1
   
 if ro == row2 and col == column2: 
    print("Congratulations you won found the second treasure in",tries,"tries!, Find the rest to win!")
    treasure2 = treasure2 + 1 

 if ro == row3 and col == column3: 
    print("Congratulations you found the third treasure in",tries,"tries! Find the rest to win!")
    treasure3 = treasure3 + 1
 
 if treasure1 > 1 and treasure2 > 1 and treasure3 > 1:
   print("Congratulations you won the game in ",tries,"Tries! your score is:",score,"Points (30 max)")
   break

 if col != row or col != column:
  if col > column:
   print(" for treasure1: Go left!")
   tries = tries + 1
   score = score - 1
  elif col < column:
   print("for treasure1: Go right!")
   tries = tries + 1
   score = score - 1
  elif ro > row:
   print("For treasure 1: Go up!")
   tries = tries + 1
   score = score - 1
  elif ro < row:
   print("For treasure1 :Go down!")
   tries = tries + 1
   score = score - 1
  

 if col != row2 or col != column2:
  if col > column2:
   print("for treasure2: Go left!")
   tries = tries + 1
   score = score - 1
  elif col < column2:
   print("for treasure2: Go right!")
   tries = tries + 1
   score = score - 1
  elif ro > row2:
   print("For treasure 2: Go up!")
   tries = tries + 1
   score = score - 1
  elif ro < row2:
   print("For treasure2: Go down!")
   tries = tries + 1
   score = score - 1
  
  
 if col != row3 or col != column3:
  if col > column3:
   print(" for treasure3: Go left!")
   tries = tries + 1
   score = score - 1
  elif col < column3:
   print("for treasure3: Go right!")
   tries = tries + 1
   score = score - 1
  elif ro > row3:
   print("For treasure 3: Go up!")
   tries = tries + 1
   score = score - 1
  elif ro < row3:
   print("For treasure3: go down!")
   tries = tries + 1
   score = score - 1


      # else:
      #       # Mark the guessed cell with 'X' and give a hint
      #       grid[guess_row][guess_col] = 'X'
      #       hint = give_hint(treasure_row, treasure_col, guess_row, guess_col)
      #       print("Hint: {}".format(hint))