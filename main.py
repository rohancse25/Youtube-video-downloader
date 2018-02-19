import pytube
link=input()
def show_progress(stream, chunk, file_handle, bytes_remaining):
      if(bytes_remaining%100==0):
           print(int(file_handle.tell()*100/(file_handle.tell()+bytes_remaining)),' %')

yt = pytube.YouTube(link)
yt.register_on_progress_callback(show_progress)
vids= yt.streams.filter(subtype='mp4',progressive=True).all()
for i in range(len(vids)):
    print(i,'. ',vids[i])
sno = int(input())
vids[sno].download()
print('done')
