
student = {}

active = True

while active:
    userinput = input("What is the student's name: ")
    course = input("What course is the student assigned: ")
    student[userinput] = course

    exit_continue = input("Please press Y to continue")
    if str(exit_continue) != "Y":
        active = False
print("\n{}\t \t \t\t \t{:<20}".format("Student", "Course"))
for sname, scourse in student.items():
    print(str(sname + " \t\t\t\t" + str(scourse)))
    
    
    while True:
    user_input = input("Please guess a number between 1 and 20 (Press Y to exit): ")

    the_number = 7
    if user_input == "Y":
        break

    if int(user_input) == 7:
        print("Wow, you’re good!!!!")

    elif the_number-5 <= int(user_input) <= the_number+5:
        print("You’re getting warm")

    elif (the_number + 5 < int(user_input) <= 20) or (the_number -5 > int(user_input) > 0):
        print("You’re not even close")

    else:
        print("Your number is outside of the range")
