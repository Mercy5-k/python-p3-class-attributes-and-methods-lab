from itertools import count


class Song:
    count = 0
    genres = []
    genres_unique = []
    genre_count = {}

    artists = []
    artists_unique = []
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1
        Song.genres.append(genre)
        Song.artists.append(artist)

        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres_unique:
            cls.genres_unique.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists_unique:
            cls.artists_unique.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    pass

s1 = Song("99 Problems", "Jay-Z", "Rap")
s2 = Song("Bohemian Rhapsody", "Queen", "Rock")
s3 = Song("Empire State of Mind", "Jay-Z", "Rap")
s4 = Song("Jolene", "Dolly Parton", "Country")
s5 = Song("Halo", "Beyoncé", "Pop")
s6 = Song("Crazy in Love", "Beyoncé", "Pop")

print("Total songs:", Song.count)
print("Unique genres:", Song.genres_unique)
print("Unique artists:", Song.artists_unique)
print("Genre count:", Song.genre_count)
print("Artist count:", Song.artist_count)