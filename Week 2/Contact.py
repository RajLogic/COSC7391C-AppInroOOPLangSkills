class Idk:
    @staticmethod
    def Address():
        print("My Address is ")
        print("176 Furlong Rd, St Albans VIC 3021")

    @staticmethod
    def Classes():
        print("I am enroled in the following classes.")
        print("Diploma of Information Technology")
        print("at RMIT University")
boop = 0
# Call static methods in class
Idk.Address()
while boop < 2:
    print("")
    boop  += 1    
Idk.Classes()