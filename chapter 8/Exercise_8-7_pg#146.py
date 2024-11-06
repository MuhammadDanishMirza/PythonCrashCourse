def make_album(artist_name,album_title,number_of_tracks_on_an_album=''):
    dict_album = {'Artist_Name': artist_name , 'Album_Title':album_title}
    if number_of_tracks_on_an_album:
        dict_album['Number_Of_Tracks_On_An_Album']=  number_of_tracks_on_an_album
        
    return dict_album
        
print(make_album("Artist1", "Album1"))
print(make_album("Artist2", "Album2"))
print(make_album("Artist3", "Album3"))


print(make_album("Artist4", "Album4", 12))


