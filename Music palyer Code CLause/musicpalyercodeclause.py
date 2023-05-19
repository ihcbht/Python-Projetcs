import os
import pickle
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from pygame import mixer

class Musicplayer(tk.Frame):
    def __init__(myobj, master):
        super().__init__(master)
        myobj.master=master
        myobj.pack()

        mixer.init()

        if os.path.exists('songs.pickle'):
            with open('songs.pickle','rb')as f:
                myobj.playlist=pickle.load(f)
        else:
            myobj.playlist=[]

        myobj.current=0
        myobj.paused=True
        myobj.played=False

        myobj.create_frames()
        myobj.track_widgets()
        myobj.control_widgets()
        myobj.tracklist_widgets()
    
    def create_frames(myobj):
        myobj.musicwindow=tk.LabelFrame(myobj, text='Song Track',font=("times new roman",20,"bold"),
                    bg="lime green",fg="black",bd=8,relief=tk.GROOVE)
        myobj.musicwindow.configure(width=750, height=600)
        myobj.musicwindow.grid(row=0,column=0,padx=12)


        myobj.musicplaylist=tk.LabelFrame(myobj, text=f'Playlist-{len(myobj.playlist)}',font=("times new roman",20,"bold"),
                    bg="lime green",fg="black",bd=8,relief=tk.GROOVE)
        myobj.musicplaylist.configure(width=250, height=800)
        myobj.musicplaylist.grid(row=0,column=1,rowspan=3,pady=7)


        myobj.controlwindow=tk.LabelFrame(myobj, text='Controls',font=("times new roman",20,"bold"),
                    bg="lime green",fg="black",bd=8,relief=tk.GROOVE)
        myobj.controlwindow.configure(width=650, height=200)
        myobj.controlwindow.grid(row=2,column=0,pady=7,padx=12)
    

    def track_widgets(myobj):
        myobj.canvas=tk.Label(myobj.musicwindow,image=img)
        myobj.canvas.configure(width=630,height=450)
        myobj.canvas.grid(row=0,column=0)

        myobj.songtrack=tk.Label(myobj.musicwindow,font=("times new roman",20,"bold"),bg="light blue",fg="black")
        myobj.songtrack['text']="Code Clause Music Player"
        myobj.songtrack.configure(width=30,height=1)
        myobj.songtrack.grid(row=1,column=0)

    def control_widgets(myobj):
        myobj.Openqueue=tk.Button(myobj.controlwindow,bg='black',fg='lime green',font=10)
        myobj.Openqueue['text']= 'Open Queue'
        myobj.Openqueue['command']=myobj.retrievesongs
        myobj.Openqueue.grid(row=0,column=0,padx=10)

        myobj.previous=tk.Button(myobj.controlwindow,image=prev)
        myobj.previous['command']=myobj.prevsong
        myobj.previous.grid(row=0,column=1)

        myobj.pause=tk.Button(myobj.controlwindow,image=pause)
        myobj.pause['command']=myobj.pausesong
        myobj.pause.grid(row=0,column=2)

        myobj.next=tk.Button(myobj.controlwindow,image=nextt)
        myobj.next['command']=myobj.nextsong
        myobj.next.grid(row=0,column=3)

        myobj.volume=tk.DoubleVar()
        myobj.slider=tk.Scale(myobj.controlwindow,from_=0, to=10,orient=tk.HORIZONTAL)
        myobj.slider['variable']=myobj.volume
        myobj.slider.set(6)
        mixer.music.set_volume(0.6)
        myobj.slider['command']=myobj.changevolume
        myobj.slider.grid(row=0,column=4,padx=7)

    def tracklist_widgets(myobj):
        myobj.scrollbar=tk.Scrollbar(myobj.musicplaylist,orient=tk.VERTICAL)
        myobj.scrollbar.grid(row=0,column=1,rowspan=7,sticky='ns')

        myobj.list=tk.Listbox(myobj.musicplaylist,selectmode=tk.SINGLE,yscrollcommand=myobj.scrollbar.set,selectbackground='orange')
        myobj.namesongs()
        myobj.list.config(height=25)
        myobj.list.bind('<Double-1>',myobj.playsong)
        myobj.scrollbar.config(command=myobj.list.yview)
        myobj.list.grid(row=0,column=0,rowspan=7)

    def namesongs(myobj):
        for index,song in enumerate(myobj.playlist):
            myobj.list.insert(index,os.path.basename(song))

    def retrievesongs(myobj):
        myobj.songlist=[]
        directory=filedialog.askdirectory()
        for roott,dirs,files in os.walk(directory):
            for file in files:
                if os.path.splitext(file)[1]=='.mp3':
                    path=(roott+'/'+file).replace('\\','/')
                    myobj.songlist.append(path)
        
        with open('songs.pickle', 'wb')as f:
            pickle.dump(myobj.songlist,f)
        myobj.playlist=myobj.songlist
        myobj.musicplaylist['text']=f'Playlist - {str(len(myobj.playlist))}'
        myobj.list.delete(0,tk.END)
        myobj.namesongs()

    def playsong(myobj,event=None):
        if event is not None:
            myobj.current=myobj.list.curselection()[0]
            for i in range(len(myobj.playlist)):
                myobj.list.itemconfigure(i,bg='white')
        mixer.music.load(myobj.playlist[myobj.current])

        myobj.pause['image']=play
        myobj.paused=False
        myobj.played=True
        myobj.songtrack['anchor']='w'
        myobj.songtrack['text']=os.path.basename(myobj.playlist[myobj.current])
        myobj.list.activate(myobj.current)
        myobj.list.itemconfigure(myobj.current,bg='sky blue')
        mixer.music.play()
    def pausesong(myobj):
        if not myobj.paused:
            myobj.paused=True
            mixer.music.pause()
            myobj.pause['image']=pause
        else:
            if myobj.played==False:
                myobj.playsong()
            myobj.paused=False
            mixer.music.unpause()
            myobj.pause['image']=play

    def prevsong(myobj):
        if myobj.current>0:
            myobj.current-=1
        else:
            myobj.current=0
        myobj.list.itemconfigure(myobj.current+1,bg='white')
        myobj.playsong()

    def nextsong(myobj):
        if myobj.current<len(myobj.playlist)-1:
            myobj.current+=1
        else:
            myobj.current=0
        myobj.list.itemconfigure(myobj.current-1,bg='white')
        myobj.playsong()

    def changevolume(myobj,event=None):
        myobj.v=myobj.volume.get()
        mixer.music.set_volume(myobj.v/10)
    


root=tk.Tk()
root.geometry('900x650')
root.configure(bg='black')
root.wm_title('Code Clause Music Player')

img = PhotoImage(file='images/music.gif')
nextt = PhotoImage(file = 'images/next.gif')
prev = PhotoImage(file='images/previous.gif')
play = PhotoImage(file='images/play.gif')
pause = PhotoImage(file='images/pause.gif')


obj=Musicplayer(master=root)
obj.mainloop()
