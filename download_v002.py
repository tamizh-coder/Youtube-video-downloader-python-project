from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
from turtle import left
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

 

import shutil

#functions

def select_path():
    #allows user to selct a path from the explorer
    path =filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path =path_label.cget("text")
    screen.title("Downloading!")
    #Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #movie file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title("Download Complete!, Try Another")
    
    
# Defining a function to toggle
# between light and dark theme
def toggle():
  
    global switch_value
    if switch_value == True:
        switch.config(image=new_dark, bg="#26242f",activebackground="#26242f")
          
        # Changes the window to dark theme
        canvas.config(bg="#26242f")  
        switch_value = False
  
    else:
        switch.config(image=new_light, bg="#F5F5F5", activebackground="#F5F5F5")
          
        # Changes the window to light theme
        canvas.config(bg="#F5F5F5")  
        switch_value = True
  
     
screen = Tk()
title = screen.title('Youtube Download')
canvas = Canvas(screen, width=500, height=600)
screen.config(bg="#F5F5F5")
canvas.pack()


# Adding light and dark mode images
light = (Image.open('C:\python_projects\\da.png'))
resized_light= light.resize((60,45), Image.ANTIALIAS)
new_light= ImageTk.PhotoImage(resized_light)

#resize
canvas.create_image(400,10, anchor=NW, image=new_light)

dark = (Image.open('C:\python_projects\\nt.png'))
resized_dark= dark.resize((60,45), Image.ANTIALIAS)
new_dark= ImageTk.PhotoImage(resized_dark)

#resize
canvas.create_image(400,10, anchor=NW, image=new_dark)
  
switch_value = True
  

  
# Creating a button to toggle
# between light and dark themes
switch = Button(screen, image=new_light,bd=0, bg="#F5F5F5",activebackground="#F5F5F5",command=toggle)
switch.pack(padx=0, pady=0)

canvas.create_window(430,27, window= switch)



#image Logo

logo_img=PhotoImage(file= r'C:\python_projects\yt1.png')

#resize
logo_img = logo_img.subsample(6,6)

canvas.create_image(250,120,image=logo_img)

#link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Download URL:", font=(15))

# Select Path for save the file

path_label = Label(screen,text="Select path for Download",font=(12))
select_btn = Button(screen, text='Select', command=select_path)
select_btn.pack(side=LEFT)
canvas.create_window(250,360, window= select_btn)

# add window

canvas.create_window(250,320, window = path_label)
canvas.create_window(250,260, window=link_field)

# add widgets windows
canvas.create_window(250,210, window=link_label)
canvas.create_window(250,240, window=link_field)


#download btn

download_btn = Button(screen, text= "Download File", command=download_file)
download_btn.pack()




#add to canvas
canvas.create_window(250,410, window= download_btn)





screen.mainloop()