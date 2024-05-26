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

while True:
    print("\nEnter information about an album (or 'q' to quit):")
    artist_name = input("Artist name: ")
    if artist_name == 'q':
        break

    album_title = input("Album title: ")
    if album_title == 'q':
        break

    tracks = input("Tracks: ")
    if tracks.isdigit():
        tracks =int(tracks)
    else:
        tracks = None

    album = make_album(artist_name, album_title, tracks)
    print(f"\nAlbum information:\n{album}")

print("Thanks for using the Album Creator!")
    
