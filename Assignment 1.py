# Name: Reshad Mohsin
# Due Date: October 10 2024
# Title: Who Am I?

print("Welcome to 'Who am I?' by Reshad Mohsin.") # Welcome message to start the game
play = input("Would you like to play? (yes/no): ").lower()  # This is an optional question, but it makes the game more formal by asking if the user wants to play compared to if the game started immediately

if play == "yes": # Simple if statement to check the string to say yes in response to the inital question above
    print("It’s your first day at a brand-new high school, Bill Hogarth Secondary School. You’re feeling nervous but excited, ready to make an impression. Every choice you make will shape your reputation, relationships, and overall high school experience. Will you become the star student, a social butterfly, or something entirely unexpected? Your choices determine your destiny and who you are.")
    # Giving the story overview or scenario to allow the player to understand the context before he begins the game
    print("You take your first steps into the school, What would you like to do first?") # First question the user needs to answer. 
    # The first set of choices to pick from are presented below:
    print("1. Go straight to your first class")
    print("2. Explore the school hallways")
    print("3. Head to the gym to check out sports teams")
    choice1 = input("Enter 1, 2, or 3: ") # Asking the user to tell the game which choice it would like to go with either 1, 2, or 3

    # Branch 1 - If there initial choice was to go to class (choice1)
    if choice1 == "1": # Same process as before: using a simple if statement to check the string, asking the user a new question, then giving the choices to pick from.
        print("You don’t want to be late for your first class, so you rush in and take a seat. Mr. Nagra gives out a pop quiz.")
        print("What do you do?")
        print("1. Take the quiz seriously and try your best")
        print("2. Try to cheat off the person next to you")
        choice1A = input("Enter 1 or 2: ") # Once again asks for the users choice

        if choice1A == "1": # Based on the users choice, it presents even more choices through nested if statements
            print("You put effort into the quiz and score amazingly! Mr. Nagra asks you if your willing to offer tutoring services to the other students.")
            print("1. Accept and help your classmates study")
            print("2. Decline and focus on your own academics")
            choice1A1 = input("Enter 1 or 2: ")

            if choice1A1 == "1": # Uses a nested if statement for if the user picks choice1 then choice 1A then choice 1A1
                print("ENDING: Class Genius – Your dedication to helping others earns you a reputation for being brilliant.") # This is the first of twelve possible endings you can reach
            elif choice1A1 == "2": 
                print("ENDING: Star Student – You excel in your studies and stand out academically.") # Same idea as above just a different ending 

        elif choice1A == "2": # Repeats the same process as above using nested if statements (this will occur in each pathway)
            print("You try to cheat on the quiz, but Mr. Nagra catches you and you get sent to detention in Mr. Cotey’s office.")
            print("1. Serve your detention quietly")
            print("2. Skip detention and leave school")
            choice1B = input("Enter 1 or 2: ")

            if choice1B == "1":
                print("ENDING: Reformed Cheater – You decide to turn things around after detention and focus on school.")
            elif choice1B == "2":
                print("ENDING: The Troublemaker – Instead of going to detention you simply leave and fall into a frequent pattern of avoiding classes altogether.")

    # Branch 2 - If there initial choice was to explore the hallways (choice 2). Process is the exact same throughout the rest of the code.
    elif choice1 == "2":
        print("You wander the hallways, curious about your new school. Suddenly, you stumble upon a fight between Vihan and Jamyl.")
        print("What do you do?")
        print("1. Let a teacher know about the fight")
        print("2. Stay back and watch")
        choice2 = input("Enter 1 or 2: ")

        if choice2 == "1":
            print("You quickly inform a nearby staff member, Ms Simmons, about the fight. They rush to intervene and thank you for your quick action.")
            print("1. Feel proud of your decision")
            print("2. Worry about being labeled a snitch")
            choice2A = input("Enter 1 or 2: ")

            if choice2A == "1":
                print("ENDING: The Hero – You gain a reputation as someone who stands up for others and is respected by your peers.")
            elif choice2A == "2":
                print("ENDING: Careful Bystander – You did the right thing, but you choose to stay low-key to avoid attention.")

        elif choice2 == "2":
            print("You decide to stay back and observe. Eventually, the fight stops, and the students are pulled apart by the vice-principal, Ms Simmons.")
            print("1. Join the crowd and gossip about it")
            print("2. Walk away and find your class")
            choice2B = input("Enter 1 or 2: ")

            if choice2B == "1":
                print("ENDING: Rumor Spreader – You become known for gossiping, which shapes your social circle.")
            elif choice2B == "2":
                print("ENDING: Quiet Thinker – You reflect on the situation and decide to focus on your studies instead of drama.")

    # Branch 3 - If there initial choice was to check out clubs and sports teams (choice 3). 
    elif choice1 == "3":
        print("You head to the gym, where sign-up sheets for various clubs and teams are posted. You spot a few different options.")
        print("What do you do?")
        print("1. Sign up for the basketball team")
        print("2. Decide to stay out of extracurricular activities")
        choice3 = input("Enter 1 or 2: ")

        if choice3 == "1":
            print("You decide to try out for the basketball team, but unfortunately, you don’t make the cut.")
            print("1. Take it as a sign to focus on your studies")
            print("2. Tryout for the soccer team instead")
            choice3A = input("Enter 1 or 2: ")

            if choice3A == "1":
                print("ENDING: Focused Student – You dedicate more time to your studies and excel academically.")
            elif choice3A == "2":
                print("ENDING: Rising Athlete – You impress the coach with your soccer skills and secure a spot on the team, becoming a key player.")

        elif choice3 == "2":
            print("You decide to keep a low profile and focus on getting through the day.")
            print("1. Sit quietly at lunch")
            print("2. Chat with some new classmates at lunch")
            choice3B = input("Enter 1 or 2: ")

            if choice3B == "1":
                print("ENDING: The Lone Wolf – You keep to yourself and avoid most social interactions.")
                
            elif choice3B == "2":
                print("ENDING: Social Butterfly – You strike up conversations and quickly make new friends.")  

    print("Thank you for playing!") # End message after any ending
else:
    print("Maybe you can play again later! Have a good day.") # Message in case they do not reply "yes" to if they want to play