import os
from flask import Flask, request, redirect, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums/index.html', albums=albums)

# GET /albums/<id>
# Returns a single album
# Try it:
#   ; curl http://localhost:5000/albums/1
@app.route('/albums/<int:id>', methods=['GET'])
def get_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    album = repository.find(id)

    return render_template('albums/show.html', album=album)

# GET /albums/new
# Returns new album form
# Try it:
#   ; curl http://localhost:5000/albums/new
@app.route('/albums/new', methods=['GET'])
def get_new_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    return render_template('albums/new.html')

# # POST /albums
# # Creates a new album
# # Try it:
# #   ; curl -X POST -d "title=Dave&release_year=2000&artist_id=1" http://localhost:5000/albums
@app.route('/albums', methods=['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']
    if title == '' or release_year == '' or artist_id == '':
        return render_template('albums/new.html', errors="Title can't be blank, Release year can't be blank, Artist id can't be blank")

    album = Album(None, title, release_year, artist_id)
    album = repository.create(album)

    return redirect(f"albums/{album.id}")

# # DELETE /albums/<id>
# # Deletes a album
# # Try it:
# #   ; curl -X DELETE http://localhost:5000/albums/1
# @app.route('/albums/<int:id>', methods=['DELETE'])
# def delete_album(id):
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     repository.delete(id)
#     return "album deleted successfully"

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template('artists/index.html', artists=artists)

@app.route('/artists/<int:id>', methods=['GET'])
def get_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    artist = repository.find(id)

    return render_template('artists/show.html', artist=artist)

@app.route('/artists/new', methods=['GET'])
def get_new_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    return render_template('artists/new.html')

@app.route('/artists', methods=['POST'])
def create_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    name = request.form['name']
    genre = request.form['genre']
    if name == '' or genre == '':
        return render_template('artists/new.html', errors="Name can't be blank, Genre can't be blank")

    artist = Artist(None, name, genre)
    artist = repository.create(artist)

    return redirect(f"artists/{artist.id}")

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
