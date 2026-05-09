"""Tkinter War Simulator GUI: army type selection, size entry, player list, and start-war button."""
import tkinter

main_window = tkinter.Tk()
main_window.geometry('500x425+375+15')
main_window.configure(bg='grey69')

for i in range(0, 9):
    main_window.rowconfigure(i, weight=1)
    if i <= 5:
        main_window.columnconfigure(i, weight=1)

top_title = tkinter.LabelFrame(main_window)
top_title.grid(row=0, column=0, columnspan=7, sticky='news')

for i in range(0, 3):
    top_title.columnconfigure(i, weight=1)

title = tkinter.Label(top_title, text="War Simulator")
title.grid(column=1)

army_frame = tkinter.Frame(main_window)
army_frame.grid(column=0, row=1, columnspan=2, rowspan=5, sticky='news')

for i in range(0, 6):
    army_frame.rowconfigure(i, weight=1)

army_title = tkinter.Label(army_frame, text='Select Which Armies to Build')
army_title.grid(row=0)

ninja_button = tkinter.Radiobutton(army_frame, text="Ninja")
ninja_button.grid(row=1, sticky='W')

knight_button = tkinter.Radiobutton(army_frame, text="Knight")
knight_button.grid(row=2, sticky='W')

ork_button = tkinter.Radiobutton(army_frame, text="Ork")
ork_button.grid(row=3, sticky='W')

wizard_button = tkinter.Radiobutton(army_frame, text="Wizard")
wizard_button.grid(row=4, sticky='W')

werewolf_button = tkinter.Radiobutton(army_frame, text='Werewolf')
werewolf_button.grid(row=5, sticky='W')

number_frame = tkinter.Frame(main_window)
number_frame.grid(column=0, row=6, columnspan=2, rowspan=2, sticky='nwes')

for i in range(0, 2):
    number_frame.rowconfigure(i, weight=1)

number_label = tkinter.Label(number_frame, text='Army Size')
number_label.grid(row=0, sticky='new')

entry_box = tkinter.Entry(number_frame)
entry_box.grid(row=1, sticky='nsew')

generate_button = tkinter.Button(main_window, text="Generate Army")
generate_button.grid(row=8, column=0, columnspan=2, sticky='news')

player_canvas = tkinter.Canvas(main_window)
player_canvas.grid(row=1, column=2, rowspan=7, columnspan=4, sticky='news')

player_canvas.rowconfigure(0, weight=1)
player_canvas.rowconfigure(1, weight=35)

player_label = tkinter.Label(player_canvas, text="Players")
player_label.grid(row=0, sticky='ews')

player_scroll = tkinter.Scrollbar(main_window)
player_scroll.grid(row=1, column=6, rowspan=7, sticky='nws')

war_button = tkinter.Button(main_window, text="Start War")
war_button.grid(row=8, column=2, columnspan=5, sticky='news')


if __name__ == '__main__':
    main_window.mainloop()
