# movie.py

from imdb import Cinemagoer

im = Cinemagoer()

class movie:
    @staticmethod
    def main():
        global search,results


        search = input("What is the movie Title? : ")
        results = im.search_movie(search)

        try:
            movie.display_movie_info()
        except IndexError:
            print("\nNo Movie Found with that title.\n")

    def display_movie_info():
        global title,movies, ID
        title = results[0]
        movies = title.getID()
        ID = im.get_movie(movies)
        cast = ID['cast']
        print('\nMovie Information:\n')
        print('Title: ',title.get('title'))
        print('Year: ',ID['year'])
        print('Rating: ',ID['rating'],'/10')
        print('Genre: ',', '.join([i for i in ID['genres']]))
        print('Country: ',', '.join([i for i in ID['countries']]))
        print('Language: ',', '.join([i for i in ID['languages']]))
        print('Director(s): ',', '.join([d['name'] for d in ID['directors']]))
        print('Top 5 Actors')
        for i in range(5): 
            print("    ", cast[i]) 
        

movie.main()