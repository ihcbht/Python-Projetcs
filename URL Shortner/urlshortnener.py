from tkinter import *
from tkinter import ttk
import pyshorteners
import webbrowser


root=Tk()
root.title("URL Shortner")
root.geometry("1000x250")

label=ttk.Label(root, text="Code Clause URL Shortener", font=('verdana', 25))
label.grid(row=0)

iurl=ttk.Label(root, text="Original URL: ")
iurl.grid(row=1, column=0, pady=10)
url=StringVar()
eurl=ttk.Entry(root, textvariable=url, width=40)
eurl.grid(row=1, column=1, pady=10)

shortbutton=ttk.Button(root, text="Shorten", command= lambda: createshorturl(url.get()))
shortbutton.grid(row=2, column=0, pady=10)

shorturlbox=ttk.Label(root, text="Shortened Url: ")
shorturlbox.grid(row=4, column=0, pady=10)

ourl=StringVar()
ourl_entry=ttk.Entry(root, textvariable=ourl, width=40)
ourl_entry.grid(row=4, column=1, pady=10)

openbutton=ttk.Button(root, text="Open", command=lambda: openurl(url.get()))
openbutton.grid(row=5, column=1, pady=10)


def createshorturl(url):
    try:
        shorturl=pyshorteners.Shortener().tinyurl.short(url)
        ourl.set(shorturl)
    except:
        print("Invalid Url")

def openurl(url):
    try:
        webbrowser.open(url)
    except:
        print("invalid Url")
root.mainloop()