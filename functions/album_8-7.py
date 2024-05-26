def make_album(artist_name, album_title, tracks=None):
    """
    Builds a dictionary describing a music album.
    
    Args:
        artist_name(str): The name of the artist.
        album_title(str): The title of the album.
        tracks (int): The number of tracks on the album.

    Returns:
        A dictionary containing the artist name, album title, 
        and optionally the number of tracks
    """

    album = {
        'artist': artist_name.title(),
        'album_title': album_title.title()
    }
    if tracks:
        album['tracks'] = tracks

    return album

# make three albums
album1 = make_album('pink floyd', 'the dark side of the moon')
album2 = make_album('red hot chili peppers', 'blood sugar sex magik')
album3 = make_album('kendrick lamar', 'to pimp a butterfly', 16)

# Print the dictionaries
print("\n", album1)
print("\n", album2)
print("\n", album3)