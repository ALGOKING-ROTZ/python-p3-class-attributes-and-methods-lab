from song import Song

# Reset class attributes before testing
Song.count = 0
Song.genres = []
Song.artists = []
Song.genre_count = {}
Song.artist_count = {}

# Create some songs
s1 = Song("99 Problems", "Jay-Z", "Rap")
s2 = Song("Halo", "Beyonce", "Pop")
s3 = Song("God's Plan", "Drake", "Rap")
s4 = Song("Formation", "Beyonce", "Pop")
s5 = Song("Empire State of Mind", "Jay-Z", "Rap")

# Check song count
print("Song count:", Song.count)  # Should be 5

# Check unique genres
print("Genres:", Song.genres)  # Should be ["Rap", "Pop"]

# Check unique artists
print("Artists:", Song.artists)  # Should be ["Jay-Z", "Beyonce", "Drake"]

# Check genre counts
print("Genre count:", Song.genre_count)  # {"Rap": 3, "Pop": 2}

# Check artist counts
print("Artist count:", Song.artist_count)  # {"Jay-Z": 2, "Beyonce": 2, "Drake": 1}
