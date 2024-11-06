def make_album(artist_name,album_title,number_of_tracks_on_an_album=''):
    dict_album = {'Artist_Name': artist_name.title() , 'Album_Title':album_title.title()}
    if number_of_tracks_on_an_album:
        dict_album['Number_Of_Tracks_On_An_Album']=  number_of_tracks_on_an_album
        
    return dict_album



while True:
    quit = input("To store information in the dictionary Enter 'Yes'\nOthetwise Enter 'quit' to Exit from the program: ")
    if quit.lower()=='quit':
        print("Exiting from the program......")
        break
    
    elif quit.lower()=='yes':
        artist_name = input("Enter Artist Name: ")
        album_title = input("Enter Album Title: ")
        number_of_tracks_on_an_album = input("If necessary enter Album Title or press Enter only: ")
        print(make_album(artist_name,album_title,number_of_tracks_on_an_album))

    else:
        print("\nInvlid Option \nYou can only Enter 'Yes' or 'Quit' ")
    

