                          ############       Aztec Music Player          ############

from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3

root = Tk()
root.geometry("900x400+200+50")
root.title("Aztec Music Player")
root.iconbitmap("aztec.ico")
root.resizable(False,False)
root.configure(bg="#2F4F4F")

############################################ Global Varriable
audiotrack = StringVar()
totalsonglength=0
count=0
text=""

def musicurl():
    url = filedialog.askopenfilename()
    audiotrack.set(url)
def playmusic():
    add=audiotrack.get()
    mixer.music.load(add)
    mixer.music.play()
    AudioStatusLabel.configure(text="Playing...")
    ProgressbarMusicLabel.grid()

    Song=MP3(add)
    totalsonglength=int(Song.info.length)
    ProgressbarMusic["maximum"]=totalsonglength
    ProgressbarMusicEndTimeLabel.configure(text="{}".format(str(datetime.timedelta(seconds=totalsonglength))))

        def Progressbarmusictick():
        CurrentSongLength=mixer.music.get_pos()//1000
        ProgressbarMusic["value"]=CurrentSongLength
        ProgressbarMusicStartTimeLabel.configure(text="{}".format(str(datetime.timedelta(seconds=CurrentSongLength))))
        ProgressbarMusic.after(2,Progressbarmusictick)
    Progressbarmusictick()

def pausemusic():
    mixer.music.pause()
    root.PauseButton.grid_remove()
    root.ResumeButton.grid()
    AudioStatusLabel.configure(text="Paused")
def resumemusic():
    root.ResumeButton.grid_remove()
    root.PauseButton.grid()
    mixer.music.unpause()
    AudioStatusLabel.configure(text="Playing...")
def volumeup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol+0.1)
def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol-0.1)
def stopmusic():
    mixer.music.stop()
    AudioStatusLabel.configure(text="Music Stopped!Play Again")
def createwidthes():
    global browse,play,pause,stop,volumeup,volumedown,resume
    global AudioStatusLabel
    global ProgressbarMusicLabel
    global ProgressbarMusic
    global ProgressbarMusicEndTimeLabel
    global ProgressbarMusicStartTimeLabel

############################################ Button Images
    browse = PhotoImage(file="browse.png")
    play = PhotoImage(file="play.png")
    pause = PhotoImage(file="pause.png")
    resume = PhotoImage(file="resume.png")
    stop = PhotoImage(file="stop.png")
    volumeup = PhotoImage(file="volumeup.png")
    volumedown = PhotoImage(file="volumedown.png")
############################################ Button Images resizing
    browse = browse.subsample(25,25)
    play =play.subsample(29,29)
    pause =pause.subsample(30,30)
    resume = resume.subsample(33,33)
    stop =stop.subsample(25,25)
    volumeup =volumeup.subsample(25,25)
    volumedown =volumedown.subsample(25,25)
############################################ Labels
    TrackLabel = Label(root,text = "Select Audio Track  :",bg = "#2F4F4F",fg="white", font =("Verdana","15","bold"))
    TrackLabel.grid(row=0,column=0,padx=20,pady=20 )

    AudioStatusLabel= Label(root,text = "",bg = "#2F4F4F",font =("Rockwell","12","bold"),width=30)
    AudioStatusLabel.grid(row=2,column=1,padx=20,pady=20)

############################################ Entry Box
    TrackLabelEntry = Entry(root,font =("Arial","16"),width=30,text=audiotrack)
    TrackLabelEntry.grid(row=0,column=1,padx=20,pady=20 )

############################################ Buttons
    BrowseButton = Button(root,text = "Search",bg = "#66CDAA",font =("Rockwell","12","bold"),width=100,bd=2,image=browse
                          ,compound=RIGHT,command=musicurl)
    BrowseButton.grid(row=0,column=3,padx=20,pady=20)

    PlayButton = Button(root, text="Play ", bg="#FFC300", font=("Rockwell", "12", "bold"), width=100, bd=2,image=play
                        ,compound=RIGHT,command=playmusic)
    PlayButton.grid(row=1, column=0, padx=20, pady=20)

    root.PauseButton = Button(root, text="Pause ", bg="#FF5733", font=("Rockwell", "12", "bold"), width=100, bd=2,image=pause
                              ,compound=RIGHT,command=pausemusic)
    root.PauseButton.grid(row=1, column=1, padx=20, pady=20)

    root.ResumeButton = Button(root, text="Resume ", bg="#FF5733", font=("Rockwell", "12", "bold"), width=100, bd=2,
                         image=resume, compound=RIGHT,command=resumemusic)
    root.ResumeButton.grid(row=1, column=1, padx=20, pady=20)
    root.ResumeButton.grid_remove()

    VolumeUpButton = Button(root, text="Vol+", bg="#ADFF2F", font=("Rockwell", "12", "bold"), width=100, bd=2,image=volumeup
                            ,compound=RIGHT,command=volumeup)
    VolumeUpButton.grid(row=1, column=3, padx=20, pady=20)

    VolumeDownButton = Button(root, text="Vol-", bg="#ADFF2F", font=("Rockwell", "12", "bold"), width=100, bd=2,image=volumedown
                              ,compound=RIGHT,command=volumedown)
    VolumeDownButton.grid(row=2, column=3, padx=20, pady=20)

    StopButton = Button(root, text="Stop ", bg="#DC143C", font=("Rockwell", "12", "bold"), width=100, bd=2,image=stop
                        ,compound=RIGHT,command=stopmusic)
    StopButton.grid(row=2, column=0, padx=20, pady=20)
############################################ Pogressbar music
    ProgressbarMusicLabel = Label(root,text="", bg="black")
    ProgressbarMusicLabel.grid(row=3, column=0, columnspan=4,padx=20,pady=20)
    ProgressbarMusicLabel.grid_remove()

    ProgressbarMusic = Progressbar(ProgressbarMusicLabel, orient=HORIZONTAL, mode="determinate", value=0)
    ProgressbarMusic.grid(row=0, column=1, ipadx=200, ipady=3)

    ProgressbarMusicStartTimeLabel = Label(ProgressbarMusicLabel, text="0:00", bg="#7B68EE",font="bold")
    ProgressbarMusicStartTimeLabel.grid(row=0, column=0)

    ProgressbarMusicEndTimeLabel = Label(ProgressbarMusicLabel, text="0:00", bg="#7B68EE",font="bold")
    ProgressbarMusicEndTimeLabel.grid(row=0, column=2)

############################################ Slider section
    slider = "Developed by Aztec"
    SliderLabel = Label(root, text=slider, bg="#2F4F4F", fg="#FF7F50", font=("Comic Sans MS", "20", "bold"))
    SliderLabel.grid(row=5, column=1, padx=20, pady=20, columnspan=6)


mixer.init()
createwidthes()
root.mainloop()




                                         ############# End ##############