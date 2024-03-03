# movie.py

'''def display_movie_info():
    title = "Inception"
    director = "Christopher Nolan"
    cast = ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page", "Tom Hardy", "Ken Watanabe", "Cillian Murphy", "Marion Cotillard", "Michael Caine"]
    genre = "Science Fiction, Action"
    year = 2010

    print("Title:", title)
    print("Director:", director)
    print("Cast:", ', '.join(cast))
    print("Genre:", genre)
    print("Year Released:", year)

if __name__ == "__main__":
    display_movie_info()'''

from imdb import IMDb

im = IMDb()

search = input("What is the movie Title? : ")
results = im.search_movie(search)
    
    
try:
    movie = results[0]
    print("\nMovie found!\n")
    print("Title: ", movie['title'])
    print("Year: ", movie['year'])
    print("Rating: ", movie['rating'])
    print("Votes: ", movie['votes'])
    print("Plot:\n", movie['plot'])
        
    directors = movie[0]
    for d in movie["director"]:
        id = d["id"]
        director = im.get_person(id)
        directors.append(f'{director["name"]}')
        
    print('\nDirectors: ')
    print(', '.join(directors))
    
    actors = movie[0]
    for a in movie['actors'][:5]: # get first five actors
        actor = im.get_person(a['id'])
        actors.append((actor['name'], actor['birth date']))
        
    print('\nTop 5 Actors and their Birthdates:\n')
    for a in actors:
        print(f"{a[0]} ({a[1][:4]})")
        
except Exception:
    print("\nNo Movie Found with that title.\n")