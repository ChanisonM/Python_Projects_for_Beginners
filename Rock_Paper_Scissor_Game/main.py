import random
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

while True :
     print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

     choice = int(input('Enter a valid choice please : '))
     
     if choice == 1 :
          choice_name = "Rock"
     elif choice == 2 :
          choice_name = "Paper" 
     elif choice == 3 :
          choice_name = "Scissors"
    
     print("User Choice is : " , choice_name)
     print("Now it's Computer's Turn...")

     comp_choice = random.randint(1,3)
     if comp_choice == 1 :
            comp_choice_name = "Rock"
     elif comp_choice == 2:
        comp_choice_name = "Paper" 
     elif comp_choice == 3:
          comp_choice_name = "Scissors"

     print("Computer Choice is : " ,  comp_choice_name)

    # Determine the winner
     if choice == comp_choice :
          result = "DRAW"
     elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2) :
          result = "Paper"
     elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 3) :
          result = "Rock"
     elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3) :
          result = "Scissors"

    # Print the result
     if result == "DRAW" :
        print("<== It's a tie ! ==>")
     elif result == choice_name :
          print("<== User Win ==>")
     else :
          print("<== Computer Win ==>")

     print("Do you want to play agin (Y/N) ?")
     ans = input().lower()
     if ans == "n" :
          break
print("Thanks for playing!")