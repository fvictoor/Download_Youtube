from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from pkg_resources import resource_filename
import os

# Import de Image
icon_img = resource_filename(__name__,"icon.png")

def baixarVideo():
    #Baixar Video
    url_list = [entry0.get()]
    youtube = YouTube(str(url_list[0]))
    video = youtube.streams.get_highest_resolution()
    save_path = filedialog.asksaveasfilename(title="Salvar Arquivo", filetypes=[("Video MP4", ".mp4")])
    out_file = video.download(output_path=save_path)
    base, ext = os.path.splitext(out_file)
    new_file = base + ' Video.mp4'
    os.rename(out_file, new_file)

def baixarAudio():
    url_list = [entry0.get()]
    youtube = YouTube(str(url_list[0]))
    audio = youtube.streams.filter(only_audio=True).first()
    save_path = filedialog.asksaveasfilename(title="Salvar Arquivo", filetypes=[("Audio MP3", ".mp3")])
    out_file = audio.download(output_path=save_path)

    base, ext = os.path.splitext(out_file)
    new_file = base + ' Audio.mp3'
    os.rename(out_file, new_file)


window = Tk()
window.geometry("800x560")
window.title("Download Video Youtube")
window.configure(bg = "#ffffff")
window.iconbitmap(False, icon_img)
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 560,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_imp = resource_filename(__name__,"ibackground.png" )
background_img = PhotoImage(file=background_imp)
background = canvas.create_image(332.5, 280.0, image=background_img)

entry_img_imp = resource_filename(__name__,"img_textBox0.png")
entry0_img_TextBox = PhotoImage(file = entry_img_imp)
entry0_bg = canvas.create_image(604.0, 247.0, image=entry0_img_TextBox)

entry0 = Entry(bd = 0, bg = "#e7e7e7", highlightthickness = 0)
entry0.place(x = 453.0, y = 229, width = 302.0, height = 34)

imgVideo_imp = resource_filename(__name__,"img0.png" )
imgVideo = PhotoImage(file = imgVideo_imp)
b0 = Button(
    image = imgVideo,
    borderwidth = 0,
    highlightthickness = 0,
    command = baixarVideo,
    relief = "flat")

b0.place(
    x = 435, y = 307,
    width = 144,
    height = 49)

imgAudio_imp = resource_filename(__name__,"img1.png" )
imgAudio = PhotoImage(file = imgAudio_imp)
b1 = Button(
    image = imgAudio,
    borderwidth = 0,
    highlightthickness = 0,
    command = baixarAudio,
    relief = "flat")

b1.place(x = 628, y = 307, width = 144, height = 49)

window.resizable(False, False)
window.mainloop()
