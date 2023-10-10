# from lib.artist_repository import ArtistRepository
# from lib.artist import Artist

# """
# When we call artistRepository#all
# We get a list of artist objects reflecting the seed data.
# """
# def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
#     db_connection.seed("seeds/music_store.sql") # Seed our database with some test data
#     repository = ArtistRepository(db_connection) # Create a new artistRepository

#     artists = repository.all() # Get all artists

#     # Assert on the results
#     assert artists == "Pixies, ABBA, Taylor Swift, Nina Simone"

# def test_artist_created(db_connection):
#     db_connection.seed("seeds/music_store.sql") # Seed our database with some test data
#     repository = ArtistRepository(db_connection) # Create a new artistRepository

#     repository.create(Artist(None, 'Wild nothing', 'indie'))

#     artists = repository.all() # Get all artists

#     assert artists == "Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"

