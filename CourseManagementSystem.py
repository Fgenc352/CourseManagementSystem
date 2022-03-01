dictOfCourse = {"physics": "4", "mathematics": "3", "programming": "3"}  # key: course name, value: credits.
dictOfUsers = {"admin": ["sehir123", 0, {}], "Ahmet": ["123", 0, {"mathematics":"3", "physics":"4"}], "Ayse": ["456", 0, {"programming":"3", "mathematics":"3"}]}  # key: user name, value: [password, budget, {}]
student_name = []
def login():
    print("****Welcome to Course Management System****\nPlease provide login information")
    while True:
        user_id = input("Id: ")
        user_password = input("Password: ")
        if user_id in dictOfUsers:
            if dictOfUsers[user_id][0] != user_password:
                print("Invalid id or password please try again.")
                continue
            else:
                print("Successfully logged in!")
                if user_id == "admin":
                    # call admin page function
                    return "admin"
                else:
                    # call student page function
                    student_name.append(user_id)
                    return "student"
        print("Invalid id or password please try again.")

def admin_menu():
    print("""Welcome Admin! What do you want to do?\n
1-List courses
2-Create a course
3-Delete a course
4-Show students registered to a course
5-Users Budget Menu
6-List Users
7-Create User
8-Delete User
9-Exit
    """)
    while True:
        admin_choice = input("Your Choice:")
        if 1 <= int(admin_choice) <= 9:
            return admin_choice


def admin_islemleri(choice):
    if choice == "1":
        print("*** Offered Courses ***\nCourse name" + " " * 10 + "Credit")
        count = 1
        for course in dictOfCourse:
            print("%d-%s" % (count, course) + " " * (23 - (len(course) + 2)) + dictOfCourse[course])
            count += 1

    elif choice == "2":
        add_course_name = input("What is the name of the course that you want to add?")
        add_course_credits = input("How many credits this course has?")
        yes_or_no = input("%s will be added with %s credits.\nAre you sure?[Y/N]" % (add_course_name, add_course_credits))
        if yes_or_no == "Y":
            print("%s has been added to courses with %s credits" % (add_course_name, add_course_credits))
            dictOfCourse[add_course_name] = add_course_credits
        else:
            print("Adding operation has been cancelled out.")

    elif choice == "3":
        print("Course name" + " " * 10 + "Credit")
        count = 1
        for course in dictOfCourse:
            print("%d-%s" % (count, course) + " " * (23 - (len(course) + 2)) + dictOfCourse[course])
            count += 1
        while True:
            delete_course_index = input("Which course do you want to delete?")
            if int(delete_course_index) <= len(dictOfCourse):
                break
        delete_index = 1
        for delete_course in dictOfCourse:
            if delete_index == int(delete_course_index):
                print("%s has been deleted and money has been transferred back to student accounts" % (delete_course))
                for user in dictOfUsers:
                    if delete_course in dictOfUsers[user][2]:
                        del dictOfUsers[user][2][delete_course]
                        dictOfUsers[user][1] += int(dictOfCourse[delete_course]) * 100
                del dictOfCourse[delete_course]
                break
            delete_index += 1

    elif choice == "4":
        while True:
            show_course = input("Which course do you want to show?")
            if show_course not in dictOfCourse:
                print("This course doesn't exist, please provide a valid input")
            else:
                count = 1
                print("Course Name: %s\nStudent taking %s:" % (show_course, show_course))
                for student in dictOfUsers:
                    if show_course in dictOfUsers[student][2]:
                        print("%d-%s" % (count, student))
                        count += 1
                break

    elif choice == "5":
        print("  User" + " "*10 + "Money")
        count = 1
        for user in dictOfUsers:
            print("%d-%s" % (count, user) + " "*(19-(len(user) + len(str(dictOfUsers[user][1])))) + str(dictOfUsers[user][1]))
            count += 1
        print("""What do you want to do?

1-Add money to user
2-Subtract money from user
3-Back to admin menu
""")
        while True:
            choice_user = input("Your Choice:")
            if choice_user == "":
                print("Please provide a valid menu.")
                continue
            elif int(choice_user) < 1 or int(choice_user) > 3:
                print("Please provide a valid menu.")
                continue
            elif 1 <= int(choice_user) <= 3:
                break
        if choice_user == "1":
            print("Which user do you want add money to their account?")
            count2 = 1
            for user in dictOfUsers:
                print ("%d-%s" % (count2, user))
                count2 += 1
            while True:
                choice_user2 = input("Your Choice:")
                if int(choice_user2) <= len(dictOfUsers):
                    break
            count_add_money = 1
            for user in dictOfUsers:
                if count_add_money == int(choice_user2):
                    add_money = input("How much money do you want to add?")
                    yes_or_no = input("%s$ will be added to %s" % (add_money, user) + "\nAre you sure?[Y/N]:")
                    if yes_or_no == "Y":
                        dictOfUsers[user][1] += int(add_money)
                        print("Adding money operations has been finished.")
                    else:
                        print("Adding money operations has been cancelled out.")
                    break
                count_add_money += 1
        elif choice_user == "2":
            print("Which user do you want subtract money to their account?")
            count3 = 1
            for user in dictOfUsers:
                print ("%d-%s" % (count3, user))
                count3 += 1
            while True:
                choice_user3 = input("Your Choice:")
                if choice_user == "":
                    print("Please provide a valid input.")
                    continue
                elif int(choice_user3) <= len(dictOfUsers):
                    break
            count_subtract_money = 1
            for user in dictOfUsers:
                if count_subtract_money == int(choice_user3):
                    subtract_money = input("How much money do you want to subtract?")
                    yes_or_no = input("%s$ will be subtracted to %s" % (subtract_money, user) + "\nAre you sure?[Y/N]:")
                    if yes_or_no == "Y":
                        dictOfUsers[user][1] -= int(subtract_money)
                        print("Subtracting money operations has been finished.")
                    else:
                        print("Subtracting money operations has been cancelled out.")
                    break
                count_subtract_money += 1

    elif choice == "6":
        print("Current Users:")
        count = 1
        for user in dictOfUsers:
            print("%d-%s" % (count, user))
            count += 1

    elif choice == "7":
        new_user_name = input("What is the name of user that you want to create?")
        new_user_password = input("What is the password for account?")
        new_user_budget = input("How much money do you want user to have?")
        dictOfUsers[new_user_name] = [new_user_password, new_user_budget, {}]
        print("The new user has been added successfully!")

    elif choice == "8":
        print("Current Users:")
        count = 1
        for user in dictOfUsers:
            print("%d-%s" % (count, user))
            count += 1
        while True:
            delete_user = input("What is the name of user that you want to delete?")
            if delete_user in dictOfUsers:
                print("%s is deleted!" % (delete_user))
                del dictOfUsers[delete_user]
                break

    elif choice == "9":
        start()
        return

    admin_islemleri(admin_menu())

