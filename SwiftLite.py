import customtkinter as CTK
import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
import io
import sys
import threading
import queue
import pywinstyles

root = CTK.CTk()
root.title('SwiftLite')
root.geometry('1090x650')
root.resizable(False, False)
root.iconbitmap('AppIcon.ico')#if the program doesn't Work, Download the Icon, or just delete this line

font1 = ('Helvetica', 25)
font2 = ('Helvetica', 20)
font3 =  ('Helvetica', 17)
font_size = 20
font_family = "Helvetica"


def open_file():
    filepath = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("Python files", "*.py")])
    if filepath:
        with open(filepath, 'r') as file:
            content = file.read()
        mainentry.delete(1.0, tk.END)
        mainentry.insert(tk.END, content)


def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Text files", "*.txt"), ("Python files", "*.py")])
    if filepath:
        with open(filepath, 'w') as file:
            file.write(mainentry.get(1.0, tk.END))

def undo_action():
    try:
        mainentry.edit_undo()
    except tk.TclError:
        pass  # Prevents errors if there is nothing to undo

def redo_action():
    try:
        mainentry.edit_redo()
    except tk.TclError:
        pass

def themecolor():
    color_code = colorchooser.askcolor(title ="Choose color")[1]
    print(color_code)
    if color_code:
        filemain.configure(fg_color=color_code, hover_color='gray17')
        undomain.configure(fg_color=color_code, hover_color='gray17')
        redomain.configure(fg_color=color_code, hover_color='gray17')
        savemain.configure(fg_color=color_code, hover_color='gray17')
        customisereset.configure(fg_color=color_code)
        customiseacrylic.configure(fg_color=color_code, hover_color='gray17')
        customiselightmode.configure(fg_color=color_code, hover_color='gray17')
        customisedarkmode.configure(fg_color=color_code, hover_color='gray17')
        customisethemecolor.configure(fg_color=color_code, hover_color='gray17')
        customizeThememain.configure(fg_color=color_code, hover_color='gray17')
        moremain.configure(fg_color=color_code, hover_color='gray17')
        moreback.configure(fg_color=color_code)
        customnonacrylicmode.configure(fg_color=color_code, hover_color='gray17')
        increasemain.configure(fg_color=color_code, hover_color='gray17')
        decreasemain.configure(fg_color=color_code, hover_color='gray17')
        resetbookmode.configure(fg_color=color_code, hover_color='gray17')

def resetthemecolor():
        filemain.configure(fg_color='#474092', hover_color='#2e2961')
        undomain.configure(fg_color='#474092', hover_color='#2e2961')
        redomain.configure(fg_color='#474092', hover_color='#2e2961')
        savemain.configure(fg_color='#474092', hover_color='#2e2961')
        customisereset.configure(fg_color='#474092')
        customiseacrylic.configure(fg_color='#474092', hover_color='#2e2961')
        customiselightmode.configure(fg_color='#474092', hover_color='#2e2961')
        customisedarkmode.configure(fg_color='#474092', hover_color='#2e2961')
        customisethemecolor.configure(fg_color='#474092', hover_color='#2e2961')
        customizeThememain.configure(fg_color='#474092', hover_color='#2e2961')
        moremain.configure(fg_color='#474092', hover_color='#2e2961')
        moreback.configure(fg_color='#474092')
        customnonacrylicmode.configure(fg_color='#474092', hover_color='#2e2961')
        increasemain.configure(fg_color='#474092', hover_color='#2e2961')
        decreasemain.configure(fg_color='#474092', hover_color='#2e2961')
        resetbookmode.configure(fg_color='#474092', hover_color='#2e2961')

        

def more():
    extraframe.place(x=300, y=150)

def bringcustomise():
    pass

def customise():
    customisereset.place(x=10, y=230)
    customiseacrylic.place(x=10, y=160)
    customiselightmode.place(x=10, y=90)
    customisedarkmode.place(x=10, y=55)
    customisethemecolor.place(x=10, y=20)
    customnonacrylicmode.place(x=10, y=195)
    resetbookmode.place(x=10,y=125)
    
    

def acrylic():
    pywinstyles.apply_style(root, 'transparent')
    topbar.configure(border_width=1, border_color='white')
    sidebar.configure(border_width=1, border_color='white')
    mainentry.configure(border_width=1, border_color='white')
    customnonacrylicmode.configure(state='enabled', hover_color='#2e2961')

def lightmode():
    mainentry.configure(fg_color='#fffcbb', border_width=2, border_color='gray1', text_color="gray1")
    resetbookmode.configure(state='enabled')

