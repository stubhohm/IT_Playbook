class MainWindow ():
    def __init__(self, display, session, messagebox):
        self.display = display
        self.session = session
        self.messagebox = messagebox
        self.init_display()
        self.init_confirm_close()

    def center_window(self, window, scale_x, scale_y):
        window.update_idletasks()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        window_width = int(screen_width * scale_x)
        window_height = int(screen_height * scale_y)
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 4
        window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def init_display(self, name = 'IT Playbook', scale_x = 0.4, scale_y = 0.6, centered = True):
        if centered:
            self.center_window(self.display, scale_x, scale_y)
        self.display.title(f'{name}')

    def init_confirm_close(self):
        self.display.protocol('WM_DELETE_WINDOW', lambda: self.close_window())
    
    def close_window(self):
        print('quit prompted')
        if self.messagebox.askokcancel('Close Play Book', 'Are you sure you want to quit?'):
            self.session = False
            self.display.destroy()

    def update(self):
        self.display.update()