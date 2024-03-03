import time
#Commit

#main  class for the app
#displying options
class Main:
    @staticmethod
    def starting():
        print("Starting...")
        time.sleep(2)  # Sleep for a bit to show the "starting" message
        #Goes to next def which is main script
        Main.main()
    def main():
        #input for choice
        print("1.Order A Pizza\n2.Pay for universtiy fees\n3.Borrow a book\n4.Book a movie ticket\nWhat would you like to do?\n")
        activity = input("Please Input a Number :  ")

        if activity == '1':
           Pizza.main()
        elif  activity == '2':
            Fees.main()
        elif  activity == '3':
            Book.main()
        elif activity == '4':
            Movie.main()
        else:
            print("\nInvalid Entry, Please enter again.\n \n \n")
            Main.main()


class Pizza:
    @staticmethod
    def main():
        global answer,type,crust,size,quantity,extras,date,times,location,contact,name
        print("Pizza TIME")
        type = input("What type of pizza would you like?")
        crust = input("What crust would you like?\n Thin, Regular,cheese stuffed \n")
        size = input("What size would you like\n  Small , Medium, Large \n")
        quantity = input("How many Pizzas Would you like to order? \n")
        extras = input("Any Extras to be addes?\n")
        date = input("What day is the pickup for?\n")
        times = input("What Time is the Pickup For? \n")
        location = input("What restaurant will the pickup be held? \n")
        name =input("Whats the name for the order?\n")
        contact = input("Whats the phone number for the order? \n")
        time.sleep(2)
        print("Prossessing...")
        time.sleep(2)
        print("Price of the order is $29.95")
        answer = input(f"Confirming order:\n {quantity} {type} pizza with {crust}, {size} size and {extras}. \n Pickup on the {date} at {times} at our {location}\n Under the name {name} and phone number {contact}")
        Pizza.payment()
        
    def payment():
        global credit1,card1,expiry,cvv
        if answer =="yes"or"y"or"Yes"or"Y":
            print("Next Card details")
            credit1 = input("Card Holder Name:\n")
            card1 = input("Credit Card Number:\n")
            expiry= input("Expiration Date:\n")
            cvv = input("CVV Code:\n")
            time.sleep(2)
            print("prosessing...")
            Pizza.confirmation()
        else:
            Pizza.main()

    def confirmation():
        global correct
        print(f"Confirming order:\n {quantity} {type} pizza with {crust}, {size} size and {extras}. \n Pickup on the {date} at {times} at our {location}\n Under the name {name} and phone number {contact}")
        print(f"Card Details:\nName: {credit1}\nCard Number: {card1}\nExpiry: {expiry}\nCVV: {cvv}")  
        correct = input("Is this corret? \n")  

        if correct == "yes"or 'y' or "YES":
            print("Order Confirmed")
        else:
            boop = input('Do you wish to restart the order? :')
            if boop == "yes" or"y"or "Yes":
                Pizza.main()



#Fees
'''prompt student id
        student name
        insitution name
        campus location
        program  code
        program name
        Course code
        coruse name
        class section
        ------- confirm details-----
        end
        '''
class Fees:
    @staticmethod
    def main():
        global student_id,student_name,insti_name,campus,prog_code,program_name,course_code,course_name,section
        print("Uni Fees")
        student_id = input ("Student ID:\n")
        student_name = input("Student Name:\n")
        insti_name = input("Institution Name:\n")
        campus = input("Campus Location\n")
        prog_code = input("Program Code:\n")
        program_name = input("Program name:\n")
        course_code = input("Course Code:\n")
        course_name = input("Course Name:\n")
        section = input("Class Section:\n")
        Fees.confirm()
        #prints all details


    def confirm():
        print("---------------CONFIRM----------------")
        print(f"Student Name: {student_id}\nStudent Name: {student_name}\nInstitution Name: {insti_name}\nCampus Location: {campus}\nProgram Code: {prog_code}\nCourse Code: {course_code}\nCourse Name: {course_name}\nClass Section: {section}")
        confirm = input("Is this correct? (yes/no): \n")
        time.sleep(3)
        print("------Prossesing-------")

        if confirm == "yes"or"y"or"Yes":
            print("\nDetails Confirmed!\n")
            time.sleep(5)
        else:
            ask = input("Do you wish to try again? (yes/no): ")
            if ask=="yes" or ask=='y':
                Fees.main()
            elif ask=="no" or ask=='n':
                quit()
            else:
                print('Please enter a valid option')
                Fees.confirm()



