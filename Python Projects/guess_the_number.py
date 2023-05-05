import random

def user_guess(x):
  random_number = random.randint(1,x)
  while True:
    guess = int(input('Enter your guess here:- '))
    if guess == random_number:
        print("You guessed correctly")
        break
    elif guess < random_number:
       print("Guess higher")
       continue
    elif guess > random_number:
       print("Guess higher")
       continue

def computer_guess(x):
   low = 1
   feedback = input(f'My guess is {low} \n')
   while True:
      if feedback == 'u':
         low = random.randint(low,x)
         feedback = input(f'My guess is {low} \n')
         continue
      elif feedback == 'd':
         low = random.randint(1,low)
         feedback = input(f'My guess is {low} \n')
         continue
      elif feedback == 'c':
         print("Yay!!!! I won!!! Bye.")
         break
      elif feedback == 's':
         break




# user_guess(4)
computer_guess(10)