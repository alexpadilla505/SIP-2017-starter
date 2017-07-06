start = '''
Welcome to the first day of Choose Your Story. It's your first day of high school!
It's 6AM! You're exhausted. Should I snooze alarm for more beauty sleep or wake
up early to prep your day?
'''


print(start)


print("Type 'snooze' to Snooze alarm for more beauty sleep or 'wake up' to Wake up early to prep your day! ")
user_input = input()
if user_input == "snooze":
    print("Oh no! You woke up, now you will only have 5 minutes!") # finished the story by writing what happens
elif user_input == "wake up":
    print("You woke up! Now you have 40 minutes to get ready!") # finished the story writing what happens
print("Who do you want to sit next to? Preps or nerds?")
print("Type 'preps'to sit with the preps or 'nerds' to sit with the nerds.")
sit = input()
if sit == "preps":
    print("You are now the most popular girl in school!")
    print("Later on in the year...")
    print("The most popular preppy guy asked you on a date.")
    print("Type 'yes'to go on a date or 'no' to not go.")
    question = input()
    if question == "yes":
        print("You go on a romantic date where he offers you a drink, but something was off...")
        print("Halfway through the night, you start feeling dizzy...")
        print("SUDDENLY...")
        print("Your date motions over and leans in closer to your body. As you close your eyes he...")
        print("STABS YOU! You die. The end!")
    elif question == "no":
        print("All preps start hating you, and you get bullied a lot.")
        print("You feel like no one cares about you anymore...")
        print("You decided to stop existing in such a hellish world.")
        print("You grab a handfull of pills. You end this once and for all. You die.")

elif sit == "nerds":
    print("You are now the smartest girl in school and become valedictorian.")
    print("The nerdiest geek asked you on a date.")
    print("Type 'yes' to go on a date or 'no' to not go.")
    ask = input()
    if ask == "yes":
        print ("He takes you on a romantic date to Pixar...")
        print("You meet your favorite director...")
        print("who offers you an internship at Pixar!!!")
        print("You enjoyed your night and continue dating him until marriage. The end!")
    elif ask == "no":
        print("You lose your full ride scholarship.")
        print("The end.")
