import tkinter
from tkinter import *
import json
import os
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
from PyMovieDb import IMDB

def search():
    text = enter.get()
    imdb = IMDB()
    movie = imdb.get_by_name(enter.get())
    enter.delete(0, END)
    movie_dict = json.loads(movie)
    if len(movie_dict) > 7:
        genre = movie_dict['genre']
        gen_str = ",".join(genre)
        print(gen_str)
    else:
        return print(movie_dict)
    filepath = "searchdata.xlsx"

    if not os.path.exists(filepath):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        heading = ["Movies", "Genre"]
        sheet.append(heading)
        workbook.save(filepath)
    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook.active
    sheet.append([text, gen_str])
    workbook.save(filepath)

def helloCallBack():
    # read by default 1st sheet of an excel file
    df = pd.read_excel('searchdata.xlsx')
    genre_table = df.loc[:, "Genre"]

    # genres
    genre_dict = {
        "action": 0,
        'comedy': 0,
        'romance': 0,
        'adventure': 0,
        'sci-fi': 0,
        'thriller': 0,
        'fantasy': 0,
        'horror': 0,
        'short': 0,
        'documentary': 0,
        'crime': 0,
        'drama': 0,
        'musical': 0
    }

    for d in genre_table:
        arr = d.split(",")
        for ele in arr:
            if "Action" in ele:
                genre_dict['action'] += 1
            elif "Comedy" in ele:
                genre_dict['comedy'] += 1
            elif "Romance" in ele:
                genre_dict['romance'] += 1
            elif "Adventure" in ele:
                genre_dict['adventure'] += 1
            elif "Sci-Fi" in ele:
                genre_dict['sci-fi'] += 1
            elif "Thriller" in ele:
                genre_dict['thriller'] += 1
            elif "Fantasy" in ele:
                genre_dict['fantasy'] += 1
            elif "Horror" in ele:
                genre_dict['horror'] += 1
            elif "Short" in ele:
                genre_dict['short'] += 1
            elif "Documentary" in ele:
                genre_dict['documentary'] += 1
            elif "Crime" in ele:
                genre_dict['crime'] += 1
            elif "Drama" in ele:
                genre_dict['drama'] += 1
            elif "Musical" in ele:
                genre_dict['musical'] += 1
    print(genre_dict)

    # Data to plot Pie Chart
    labels = []
    sizes = []
    for x, y in genre_dict.items():
        labels.append(x)
        sizes.append(y)
    # Plot
    plt.pie(sizes, labels=labels)

    plt.axis('equal')
    # plt.legend()
    plt.show()

struct = tkinter.Tk()
struct.geometry("354x350")
struct.title("My Search Engine")
label = Label(struct, text="Web Search Application", bg="teal", fg="white", font=("Times", 20, "bold"))
label.pack(side=TOP)
struct.config(background="teal")

label = Label(struct, text="Enter here to search", bg="teal", fg="white", font=("Times", 15, "bold"))
label.place(x=50, y=100)
enter = Entry(struct, font=("Times", 10, "bold"), width=30, bd=2, bg="white")
enter.place(x=50, y=130)
button = Button(struct, text="Search", font=("Times", 10, "bold"), width=30, bd=2, command=search)
button1 = Button(struct, text="View Pie Chart", font=("Times", 10, "bold"), width=30, bd=2, command=helloCallBack)
button.place(x=50, y=170)
button1.place(x=50, y=210)
struct.mainloop()
