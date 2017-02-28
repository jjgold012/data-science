from tkinter import ttk

import matplotlib
import sys
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pymysql
from matplotlib import pylab as plt
from tkinter.scrolledtext import *
matplotlib.use("TkAgg")
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk

PRINT_FONT = ("Helvetica", 12, "bold")
TITLE_FONT = ("Helvetica", 16, "bold")
BASKETBALL_FONT = ("Helvetica", 14, "bold")
ALL_FONT = ("Helvetica", 20, "bold")


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.attributes("-fullscreen", True)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, HelpPage, AllSportsPage, AllSportsOpt1Page, AllSportsOpt2Page, AllSportsOpt3Page,
                  AllSportsOpt4Page, SoccerPage, SoccerOpt1Page, SoccerOpt2Page, SoccerOpt3Page, SoccerOpt4Page, FootballPage,
                  AmericanFootballPage, AmericanFootballOpt1Page, FootballComparePage, AustralianFootballPage,
                  AustralianFootballOpt1Page, CricketPage, CricketOpt1Page, CricketOpt2Page, BasketballPage,
                  BasketballOpt1Page, BasketballOpt2Page, HockeyPage, HockeyOpt1Page, HockeyOpt2Page, RugbyPage,
                  RugbyOpt1Page, RugbyOpt2Page, TennisPage, TennisOpt1Page, TennisOpt2Page):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, c):
        frame = self.frames[c]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/sports2.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Main", bg="white", font=TITLE_FONT)
        label.place(x=620, y=50, width=100, height=44)
        help_btn = tk.Button(self, text="Help", width=3, command=lambda: controller.show_frame(HelpPage))
        soccer_btn = tk.Button(self, text="Soccer", width=10, bg="green", font=TITLE_FONT,
                               command=lambda: controller.show_frame(SoccerPage))
        football_btn = tk.Button(self, text="football", width=10, bg="red", font=TITLE_FONT,
                                 command=lambda: controller.show_frame(FootballPage))
        cricket_btn = tk.Button(self, text="cricket", width=10, bg="blue", font=TITLE_FONT,
                                command=lambda: controller.show_frame(CricketPage))
        basketball_btn = tk.Button(self, text="basketball", width=10, bg="cyan", font=BASKETBALL_FONT,
                                   command=lambda: controller.show_frame(BasketballPage))
        hockey_btn = tk.Button(self, text="hockey", width=10, bg="orange red", font=TITLE_FONT,
                               command=lambda: controller.show_frame(HockeyPage))
        rugby_btn = tk.Button(self, text="rugby", width=10, bg="purple4", font=TITLE_FONT,
                              command=lambda: controller.show_frame(RugbyPage))
        tennis_btn = tk.Button(self, text="tennis", width=10, bg="goldenrod1", font=TITLE_FONT,
                               command=lambda: controller.show_frame(TennisPage))
        all_sports_btn = tk.Button(self, text="All-Sports", width=10, bg="wheat", font=ALL_FONT,
                                   command=lambda: controller.show_frame(AllSportsPage))
        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        help_btn.place(x=0, y=725, width=80, height=44)
        all_sports_btn.place(x=220, y=725, width=150, height=44)
        soccer_btn.place(x=365, y=725, width=100, height=44)
        basketball_btn.place(x=465, y=725, width=100, height=44)
        football_btn.place(x=565, y=725, width=100, height=44)
        hockey_btn.place(x=665, y=725, width=100, height=44)
        tennis_btn.place(x=765, y=725, width=100, height=44)
        rugby_btn.place(x=865, y=725, width=100, height=44)
        cricket_btn.place(x=965, y=725, width=100, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class HelpPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/sports2.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Help\n\nIn this software you are able to view some stats\nand interesting facts"
                                    " about teams, betting odds\n of different sports and more...\n\n"
                                    "Choose your favorite sport and enjoy!", bg="white", font=TITLE_FONT)
        label.place(x=400, y=250, width=550, height=250)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class AllSportsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/sports2.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="All-Sports", bg="wheat", font=TITLE_FONT)
        label.place(x=620, y=50, width=120, height=44)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Most Predictable", bg="white",
                            command=lambda: controller.show_frame(AllSportsOpt1Page))
        option2 = tk.Button(self, text="Most Unpredictable", bg="white",
                            command=lambda: controller.show_frame(AllSportsOpt2Page))
        option3 = tk.Button(self, text="# Home Wins", bg="white",
                            command=lambda: controller.show_frame(AllSportsOpt3Page))
        option4 = tk.Button(self, text="# Away Wins", bg="white",
                            command=lambda: controller.show_frame(AllSportsOpt4Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=450, y=725, width=120, height=44)
        option2.place(x=570, y=725, width=120, height=44)
        option3.place(x=690, y=725, width=120, height=44)
        option4.place(x=810, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class AllSportsOpt1Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/sports2.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="All-Sports", bg="wheat", font=TITLE_FONT)
        label.place(x=620, y=50, width=120, height=44)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Most Predictable", bg="white",
                            command=lambda: controller.show_frame(AllSportsOpt1Page))
        option2 = tk.Button(self, text="Most Unpredictable", bg="white",
                            command=lambda: controller.show_frame(AllSportsOpt2Page))
        option3 = tk.Button(self, text="# Home Wins", bg="white",
                            command=lambda: controller.show_frame(AllSportsOpt3Page))
        option4 = tk.Button(self, text="# Away Wins", bg="white",
                            command=lambda: controller.show_frame(AllSportsOpt4Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=450, y=725, width=120, height=44)
        option2.place(x=570, y=725, width=120, height=44)
        option3.place(x=690, y=725, width=120, height=44)
        option4.place(x=810, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class AllSportsOpt2Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/sports2.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="All-Sports", bg="wheat", font=TITLE_FONT)
        label.place(x=620, y=50, width=120, height=44)

        image = plt.imread('all/charts/underdog.png')
        fig = plt.figure(figsize=(8, 7))
        im = plt.imshow(image)
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.NONE, expand=False)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Most Predictable", bg="white",
                            command=lambda: controller.show_frame(AllSportsOpt1Page))
        option2 = tk.Button(self, text="Most Unpredictable", bg="white",
                            command=lambda: controller.show_frame(AllSportsOpt2Page))
        option3 = tk.Button(self, text="# Home Wins", bg="white",
                            command=lambda: controller.show_frame(AllSportsOpt3Page))
        option4 = tk.Button(self, text="# Away Wins", bg="white",
                            command=lambda: controller.show_frame(AllSportsOpt4Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=450, y=725, width=120, height=44)
        option2.place(x=570, y=725, width=120, height=44)
        option3.place(x=690, y=725, width=120, height=44)
        option4.place(x=810, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class AllSportsOpt3Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/sports2.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="All-Sports", bg="wheat", font=TITLE_FONT)
        label.place(x=620, y=50, width=120, height=44)

        image = plt.imread('all/charts/home.png')
        fig = plt.figure(figsize=(8, 7))
        im = plt.imshow(image)
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.NONE, expand=False)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Most Predictable", bg="white",
                            command=lambda: controller.show_frame(AllSportsOpt1Page))
        option2 = tk.Button(self, text="Most Unpredictable", bg="white",
                            command=lambda: controller.show_frame(AllSportsOpt2Page))
        option3 = tk.Button(self, text="# Home Wins", bg="white",
                            command=lambda: controller.show_frame(AllSportsOpt3Page))
        option4 = tk.Button(self, text="# Away Wins", bg="white",
                            command=lambda: controller.show_frame(AllSportsOpt4Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=450, y=725, width=120, height=44)
        option2.place(x=570, y=725, width=120, height=44)
        option3.place(x=690, y=725, width=120, height=44)
        option4.place(x=810, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


# class AllSportsOpt3Page(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         logo = tk.PhotoImage(file=r"backgrounds/sports2.png")
#         BGlabel = tk.Label(self, image=logo)
#         BGlabel.image = logo
#         BGlabel.place(x=0, y=0, width=1571, height=839)
#         label = tk.Label(self, text="All-Sports", bg="wheat", font=TITLE_FONT)
#         label.place(x=620, y=50, width=120, height=44)
#
#         T = tk.Text(self, height=2, width=52, font=PRINT_FONT)
#         T.pack(side=tk.BOTTOM, ipady=40, expand=False)
#         query = "select (select count(*) from soccer where (winner = 'H')) + (select count(*) from american_football" \
#                 " where (winner = 'H'))+(select count(*) from australian_football where (winner = 'H'))+" \
#                 "(select count(*) from basketball where (winner = 'H'))+(select count(*) from cricket where" \
#                 " (winner = 'H'))+(select count(*) from hockey where (winner = 'H'))+(select count(*)" \
#                 " from rugby where (winner = 'H'))+(select count(*) from tennis_men where (winner = 'H'))+" \
#                 "(select count(*) from tennis_women where (winner = 'H'));"
#         T.insert(tk.END, "The total number of wins by home teams is: " + str(make_query(query)[0]))
#
#         exit_btn = tk.Button(self, text="Exit", command=self.quit)
#         option1 = tk.Button(self, text="Most Predictable", bg="white",
#                             command=lambda: controller.show_frame(AllSportsOpt1Page))
#         option2 = tk.Button(self, text="Most Unpredictable", bg="white",
#                             command=lambda: controller.show_frame(AllSportsOpt2Page))
#         option3 = tk.Button(self, text="# Home Wins", bg="white",
#                             command=lambda: controller.show_frame(AllSportsOpt3Page))
#         option4 = tk.Button(self, text="# Away Wins", bg="white",
#                             command=lambda: controller.show_frame(AllSportsOpt4Page))
#         back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
#         back.place(x=0, y=725, width=80, height=44)
#         option1.place(x=450, y=725, width=120, height=44)
#         option2.place(x=570, y=725, width=120, height=44)
#         option3.place(x=690, y=725, width=120, height=44)
#         option4.place(x=810, y=725, width=120, height=44)
#         exit_btn.place(x=1288, y=725, width=80, height=44)


class AllSportsOpt4Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/sports2.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="All-Sports", bg="wheat", font=TITLE_FONT)
        label.place(x=620, y=50, width=120, height=44)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Most Predictable", bg="white",
                            command=lambda: controller.show_frame(AllSportsOpt1Page))
        option2 = tk.Button(self, text="Most Unpredictable", bg="white",
                            command=lambda: controller.show_frame(AllSportsOpt2Page))
        option3 = tk.Button(self, text="# Home Wins", bg="white",
                            command=lambda: controller.show_frame(AllSportsOpt3Page))
        option4 = tk.Button(self, text="# Away Wins", bg="white",
                            command=lambda: controller.show_frame(AllSportsOpt4Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=450, y=725, width=120, height=44)
        option2.place(x=570, y=725, width=120, height=44)
        option3.place(x=690, y=725, width=120, height=44)
        option4.place(x=810, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class SoccerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/soccer.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Soccer", bg="green", font=TITLE_FONT)
        label.place(x=620, y=50, width=100, height=44)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Big Clubs\nwins\\total", bg="green",
                            command=lambda: controller.show_frame(SoccerOpt1Page))
        option2 = tk.Button(self, text="Big Clubs\ntotal of draws", bg="green",
                            command=lambda: controller.show_frame(SoccerOpt2Page))
        option3 = tk.Button(self, text="Big Clubs\nloses\\total", bg="green",
                            command=lambda: controller.show_frame(SoccerOpt3Page))
        option4 = tk.Button(self, text="Queries", bg="green",
                            command=lambda: controller.show_frame(SoccerOpt4Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=450, y=725, width=120, height=44)
        option2.place(x=570, y=725, width=120, height=44)
        option3.place(x=690, y=725, width=120, height=44)
        option4.place(x=810, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class SoccerOpt1Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/soccer.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Soccer", bg="green", font=TITLE_FONT)
        label.place(x=620, y=50, width=100, height=44)

        image = plt.imread('soccer/charts/wins_total.png')
        fig = plt.figure(figsize=(8, 7))
        im = plt.imshow(image)
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.NONE, expand=False)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Big Clubs\nwins\\total", bg="green",
                            command=lambda: controller.show_frame(SoccerOpt1Page))
        option2 = tk.Button(self, text="Big Clubs\ntotal of draws", bg="green",
                            command=lambda: controller.show_frame(SoccerOpt2Page))
        option3 = tk.Button(self, text="Big Clubs\nloses\\total", bg="green",
                            command=lambda: controller.show_frame(SoccerOpt3Page))
        option4 = tk.Button(self, text="Queries", bg="green",
                            command=lambda: controller.show_frame(SoccerOpt4Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=450, y=725, width=120, height=44)
        option2.place(x=570, y=725, width=120, height=44)
        option3.place(x=690, y=725, width=120, height=44)
        option4.place(x=810, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class SoccerOpt2Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/soccer.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Soccer", bg="green", font=TITLE_FONT)
        label.place(x=620, y=50, width=100, height=44)

        image = plt.imread('soccer/charts/draws.png')
        fig = plt.figure(figsize=(8, 7))
        im = plt.imshow(image)
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.NONE, expand=False)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Big Clubs\nwins\\total", bg="green",
                            command=lambda: controller.show_frame(SoccerOpt1Page))
        option2 = tk.Button(self, text="Big Clubs\ntotal of draws", bg="green",
                            command=lambda: controller.show_frame(SoccerOpt2Page))
        option3 = tk.Button(self, text="Big Clubs\nloses\\total", bg="green",
                            command=lambda: controller.show_frame(SoccerOpt3Page))
        option4 = tk.Button(self, text="Queries", bg="green",
                            command=lambda: controller.show_frame(SoccerOpt4Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=450, y=725, width=120, height=44)
        option2.place(x=570, y=725, width=120, height=44)
        option3.place(x=690, y=725, width=120, height=44)
        option4.place(x=810, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class SoccerOpt3Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/soccer.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Soccer", bg="green", font=TITLE_FONT)
        label.place(x=620, y=50, width=100, height=44)

        image = plt.imread('soccer/charts/loses_total.png')
        fig = plt.figure(figsize=(8, 7))
        im = plt.imshow(image)
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.NONE, expand=False)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Big Clubs\nwins\\total", bg="green",
                            command=lambda: controller.show_frame(SoccerOpt1Page))
        option2 = tk.Button(self, text="Big Clubs\ntotal of draws", bg="green",
                            command=lambda: controller.show_frame(SoccerOpt2Page))
        option3 = tk.Button(self, text="Big Clubs\nloses\\total", bg="green",
                            command=lambda: controller.show_frame(SoccerOpt3Page))
        option4 = tk.Button(self, text="Queries", bg="green",
                            command=lambda: controller.show_frame(SoccerOpt4Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=450, y=725, width=120, height=44)
        option2.place(x=570, y=725, width=120, height=44)
        option3.place(x=690, y=725, width=120, height=44)
        option4.place(x=810, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class SoccerOpt4Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/soccer.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Soccer", bg="green", font=TITLE_FONT)
        label.place(x=620, y=50, width=100, height=44)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Big Clubs\nwins\\total", bg="green",
                            command=lambda: controller.show_frame(SoccerOpt1Page))
        option2 = tk.Button(self, text="Big Clubs\ntotal of draws", bg="green",
                            command=lambda: controller.show_frame(SoccerOpt2Page))
        option3 = tk.Button(self, text="Big Clubs\nloses\\total", bg="green",
                            command=lambda: controller.show_frame(SoccerOpt3Page))
        option4 = tk.Button(self, text="Queries", bg="green",
                            command=lambda: controller.show_frame(SoccerOpt4Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=450, y=725, width=120, height=44)
        option2.place(x=570, y=725, width=120, height=44)
        option3.place(x=690, y=725, width=120, height=44)
        option4.place(x=810, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)

        self.frame = tk.Frame(self)
        self.frame.pack(fill=tk.X)
        self.leagues = ['Premier League', 'Championship', 'Spanish La Liga', 'Italian Seria A', 'French Liga 1',
                   'German Bundesliga']
        self.premier_cb = ['Hull', 'Watford', 'Aston Villa', 'Swansea', 'Fulham', 'Liverpool', 'Burnley', 'Blackpool',
                      'West Brom', 'Chelsea', 'Leicester', 'Reading', 'Cardiff', 'Wolves', 'Portsmouth', 'Everton',
                      'Middlesboro', 'Norwich', 'Arsenal', 'Bournemouth', 'Derby', 'Crystal Palace', 'Man United',
                      'Newcastle', 'Southampton', 'West Ham', 'Wigan', 'QPR', 'Sheffield United', 'Leeds', 'Blackburn',
                      'Stoke', 'Middlesbrough', 'Man City', 'Tottenham', 'Charlton', 'Birmingham', 'Sunderland',
                      'Bolton']
        self.champ_cb = ['Brighton', 'Barnsley', 'Bristol City', 'Fulham', 'Portsmouth', 'Norwich', 'Hull', 'Coventry',
                    'Gillingham', 'Walsall', 'Bradford', 'Bournemouth', 'Southend', 'Bolton', 'Sunderland',
                    'Southampton', 'Peterboro', 'Leeds', 'Leicester', 'Charlton', 'Blackburn', 'Yeovil',
                    'Crystal Palace', 'Blackpool', 'West Ham', 'Cardiff', 'Burton', 'Crewe', 'Plymouth',
                    'Preston', 'Newcastle', "Nott'm Forest", 'Sheffield Weds', 'QPR', 'Colchester', 'Ipswich',
                    'Huddersfield', 'Wigan', 'Rotherham', 'Middlesbrough', 'Reading', 'Wimbledon', 'Swansea',
                    'Millwall', 'Wolves', 'West Brom', 'Aston Villa', 'Stoke', 'Burnley', 'Grimsby', 'Brentford',
                    'Sheffield United', 'Milton Keynes Dons', 'Derby', 'Scunthorpe', 'Luton', 'Watford',
                    'Doncaster', 'Birmingham']

        self.italian1_cb = ['Lazio', 'Torino', 'Sassuolo', 'Perugia', 'Como', 'Chievo', 'Roma', 'Udinese', 'Empoli', 'Cesena',
                       'Juventus', 'Cagliari', 'Brescia', 'Livorno', 'Atalanta', 'Verona', 'Napoli', 'Parma', 'Ancona',
                       'Bologna', 'Ascoli', 'Lecce', 'Inter', 'Carpi', 'Siena', 'Milan', 'Reggina', 'Catania', 'Treviso',
                       'Messina', 'Frosinone', 'Crotone', 'Modena', 'Fiorentina', 'Sampdoria', 'Novara', 'Bari',
                       'Piacenza', 'Genoa', 'Pescara', 'Palermo']

        self.f1_cb = ['Strasbourg', 'Metz', 'Lorient', 'Paris SG', 'Toulouse', 'St Etienne', 'Istres', 'Angers', 'Sedan',
                 'Boulogne', 'Bordeaux', 'Marseille', 'Nantes', 'Monaco', 'Ajaccio', 'Le Havre', 'Nice', 'Caen',
                 'Rennes', 'Lyon', 'Sochaux', 'Nancy', 'Grenoble', 'Guingamp', 'Reims', 'Ajaccio GFCO', 'Le Mans',
                 'Bastia', 'Dijon', 'Evian Thonon Gaillard', 'Lille', 'Valenciennes', 'Lens', 'Troyes', 'Auxerre',
                 'Montpellier', 'Brest', 'Arles']
        self.sp_cb = ['Albacete', 'Leganes', 'Cordoba', 'Levante', 'Ath Bilbao', 'Real Madrid', 'Hercules', 'La Coruna',
                 'Sp Gijon', 'Valencia', 'Granada', 'Santander', 'Eibar', 'Murcia', 'Sociedad', 'Las Palmas', 'Almeria',
                 'Valladolid', 'Espanol', 'Getafe', 'Ath Madrid', 'Villarreal', 'Recreativo', 'Sevilla', 'Xerez',
                 'Osasuna', 'Malaga', 'Mallorca', 'Zaragoza', 'Elche', 'Vallecano', 'Gimnastic', 'Numancia', 'Celta',
                 'Tenerife', 'Alaves', 'Cadiz', 'Barcelona', 'Betis']
        self.ger_cb = ['RB Leipzig', 'Salzburg', 'Austria Vienna', 'SV Werder Bremen', 'Ingolstadt', 'Rapid Vienna',
                  'Sturm Graz', 'Mattersburg', 'Hamburger SV', 'Schalke', 'Ried', 'FC Augsburg', 'Darmstadt',
                  'St. Polten', 'SC Freiburg', 'Wolfsburg', 'AC Wolfsberger', 'Bayer Leverkusen', 'B. Monchengladbach',
                  'Admira', 'Altach', 'Dortmund', 'Bayern Munich', 'Hertha Berlin', 'Hoffenheim', '1. FSV Mainz 05',
                  '1. FC Koln', 'Eintracht Frankfurt']

        self.query_part1 = "select * from soccer where home_team = "
        self.query_part2 = " or away_team = "

        self.league_cb = ttk.Combobox(self.frame, height=200, width=60, values=self.leagues)
        self.league_cb.pack(side=tk.LEFT)
        self.league_cb.bind("<<ComboboxSelected>>", self.get_league)
        self.league_cb.set(self.leagues[0])
        self.display_query = ScrolledText(self, bg='white', width=165, height=25, font="Arial 12")
        self.display_query.pack()
        self.club_cb = ttk.Combobox(self.frame, height=200, width=60, values=self.premier_cb)
        self.club_cb.pack(side=tk.LEFT)
        self.club_cb.bind("<<ComboboxSelected>>", self.make_query)
        self.club_cb.set(self.premier_cb[0])
        self.display((self.query_part1 + "\'" + str(self.club_cb.get()) + "\'" + self.query_part2 + "\'" +
                                   str(self.club_cb.get()) + "\'" + ';'))

    def get_league(self, event):
        league = self.league_cb.get()
        if league == 'Premier League':
            self.club_cb['values'] = self.premier_cb
            self.club_cb.set(self.premier_cb[0])
        elif league == 'Championship':
            self.club_cb['values'] = self.champ_cb
            self.club_cb.set(self.champ_cb[0])
        elif league == 'Spanish La Liga':
            self.club_cb['values'] = self.sp_cb
            self.club_cb.set(self.sp_cb[0])
        elif league == 'Italian Seria A':
            self.club_cb['values'] = self.italian1_cb
            self.club_cb.set(self.italian1_cb[0])
        elif league == 'French Liga 1':
            self.club_cb['values'] = self.f1_cb
            self.club_cb.set(self.f1_cb[0])
        else:  # Bundesliga
            self.club_cb['values'] = self.ger_cb
            self.club_cb.set(self.ger_cb[0])
        self.display_query.delete('1.0', tk.END)
        self.display((self.query_part1 + "\'" + str(self.club_cb.get()) + "\'" + self.query_part2 + "\'" +
                      str(self.club_cb.get()) + "\'" + ';'))
        return

    def make_query(self, event):
        self.display_query.delete('1.0', tk.END)
        self.display((self.query_part1 + "\'" + str(self.club_cb.get()) + "\'" + self.query_part2 + "\'" +
                            str(self.club_cb.get()) + "\'" + ';'))

    def display(self, sql):
        query_result = make_query(sql)
        print(query_result)
        self.display_query.insert("insert",
                                  "Date\t\tLeague\t\t  Home Team\t\t\tAwayTeam\t\t\tResult\tHome Result\t\tAway Result\n\n")
        for result in query_result:
            self.display_query.insert("insert", (str(result[0]) + '\t\t' + str(result[1]) + '\t\t   ' +
                                                 str(result[2]) + '\t\t\t' + str(result[3]) + '\t\t\t  ' +
                                                 str(result[4]) + '\t         ' + str(result[5]) + '\t\t        ' +
                                                 str(result[6]) + '\n'))


class BasketballPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/basketball.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Basketball", bg="cyan", font=TITLE_FONT)
        label.place(x=620, y=50, width=150, height=44)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Most Predictable", bg="cyan",
                            command=lambda: controller.show_frame(BasketballOpt1Page))
        option2 = tk.Button(self, text="Most Unpredictable", bg="cyan",
                            command=lambda: controller.show_frame(BasketballOpt2Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=590, y=725, width=120, height=44)
        option2.place(x=710, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class BasketballOpt1Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/basketball.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Basketball", bg="cyan", font=TITLE_FONT)
        label.place(x=620, y=50, width=150, height=44)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Most Predictable", bg="cyan",
                            command=lambda: controller.show_frame(BasketballOpt1Page))
        option2 = tk.Button(self, text="Most Unpredictable", bg="cyan",
                            command=lambda: controller.show_frame(BasketballOpt2Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=590, y=725, width=120, height=44)
        option2.place(x=710, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class BasketballOpt2Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/basketball.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Basketball", bg="cyan", font=TITLE_FONT)
        label.place(x=620, y=50, width=150, height=44)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Most Predictable", bg="cyan",
                            command=lambda: controller.show_frame(BasketballOpt1Page))
        option2 = tk.Button(self, text="Most Unpredictable", bg="cyan",
                            command=lambda: controller.show_frame(BasketballOpt2Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=590, y=725, width=120, height=44)
        option2.place(x=710, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class FootballPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/football.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Football", bg="red", font=TITLE_FONT)
        label.place(x=620, y=50, width=110, height=44)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        american_btn = tk.Button(self, text="American Football", bg="red",
                                 command=lambda: controller.show_frame(AmericanFootballPage))
        cmp_btn = tk.Button(self, text="Score Compare\nBetween Two", bg="white",
                                   command=lambda: controller.show_frame(FootballComparePage))
        australian_btn = tk.Button(self, text="Australian Football", bg="red",
                                   command=lambda: controller.show_frame(AustralianFootballPage))
        back.place(x=0, y=725, width=80, height=44)
        american_btn.place(x=500, y=725, width=120, height=44)
        cmp_btn.place(x=620, y=725, width=120, height=44)
        australian_btn.place(x=740, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class FootballComparePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/football.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Football", bg="red", font=TITLE_FONT)
        label.place(x=620, y=50, width=110, height=44)

        image = plt.imread('football/charts/avg_score.png')
        fig = plt.figure(figsize=(8, 7))
        im = plt.imshow(image)
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.NONE, expand=False)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(FootballPage))
        back.place(x=0, y=725, width=80, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class AmericanFootballPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/football.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="American Football", bg="red", font=TITLE_FONT)
        label.place(x=600, y=50, width=195, height=44)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Total score\nof all teams", bg="red",
                            command=lambda: controller.show_frame(AmericanFootballOpt1Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(FootballPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=620, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class AmericanFootballOpt1Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/football.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="American Football", bg="red", font=TITLE_FONT)
        label.place(x=600, y=50, width=195, height=44)
        T = tk.Text(self, height=2, width=52, font=PRINT_FONT)
        T.pack(side=tk.BOTTOM, ipady=40, expand=False)
        query = "select(select sum(home_score) from american_football)+(select sum(away_score) from american_football);"
        T.insert(tk.END, "\n\n\n            The total score of all teams in 1978 is: " + str(make_query(query)[0][0]))
        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(FootballPage))
        back.place(x=0, y=725, width=80, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class AustralianFootballPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/football.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Australian Football", bg="red", font=TITLE_FONT)
        label.place(x=600, y=50, width=200, height=44)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Total wins\nas underdog", bg="red",
                            command=lambda: controller.show_frame(AustralianFootballOpt1Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(FootballPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=620, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class AustralianFootballOpt1Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/football.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Australian Football", bg="red", font=TITLE_FONT)
        label.place(x=600, y=50, width=200, height=44)

        image = plt.imread('football/charts/underdog.png')
        fig = plt.figure(figsize=(8, 7))
        im = plt.imshow(image)
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.NONE, expand=False)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(FootballPage))
        back.place(x=0, y=725, width=80, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class HockeyPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/hockey.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Hockey", bg="orange red", font=TITLE_FONT)
        label.place(x=620, y=50, width=100, height=44)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Most Predictable", bg="orange red",
                            command=lambda: controller.show_frame(HockeyOpt1Page))
        option2 = tk.Button(self, text="Most Unpredictable", bg="orange red",
                            command=lambda: controller.show_frame(HockeyOpt2Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=590, y=725, width=120, height=44)
        option2.place(x=710, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class HockeyOpt1Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/hockey.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Hockey", bg="orange red", font=TITLE_FONT)
        label.place(x=620, y=50, width=100, height=44)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Most Predictable", bg="orange red",
                            command=lambda: controller.show_frame(HockeyOpt1Page))
        option2 = tk.Button(self, text="Most Unpredictable", bg="orange red",
                            command=lambda: controller.show_frame(HockeyOpt2Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=590, y=725, width=120, height=44)
        option2.place(x=710, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class HockeyOpt2Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/hockey.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Hockey", bg="orange red", font=TITLE_FONT)
        label.place(x=620, y=50, width=100, height=44)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Most Predictable", bg="orange red",
                            command=lambda: controller.show_frame(HockeyOpt1Page))
        option2 = tk.Button(self, text="Most Unpredictable", bg="orange red",
                            command=lambda: controller.show_frame(HockeyOpt2Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=590, y=725, width=120, height=44)
        option2.place(x=710, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class TennisPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/tennis.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Tennis", bg="goldenrod1", font=TITLE_FONT)
        label.place(x=620, y=50, width=100, height=44)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Participation of\nFederer", bg="goldenrod1",
                            command=lambda: controller.show_frame(TennisOpt1Page))
        option2 = tk.Button(self, text="Participation of\nSerena", bg="goldenrod1",
                            command=lambda: controller.show_frame(TennisOpt2Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=590, y=725, width=120, height=44)
        option2.place(x=710, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class TennisOpt1Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/tennis.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Tennis", bg="goldenrod1", font=TITLE_FONT)
        label.place(x=620, y=50, width=100, height=44)

        image = plt.imread('tennis/charts/federer.png')
        fig = plt.figure(figsize=(8, 7))
        im = plt.imshow(image)
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.NONE, expand=False)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Participation of\nFederer", bg="goldenrod1",
                            command=lambda: controller.show_frame(TennisOpt1Page))
        option2 = tk.Button(self, text="Participation of\nSerena", bg="goldenrod1",
                            command=lambda: controller.show_frame(TennisOpt2Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=590, y=725, width=120, height=44)
        option2.place(x=710, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class TennisOpt2Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/tennis.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Tennis", bg="goldenrod1", font=TITLE_FONT)
        label.place(x=620, y=50, width=100, height=44)

        image = plt.imread('tennis/charts/serena.png')
        fig = plt.figure(figsize=(8, 7))
        im = plt.imshow(image)
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.NONE, expand=False)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Participation of\nFederer", bg="goldenrod1",
                            command=lambda: controller.show_frame(TennisOpt1Page))
        option2 = tk.Button(self, text="Participation of\nSerena", bg="goldenrod1",
                            command=lambda: controller.show_frame(TennisOpt2Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=590, y=725, width=120, height=44)
        option2.place(x=710, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class RugbyPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/rugby.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Rugby", bg="purple4", font=TITLE_FONT)
        label.place(x=620, y=50, width=100, height=44)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Most Predictable", bg="purple4",
                            command=lambda: controller.show_frame(RugbyOpt1Page))
        option2 = tk.Button(self, text="Most Unpredictable", bg="purple4",
                            command=lambda: controller.show_frame(RugbyOpt2Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=590, y=725, width=120, height=44)
        option2.place(x=710, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class RugbyOpt1Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/rugby.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Rugby", bg="purple4", font=TITLE_FONT)
        label.place(x=620, y=50, width=100, height=44)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Most Predictable", bg="purple4",
                            command=lambda: controller.show_frame(RugbyOpt1Page))
        option2 = tk.Button(self, text="Most Unpredictable", bg="purple4",
                            command=lambda: controller.show_frame(RugbyOpt2Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=590, y=725, width=120, height=44)
        option2.place(x=710, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class RugbyOpt2Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/rugby.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Rugby", bg="purple4", font=TITLE_FONT)
        label.place(x=620, y=50, width=100, height=44)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Most Predictable", bg="purple4",
                            command=lambda: controller.show_frame(RugbyOpt1Page))
        option2 = tk.Button(self, text="Most Unpredictable", bg="purple4",
                            command=lambda: controller.show_frame(RugbyOpt2Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=590, y=725, width=120, height=44)
        option2.place(x=710, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class CricketPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/cricket.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Cricket", bg="blue", font=TITLE_FONT)
        label.place(x=620, y=50, width=100, height=44)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Most Predictable", bg="blue",
                            command=lambda: controller.show_frame(CricketOpt1Page))
        option2 = tk.Button(self, text="Most Unpredictable", bg="blue",
                            command=lambda: controller.show_frame(CricketOpt2Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=590, y=725, width=120, height=44)
        option2.place(x=710, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class CricketOpt1Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/cricket.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Cricket", bg="blue", font=TITLE_FONT)
        label.place(x=620, y=50, width=100, height=44)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Most Predictable", bg="blue",
                            command=lambda: controller.show_frame(CricketOpt1Page))
        option2 = tk.Button(self, text="Most Unpredictable", bg="blue",
                            command=lambda: controller.show_frame(CricketOpt2Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=590, y=725, width=120, height=44)
        option2.place(x=710, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


class CricketOpt2Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file=r"backgrounds/cricket.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, width=1571, height=839)
        label = tk.Label(self, text="Cricket", bg="blue", font=TITLE_FONT)
        label.place(x=620, y=50, width=100, height=44)

        exit_btn = tk.Button(self, text="Exit", command=self.quit)
        option1 = tk.Button(self, text="Most Predictable", bg="blue",
                            command=lambda: controller.show_frame(CricketOpt1Page))
        option2 = tk.Button(self, text="Most Unpredictable", bg="blue",
                            command=lambda: controller.show_frame(CricketOpt2Page))
        back = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        back.place(x=0, y=725, width=80, height=44)
        option1.place(x=590, y=725, width=120, height=44)
        option2.place(x=710, y=725, width=120, height=44)
        exit_btn.place(x=1288, y=725, width=80, height=44)


def make_query(sql):
    # Connect to the database
    connection = pymysql.connect(host="localhost", user="root", db="project", charset='utf8')
    try:
        with connection.cursor() as cursor:
            # Read a single record
            cursor.execute(sql)
            result = cursor.fetchall()
            # print(result)
    finally:
        connection.close()
    return result


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
