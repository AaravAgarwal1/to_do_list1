#this program will check all your activities throughout the day and tell you what all you have left to do

print("This program will check all your activities throughout the day and tell you what all you have left to do")
print("Hi, today's object list is: 1. Have a Shower 2. Study 3. Eat Food 4. Sleep")
print("Enter True or False if you do/do not do your tasks!")



def to_do():
    shower=input("Have you taken a shower?")
    if shower=='True':
        print("Well done!")
    else:
        print("Complete it fast!")

    study= input("Did you study yet? ")
    if study=='True':
        print("Well done!")
    else:
        print("Complete it fast!")

    food= input("Have you eaten yet? ")

    if food=='True':
        print("Well done!")
    else:
        print("Complete it fast!")

    sleep= input("Are you going to sleep? ")
    if sleep=='True':
        print("Well done!")
    else:
        print("Please go to bed now!")


    if shower and food and study and sleep=='True':
        print("Well Done! You are done for the day!")
    else:
        print("Kindly complete the remanining tasks!")

to_do()