def disablebookmode():
    mainentry.configure(fg_color='gray12', border_width=2, border_color='gray1', text_color="gray100")
    resetbookmode.configure(state='disabled')


def reset():
    pywinstyles.apply_style(root, "normal")
    CTK.set_appearance_mode("Dark")
    topbar.configure(fg_color='gray10', bg_color='gray11', border_width=2, border_color='gray1')
    sidebar.configure(fg_color='gray20', bg_color='gray1', border_width=2, border_color='gray1')
    mainentry.configure(fg_color='gray10', bg_color='gray1', border_width=2, border_color='gray1')
    customnonacrylicmode.configure(state='disabled')
    mainentry.configure(fg_color='gray12', border_width=2, border_color='gray1', text_color="gray100")
    filemain.configure(fg_color='#474092', hover_color='#2e2961')
    undomain.configure(fg_color='#474092', hover_color='#2e2961')
    redomain.configure(fg_color='#474092', hover_color='#2e2961')
    savemain.configure(fg_color='#474092', hover_color='#2e2961')
    customisereset.configure(fg_color='#474092')
    customiseacrylic.configure(fg_color='#474092', hover_color='#2e2961')
    customiselightmode.configure(fg_color='#474092', hover_color='#2e2961')
    customisedarkmode.configure(fg_color='#474092', hover_color='#2e2961')
    customisethemecolor.configure(fg_color='#474092', hover_color='#2e2961')
    customizeThememain.configure(fg_color='#474092', hover_color='#2e2961')
    moremain.configure(fg_color='#474092', hover_color='#2e2961')
    moreback.configure(fg_color='#474092')
    customnonacrylicmode.configure(fg_color='#474092', hover_color='#2e2961')
    increasemain.configure(fg_color='#474092', hover_color='#2e2961')
    decreasemain.configure(fg_color='#474092', hover_color='#2e2961')
    resetbookmode.configure(fg_color='#474092', hover_color='#2e2961')
    

def back():
    extraframe.place(x=1, y=1400)

def resetacrylic():
    pywinstyles.apply_style(root, "normal")
    CTK.set_appearance_mode("Dark")
    topbar.configure(fg_color='gray10', bg_color='gray11', border_width=2, border_color='gray1')
    sidebar.configure(fg_color='gray20', bg_color='gray1', border_width=2, border_color='gray1')
    mainentry.configure(fg_color='gray10', bg_color='gray1', border_width=2, border_color='gray1')
    customnonacrylicmode.configure(state='disabled')

def increasefont():
    global font_size
    font_size += 2  # Increase font size
    mainentry.configure(font=(font_family, font_size))

def decreasefont():
    global font_size
    font_size -= 2  # Increase font size
    mainentry.configure(font=(font_family, font_size))



mainentry = CTK.CTkTextbox(root, height=595, width=1040, border_width=2, border_color='gray1',wrap="word", undo=True, font=(font_family, font_size))
mainentry.place(x=40, y=50)
mainentry.bind("<Control-z>", lambda event: undo_action())
mainentry.bind("<Control-y>", lambda event: redo_action())

topbar = CTK.CTkFrame(root, height=40, width=1075, fg_color='gray10', border_width=2, border_color='gray1')
topbar.place(x=4, y=4)

sidebar = CTK.CTkFrame(root, height=595, width=30, fg_color='gray20', border_width=2, border_color='gray1')
sidebar.place(x=4, y=50)




extraframe = CTK.CTkFrame(root, height=300, width=500, fg_color='gray20', border_width=2, border_color='gray1', bg_color='gray10')
extraframe.place(x=1, y=1400)

customiseframe2 = CTK.CTkFrame(extraframe, height=270, width=220, fg_color='gray10', border_width=2, border_color='gray1', bg_color='gray20')
customiseframe2.place(x=260, y=14)




customizeThememain = CTK.CTkButton(extraframe, fg_color="#474092", bg_color='gray20', hover_color="#2e2961", text='Customize', height=25, width=240, font=font3, command=customise, border_width=2, border_color='gray1')
customizeThememain.place(x=10, y=30)

customiseacrylic = CTK.CTkButton(customiseframe2, fg_color="#474092", bg_color='gray10', hover_color="#2e2961", text='AcrylicMode', height=25, width=200, font=font3, command=acrylic, border_width=2, border_color='gray1')
customiseacrylic.place(x=10, y=900)

