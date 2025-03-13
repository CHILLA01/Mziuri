class Movie:
    def __init__(self, title: str, genre: str, release_year: int, rating: float):
        self.title = title
        self.genre = genre
        self.release_year = release_year
        self.rating = rating

    def get_title(self):
        return self.title

    def get_genre(self):
        return self.genre

    def get_release_year(self):
        return self.release_year

    def get_rating(self):
        return self.rating

    def __str__(self):
        return f"{self.title} ({self.release_year}) - {self.genre}, IMDB Rating: {self.rating}/10"


class MovieDatabase:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie: Movie):
        self.movies.append(movie)

    def display_all_movies(self):
        if not self.movies:
            print("No movies in the database.")
        for movie in self.movies:
            print(movie)



movie1 = Movie("Cars 1", "Animation", 2006, 7.2)
movie2 = Movie("Cars 2", "Animation", 2011, 6.2)
movie3 = Movie("Cars 3", "Animation", 2017, 6.7)


db = MovieDatabase()
db.add_movie(movie1)
db.add_movie(movie2)
db.add_movie(movie3)


db.display_all_movies()
