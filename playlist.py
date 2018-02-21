from pytube import Playlist
n=input("ENTER PLAYLIST LINK\n")
pl=Playlist(n)
pl.download_all()
