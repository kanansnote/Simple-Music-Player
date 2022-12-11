# Importing Needed Modules

import os
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer

# Initializing root window

root = Tk()
root.title('Music player from kanansnote')
root.geometry('920x670+290+85')
root.configure(bg='#0f1a2b')
root.resizable(False, False)
mixer.init()


# Creating music player functions. 'Playlist' is the problematic function here.

def add_music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir()

        for song in songs:
            if song.endswith('.mp3'):
                playlist.insert(END, song)


def play_music():
    music_name = playlist.get(ACTIVE)
    print(music_name[0:-4])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()


# Making icon and logo

# Icon. The problem arose in 'root.iconphoto' with the 'icon_image' statement
icon_image = PhotoImage(file='logo.png')
root.iconphoto(False, icon_image)

top_image = PhotoImage(file='top.png')
Label(root, image=top_image, bg='#0f1a2b')

# Logo
logo_image = PhotoImage(file='logo.png')
Label(root, image=logo_image, bg='#0f1a2b').place(x=65, y=115)

# Creating music player buttons

# Button
button_play = PhotoImage(file='play.png')
Button(root, image=button_play, bg='#0f1a2b', bd=0, command=play_music).place(x=100, y=400)

button_stop = PhotoImage(file='stop.png')
Button(root, image=button_stop, bg="#0f1a2b", bd=0, command=mixer.music.stop).place(x=30, y=500)

button_resume = PhotoImage(file='resume.png')
Button(root, image=button_resume, bg='#0f1a2b', bd=0, command=mixer.music.unpause).place(x=115, y=500)

button_pause = PhotoImage(file='pause.png')
Button(root, image=button_pause, bg='#0f1a2b', bd=0, command=mixer.music.pause).place(x=200, y=500)

# Music
Menu = PhotoImage(file='menu.png')
Label(root, image=Menu, bg='#0f1a2b').pack(padx=10, pady=50, side=RIGHT)

frame_music = Frame(root, bd=2, relief=RIDGE)
frame_music.place(x=330, y=350, width=560, height=250)

Button(root, text='Add Music', width=15, height=2, font=('arial', 12, 'bold'),
       fg='Black', bg='#21b3de', command=add_music).place(x=330, y=300)

scroll = Scrollbar(frame_music)
playlist = Listbox(frame_music,
                   width=100, font=('arial', 10), bg='#333333', fg="grey",
                   selectbackground='lightblue', cursor='hand2', bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)

root.mainloop()

# Source = https://techvidvan.com/tutorials/python-create-mp3-music-player/
