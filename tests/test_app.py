from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""


def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_store.sql")
    page.goto(f"http://{test_web_address}/albums")

    a_tags = page.locator("a")

    expect(a_tags).to_have_text([
        'Doolittle',
        'Surfer Rosa',
        'Add new album'
    ])

def test_get_album(page, db_connection, test_web_address):
    db_connection.seed("seeds/music_store.sql")
    page.goto(f"http://{test_web_address}/albums/1")          

    h1_tags = page.locator("h1")
    p_tags = page.locator("p")

    expect(h1_tags).to_have_text([
        'Doolittle',
    ])
    
    expect(p_tags).to_have_text([
        'Released: 1989', 'Artist: Pixies'
    ])

def test_new_album(page, db_connection, test_web_address):
    db_connection.seed("seeds/music_store.sql")
    page.goto(f"http://{test_web_address}/albums/new")          

    h1_tags = page.locator("h1")
    title_element = page.get_by_title("title")
    release_year_element = page.get_by_title("release_year")
    artist_id_element = page.get_by_title("artist_id")

    expect(h1_tags).to_have_text([
        'Add an album',
    ])
    
    expect(title_element).to_have_text([
        'Title'
    ])
    expect(release_year_element).to_have_text([
        'Release year'
    ])
    expect(artist_id_element).to_have_text([
        'Artist'
    ])

def test_create_album(page, db_connection, test_web_address):
    db_connection.seed("seeds/music_store.sql")
    page.goto(f"http://{test_web_address}/albums")

    page.click("text=Add new album")
    
    page.fill("input[name=title]", 'Test album')
    page.fill("input[name=release_year]", '2000')
    page.fill("input[name=artist_id]", '1')

    page.click("text=Add album")


def test_attempt_create_album_with_errors(page, db_connection, test_web_address):
    db_connection.seed("seeds/music_store.sql")
    page.goto(f"http://{test_web_address}/albums")

    page.click("text=Add new album")
    page.click("text=Add album")

    errors_tag = page.locator('.t-errors')
    expect(errors_tag).to_have_text("There were errors with your submission: Title can't be blank, Release year can't be blank, Artist id can't be blank")


# def test_delete_album(db_connection, web_client):
#     db_connection.seed("seeds/music_store.sql")
#     response = web_client.delete("/albums/1")

#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == "album deleted successfully"

#     response = web_client.get("/albums")

#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == "\n".join([
#         'Album(2, The Man Who Was Thursday, 1999, 3)',
#         'Album(3, Bluets, 1972, 1)',
#         'Album(4, No Place on Earth, 1983, 2)',
#         'Album(5, Nevada, 2012, 4)'
#     ])


def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_store.sql")
    page.goto(f"http://{test_web_address}/artists")

    a_tags = page.locator("a")

    expect(a_tags).to_have_text([
        'Pixies',
        'ABBA',
        'Taylor Swift',
        'Nina Simone',
        'Add new artist'
    ])

def test_get_artist(page, db_connection, test_web_address):
    db_connection.seed("seeds/music_store.sql")
    page.goto(f"http://{test_web_address}/artists/1")          

    h1_tags = page.locator("h1")
    p_tags = page.locator("p")

    expect(h1_tags).to_have_text([
        'Pixies',
    ])
    
    expect(p_tags).to_have_text([
        'Genre: rock'
    ])

def test_create_artist(page, db_connection, test_web_address):
    db_connection.seed("seeds/music_store.sql")
    page.goto(f"http://{test_web_address}/artists")

    page.click('text=Add new artist')

    name_element = page.get_by_title('name')
    genre_element = page.get_by_title('genre')

    expect(name_element).to_have_text('Name')
    expect(genre_element).to_have_text('Genre')

    page.fill("input[name=name]", 'Test name')
    page.fill("input[name=genre]", 'Test genre')

    page.click('text=Add artist')



# === End Example Code ===
