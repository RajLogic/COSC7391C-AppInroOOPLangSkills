# profile.py

'''class Profile:
    def __init__(self, favourite\_music, favourite\_countries, favourite\_food, favourite\_sports, favourite\_cars, favourite\_subjects):
        self.favourite_music = favourite_music
        self.favourite_countries = favourite_countries
        self.favourite_food = favourite_food
        self.favourite_sports = favourite_sports
        self.favourite_cars = favourite_cars
        self.favourite_subjects = favourite_subjects

    def display_profile(self):
        print("Favourite music genre(s):", self.favourite_music)
        print("Favourite countries visited: ", self.favourite_countries)
        print("Favourite food: ", self.favourite_food)
        print("Favourite sport(s): ", self.favourite_sports)
        print("Favourite car(s): ", self.favourite_cars)
        print("Favourite subject(s): ", self.favourite_subjects)

# create a profile
my_profile = Profile(favourite_music=["rock", "pop"], favourite_countries=["spain", "germany"], favourite_food="pasta", favourite_sports=["soccer", "tennis"], favourite_cars=["ferrari", "lamborghini"], favourite_subjects=["math", "science"])

# display the profile
my_profile.display_profile()'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("profile.html", name="Your Name", bio="Your Bio")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)