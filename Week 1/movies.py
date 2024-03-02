# movie.py

def display_movie_info():
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
    display_movie_info()