'''Borrower ID
Borrower Name
Book title
borrow date
libary loaction
'''
class Book:
        @staticmethod
        def main():
            global bookid,borrowId,borrowName,date,location,bookName
            borrowId = input("Enter your ID Number: ")
            borrowName = input("Enter your Name: ")
            bookid = input("Enter the Book ID: ")
            bookName = input("What is the Title of the Book?: ")
            date = input('"Date of Borrow: ')
            location = input("Libary Location: ")
            Book.confirm()

        def confirm():
            print("---------------CONFIRM----------------")
            print(f"Borrower ID: {borrowId}\nBorrower Name: {borrowName}\nBook ID: {bookid}\nBook Name: {bookName}\nDate of Borrow: {date}\nLocation of Borrow: {location}")
            confirm2 = input("Is this correct? (yes/no): \n")
            time.sleep(3)
            print("------Prossesing-------")

            if confirm2 == "yes"or"y"or"Yes":
                print("\nDetails Confirmed!\n")
                time.sleep(5)
            else:
                ask2 = input("Do you wish to try again? (yes/no): ")
                if ask2=="yes" or ask2=='y':
                    Book.main()
                elif ask2=="no" or ask2=='n':
                    quit()
                else:
                    print('Please enter a valid option')
                    Book.confirm()

            

class Movie:
    def main():
        global movieTitle,sessiondate,showtime,cinema,seats,cost
        print("Movie TIME")
        movieTitle=input("Enter the Movie Title: ")
        sessiondate = input("Whats the date: ")
        showtime = input("What Time does it start: ")
        cinema = input("What is the Cinema location: ")
        tickets = int(input("How many tickets? :"))
        seats = input("Where would you like the seats?\nFront, Middle, Back: ")
        print("----------Prosessing--------")
        cost = tickets * 5 #asuming tickets cost $5
        Movie.confirm()


    def confirm():
            global confirm3,ask3
            print("---------------CONFIRM----------------")
            print(f"The price of the Tickets  will be ${cost}")
            confirm3 = input("Confirm? (yes/no): \n")
            time.sleep(3)
            print("------Prossesing-------")

            if confirm3 == "yes"or"y"or"Yes":
                print("\nPrice and tickets confirmed\nMoving onto details\n")
                time.sleep(2)
                Movie.payment()
            else:
                ask3 = input("Do you wish to try again? (yes/no): ")
                if ask3=="yes" or ask3=='y':
                    Movie.main()
                elif ask3=="no" or ask3=='n':
                    quit()
                else:
                    print('Please enter a valid option')
                    Movie.confirm()

    def payment():
        global card2,cvv2,email
        card2 = input(f"\nCard Number:\n")
        cvv2 = input(f"CVV Code:\n")
        email = input("Email adress: \n")
        print('\nProcessing Payment...\n')
        Movie.confirm2()

    def confirm2():
        global confirm4,ask4
        print("---------------CONFIRM----------------")
        print(f"The card Number is: {card2}\nCVV is: {cvv2}\nEmail is: {email}\nTotal cost of  movie ticket is: ${cost}")
        confirm4 = input("Confirm? (yes/no): \n")
        time.sleep(3)
        print("------Prossesing-------")

        if confirm4 == "yes"or"y"or"Yes":
            print("\nPrice and tickets confirmed\nMoving onto details\n")
            time.sleep(2)
            Movie.end()
        else:
            ask4 = input("Do you wish to try again? (yes/no): ")
            if ask4=="yes" or ask4=='y':
                Movie.main()
            elif ask4=="no" or ask4=='n':
                quit()
            else:
                print('Please enter a valid option')
                Movie.confirm2()

    def end():
        print(f"Movie tickets for {movieTitle}, on {sessiondate} at {showtime} at the {cinema} location with {seats} seat.\n Have been Booked ")
        print("\nYour transaction has been successful!\n")
        time.sleep(5)
        quit()
        


Main.starting()