import tkinter as tk
from tkinter import Tk, ttk, messagebox, filedialog
import sqlite3
import re
import os
from Services.MainWindow import MainWindow


def main():
    main_window = MainWindow(Tk(), ttk, True, messagebox)
    while main_window.session:
        main_window.update()
    print('closing playbook')

if __name__ == '__main__':
    main()
