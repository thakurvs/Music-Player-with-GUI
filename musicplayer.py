import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

# Creating application window
musicplayer = tkr.Tk()

# setting the title
musicplayer.title("Welcome To Music Player")

# Setting dimensions for application window
musicplayer.geometry('550x450')

# asking for the music directory
directory = askdirectory()

# setting music directory to the current working directory
os.chdir(directory)

# creating song list
# os.listdir() method return a list containing the names of entries in the directory given by path
songlist = os.listdir()

# creating the playlist
playlist = tkr.Listbox(musicplayer, font="Cambria 14 bold", bg="cyan2", selectmode=tkr.SINGLE)

# Adding songs from songlist to playlist
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos+1

# initialize the pygame module to load and play the selected song
pygame.init()
pygame.mixer.init()

# function for play button
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

# function for stop button
def ExitMusicPlayer():
    pygame.mixer.music.stop()

# function for pause button
def pause():
    pygame.mixer.music.pause()

# function for resume button
def resume():
    pygame.mixer.music.unpause()

Button_play = tkr.Button(musicplayer, height="3", width="5", text="Play Music", font="Cambria 14 bold", command=play, bg="lime green", fg="black")
Button_stop = tkr.Button(musicplayer, height="3", width="5", text="Stop Music", font="Cambria 14 bold", command=ExitMusicPlayer, bg="red", fg="black")
Button_pause = tkr.Button(musicplayer, height="3", width="5", text="Pause Music", font="Cambria 14 bold", command=pause, bg="orange", fg="black")
Button_resume = tkr.Button(musicplayer, height="3", width="5", text="Resume Music", font="Cambria 14 bold", command=resume, bg="yellow", fg="black")

Button_play.pack(fill="x")
Button_stop.pack(fill="x")
Button_pause.pack(fill="x")
Button_resume.pack(fill="x")

playlist.pack(fill="both", expand="yes")

var = tkr.StringVar()
songtitle = tkr.Label(musicplayer, font="Cambria 20 bold", textvariable=var)
songtitle.pack()
musicplayer.mainloop()