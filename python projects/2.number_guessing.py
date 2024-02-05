import random

top_of_range = input("Type a number: ")
# returns a string

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type a number greater than 0 next time.")
        quit()
        
else:
    print("Please enter a number next time.")
    
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    answer = input("Make a guess. ")
    if answer.isdigit():
        answer = int(answer)
    else:
        print("Please enter a number next time.")
        continue
    
    if answer == random_number:
        print("You guessed it correct!")
        break
    elif answer > random_number:
        print("You were above the number.")
    else:
        print("You were below the number.")

print("You got it in ", guesses, "guesses.")

'''
#does not include 11
r1 = random.randrange(-5, 11)

#to include 11
r2 = random.randint(-5, 11)

print(r1, r2)
'''