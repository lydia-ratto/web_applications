# from lib.album_repository import AlbumRepository
# from lib.album import Album

# """
# When we call albumRepository#all
# We get a list of album objects reflecting the seed data.
# """
# def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
#     db_connection.seed("seeds/music_store.sql") # Seed our database with some test data
#     repository = AlbumRepository(db_connection) # Create a new albumRepository

#     albums = repository.all() # Get all albums

#     # Assert on the results
#     assert albums == [
#         Album(1, "Invisible Cities", 2001, 1),
#         Album(2, "The Man Who Was Thursday", 1999, 3),
#         Album(3, "Bluets", 1972, 1),
#         Album(4, "No Place on Earth", 1983, 2),
#         Album(5, "Nevada", 2012, 4)
#     ]

# """
# When we call albumRepository#find
# We get a single album object reflecting the seed data.
# """
# def test_get_single_record(db_connection):
#     db_connection.seed("seeds/music_store.sql")
#     repository = AlbumRepository(db_connection)

#     album = repository.find(3)
#     assert album == Album(3, "Bluets", 1972, 1)

# """
# When we call AlbumRepository#create
# We get a new record in the database.
# """
# def test_create_record(db_connection):
#     db_connection.seed("seeds/music_store.sql")
#     repository = AlbumRepository(db_connection)

#     repository.create(Album(None, "The Great Gatsby", 2010, 2))

#     result = repository.all()
#     assert result == [
#         Album(1, "Invisible Cities", 2001, 1),
#         Album(2, "The Man Who Was Thursday", 1999, 3),
#         Album(3, "Bluets", 1972, 1),
#         Album(4, "No Place on Earth", 1983, 2),
#         Album(5, "Nevada", 2012, 4),
#         Album(6, "The Great Gatsby",2010, 2),
#     ]

# """
# When we call albumRepository#delete
# We remove a record from the database.
# """
# def test_delete_record(db_connection):
#     db_connection.seed("seeds/music_store.sql")
#     repository = AlbumRepository(db_connection)
#     repository.delete(3) # Apologies to Maggie Nelson fans

#     result = repository.all()
#     assert result == [
#         Album(1, "Invisible Cities", 2001, 1),
#         Album(2, "The Man Who Was Thursday", 1999, 3),
#         Album(4, "No Place on Earth", 1983, 2),
#         Album(5, "Nevada", 2012, 4),
#     ]