def student_menu(name):
    print("""Welcome %s! What do you want to do?

1-Add courses to my courses
2-Delete a course from my courses
3-Show my courses
4-Budget Menu
5-Exit
""" % name)
    while True:
        student_choice = input("Your choice:")
        if student_choice in ["1", "2", "3", "4", "5"]:
            return student_choice

def student_islemler(choice):
    if choice == "1":
        listCourseNumber = []  # this will check add_course_choice is valid or not.
        print("Course name" + " " * 10 + "Credit")
        count = 1
        for course in dictOfCourse:
            listCourseNumber.append(str(count))
            print("%d-%s" % (count, course) + " " * (23 - (len(course) + 2)) + dictOfCourse[course])
            count += 1
        while True:
            add_course_choice = input("Which course do you want to take (Enter 0 to go to main menu)? ")
            if add_course_choice in listCourseNumber:
                add_index = 1
                for add_course in dictOfCourse:
                    if add_index == int(add_course_choice):
                        if add_course in dictOfUsers[student_name[-1]][2]:
                            print("This course is already in your profile, please choose another course")
                        else:
                            if dictOfUsers[student_name[-1]][1] < int(dictOfCourse[add_course])*100:
                                print("You don't have enough money in your account. Please deposit money, or choose a course with lesser credit.")
                            else:
                                print("%s has been successfully added to your courses." % add_course)
                                dictOfUsers[student_name[-1]][2][add_course] = dictOfCourse[add_course]
                                dictOfUsers[student_name[-1]][1] -= 100 * int(dictOfCourse[add_course])
                                student_islemler(student_menu(student_name[-1]))

                    add_index += 1
            elif add_course_choice == "0":
                break


    elif choice == "2":
        listCourseNumber = []  # this will check add_course_choice is valid or not.
        print("Course name" + " " * 10 + "Credit")
        count = 1
        for course in dictOfUsers[student_name[-1]][2]:
            listCourseNumber.append(str(count))
            print("%d-%s" % (count, course) + " " * (23 - (len(course) + 2)) + dictOfUsers[student_name[-1]][2][course])
            count += 1
        while True:
            delete_course_choice = input("Which course do you want to remove?")
            if delete_course_choice in listCourseNumber:
                delete_index = 1
                for delete_course in dictOfUsers[student_name[-1]][2]:
                    if delete_index == int(delete_course_choice):
                        print("""You have chosen: %s
%d$ will be returned to your account""" % (delete_course, 100 * int(dictOfUsers[student_name[-1]][2][delete_course])))
                        while True:
                            yes_or_no = input("Are you sure that you want to remove this course? [Y/N]")
                            if yes_or_no == "Y" or yes_or_no == "N":
                                break
                        if yes_or_no == "Y":
                            dictOfUsers[student_name[-1]][1] += 100 * int(dictOfUsers[student_name[-1]][2][delete_course])
                            del dictOfUsers[student_name[-1]][2][delete_course]
                            print("Course has been deleted from your profile")
                            print(dictOfUsers[student_name[-1]][1])
                            break
                        else:
                            print("Deleting course operation has been cancelled out.")
                            break
                    delete_index += 1
                break

    elif choice == "3":
        print("Your Courses:\nCourse Name" + " " * 10 + "Credit")
        count = 1
        for course in dictOfUsers[student_name[-1]][2]:
            print("%d-%s" % (count, course) + " " * (23 - (len(course) + 2)) + dictOfUsers[student_name[-1]][2][course])
            count += 1

    elif choice == "4":
        print("""#### BUDGET MENU #####
Your budget is: %d$

What do you want to do?
1-Add Money 
2-Go to main menu
""" % dictOfUsers[student_name[-1]][1])
        while True:
            user_choice = input("Your choice:")
            if user_choice == "1" or user_choice == "2":
                break
        if user_choice == "1":
            amount_money = input("Amount of money:")
            dictOfUsers[student_name[-1]][1] += int(amount_money)
            print("Your budget has been updated.")

    elif choice == "5":
        start()
        return



    student_islemler(student_menu(student_name[-1]))



def start():
    if login() == "admin":
        admin_islemleri(admin_menu())

    else:
        student_islemler(student_menu(student_name[-1]))

start()





