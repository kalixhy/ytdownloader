import tkinter

import  customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video =  ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color = "white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text = "Download Finished")

    except:
        finishLabel.configure(text = "Download Error", text_color = "red")

def on_progress(stream, chunk, bytes_remaining):   
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + "%")
    pPercentage.update()

    # to update progress bar
    progressBar.set(float(percentage_of_completion / 100))

# System settings for customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")



#Our app frame

app = customtkinter.CTk()
app.title("Yt Downloader")
app.geometry("720x480")

#Adding UI elements
title = customtkinter.CTkLabel(app, text = "Insert a Youtube link here")
title.pack(padx=10, pady=10)

#Adding link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width = 350, height = 40)
link.pack()

#Button for finsihed downloading 

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#display progress bar or percentage

pPercentage = customtkinter.CTkLabel(app, text = "0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)


download = customtkinter.CTkButton(app, text = "Download", command = startDownload)
download.pack(padx=10, pady=10)
# Run app 
app.mainloop()