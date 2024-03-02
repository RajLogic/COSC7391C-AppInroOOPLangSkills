class CarDetail:
    @staticmethod
    def main():
        # this program prints the details of a Car
        make = input("Whats the Make of the Car? \n")
        model = input(f"Whats the Model of {make}? \n")
        colour = input(f"Whats the Colour of the {make}, {model}? \n")
        price = input(f"Whats the Price of {make}, {model}? \n")
        year = input(f"Whats the Year for {model}? \n")

        #print the details of the car
        print("\n \n \n")
        print(f"the make of the car is {make} \nThe model of the Make is {model} \nThe colour of the {model} is {colour} \nThe price is ${price} and the uear is {year}")

CarDetail.main()