import tkinter as tk
from tkinter import *
from tkinter import ttk

def end_screen(root):
    screen = tk.Frame(root)
    label = tk.Label(screen, text="設定が保存されました。")
    label.grid(row=0,column=0,sticky=tk.NW)
    label = tk.Label(screen, text="画面を閉じてください")
    label.grid(row=1,column=0,sticky=tk.NW)
    screen.grid(row=0,column=0)