customiselightmode = CTK.CTkButton(customiseframe2, fg_color="#474092", bg_color='gray10', hover_color="#2e2961", text='BookMode', height=25, width=200, font=font3, command=lightmode, border_width=2, border_color='gray1')
customiselightmode.place(x=10, y=900)

customisedarkmode = CTK.CTkButton(customiseframe2, fg_color="#474092", bg_color='gray10', hover_color="#2e2961", text='ResetThemeColor', height=25, width=200, font=font3, border_width=2, border_color='gray1', command=resetthemecolor)
customisedarkmode.place(x=10, y=900)

customisethemecolor = CTK.CTkButton(customiseframe2, fg_color="#474092", bg_color='gray10', hover_color="#2e2961", text='SetThemeColor', height=25, width=200, font=font3, command=themecolor, border_width=2, border_color='gray1')
customisethemecolor.place(x=10, y=900)

customisereset = CTK.CTkButton(customiseframe2, fg_color="#474092", bg_color='gray10', hover_color="red", text='Reset', height=25, width=200, font=font3, command=reset, border_width=2, border_color='gray1')
customisereset.place(x=10, y=900)

customnonacrylicmode = CTK.CTkButton(customiseframe2, fg_color="#474092", bg_color='gray10', hover_color="#2e2961", text='DisableAcrylic', height=25, width=200, font=font3, command=resetacrylic, border_width=2, border_color='gray1')
customnonacrylicmode.place(x=10, y=900)
customnonacrylicmode.configure(state='disabled')

resetbookmode = CTK.CTkButton(customiseframe2, fg_color="#474092", bg_color='gray10', hover_color="#2e2961", text='DisableBookMode', height=25, width=200, command=disablebookmode, font=font3, border_width=2, border_color='gray1')
resetbookmode.place(x=10, y=900)
resetbookmode.configure(state='disabled')


increasemain = CTK.CTkButton(sidebar, fg_color="#474092", bg_color='gray20', hover_color="#2e2961", text='+', height=25, width=20, command=increasefont, font=font3)
increasemain.place(x=2, y=6)

decreasemain = CTK.CTkButton(sidebar, fg_color="#474092", bg_color='gray20', hover_color="#2e2961", text='-', height=27, width=24, command=decreasefont, font=font3)
decreasemain.place(x=2, y=35)




filemain = CTK.CTkButton(topbar, fg_color="#474092", bg_color='gray10', hover_color="#2e2961", text='File', height=25, width=20, command=open_file)
filemain.place(x=10, y=9)

undomain = CTK.CTkButton(topbar, fg_color="#474092", bg_color='gray10', hover_color="#2e2961", text='Undo', height=25, width=20, command=undo_action)
undomain.place(x=50, y=9)

redomain = CTK.CTkButton(topbar, fg_color="#474092", bg_color='gray10', hover_color="#2e2961", text='Redo', height=25, width=20, command=redo_action)
redomain.place(x=100, y=9)

savemain = CTK.CTkButton(topbar, fg_color="#474092", bg_color='gray10', hover_color="#2e2961", text='Save', height=25, width=20, command=save_file)
savemain.place(x=150, y=9)

moremain = CTK.CTkButton(topbar, fg_color="#474092", bg_color='gray10', hover_color="#2e2961", text='...', height=20, width=10, font=font3, command=more)
moremain.place(x=1040, y=9)

moreback = CTK.CTkButton(extraframe, fg_color="#474092", bg_color='gray20', hover_color="red", text='Back', height=25, width=240, font=font3, command=back, border_width=2, border_color='gray1')
moreback.place(x=10, y=60)

aboutframe = CTK.CTkFrame(extraframe, bg_color='gray20', fg_color='gray10', border_width=2, border_color='gray1', width=220, height=145).place(x=20, y=140)
about = CTK.CTkLabel(extraframe, text='©Harshu Jiwane', font=font3, bg_color='gray10').place(x=64, y=150)
about2 = CTK.CTkLabel(extraframe, text='AKA', font=font3, bg_color='gray10').place(x=110, y=170)
about3 = CTK.CTkLabel(extraframe, text='Ridan Jiwane', font=font3, bg_color='gray10').place(x=75, y=190)
about4 = about = CTK.CTkLabel(extraframe, text='For Quieres:', font=font3, bg_color='gray10').place(x=80, y=230)
about5 = about = CTK.CTkLabel(extraframe, text='harshugotu12@gmail.com', font=font3, bg_color='gray10').place(x=35, y=250)










root.mainloop()
