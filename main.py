from tkinter import *
import pytube
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="WELCOME TO YOUTUBE DOWNLOADER")
        self.label.pack()

        self.l2 = Label(master, text="ENTER URL")
        self.l2.pack()
        self.tx1=Entry()
        self.tx1.pack()
        self.close_button = Button(master, text="DOWNLOAD", command=self.download)
        self.close_button.pack()
        self.close_button = Button(master, text="CLOSE", command=master.quit)
        self.close_button.pack()

    def download(self):
        n = self.tx1.get()
        yt = pytube.YouTube(n)
        vids = yt.streams.filter(subtype='mp4', progressive=True).all()
            
        for i in range(len(vids)):
            print(i, '. ', vids[i])
        sno = int(input())
        vids[sno].download()
        print('done')
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
