from tkinter import ttk

class MainWindow ():
    def __init__(self, display, ttk, session:bool, messagebox):
        self.display = display
        self.ttk = ttk
        self.session = session
        self.messagebox = messagebox
        self.ticket_type = None
        self.dropdown_list:list = []
        self.dropdown_dict:dict = {}
        self.init_frame:bool = False
        self.old_value = None
        self.init_display()
        self.init_confirm_close()

    def center_window(self, window, scale_x:float, scale_y:float):
        window.update_idletasks()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        window_width = int(screen_width * scale_x)
        window_height = int(screen_height * scale_y)
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 4
        window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def init_display(self, name:str = 'IT Playbook', scale_x:float = 0.4, scale_y:float = 0.6, centered:bool = True):
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

    def make_frame(self):
        frame = self.ttk.Frame(self.display)
        return frame

    def make_label(self, root, label_text: str):
        label = self.ttk.Label(root, text =f'{label_text}')
        return label
    
    def clear_dropdowns(self):
        self.dropdown_list = []
        self.dropdown_dict = {}

    def on_box_select(self, dropdown, key: str):
        value = dropdown.get()
        self.dropdown_dict[key] = value

    def make_dropdown(self, root, options: list, count: int):
        dropdown = self.ttk.Combobox(root, values=options)
        dropdown.set('Select a Ticket Type')
        key = f'Drop Down {count}'
        dropdown.bind('<<ComboboxSelected>>', lambda event, dd = dropdown, key = key: self.on_box_select(dd, key))
        self.dropdown_list.append(dropdown)
        self.dropdown_dict[key] = None
        return dropdown

    def select_ticket_type(self, reset = False):
        if reset:
            self.init_frame = True
        if self.init_frame:
            return
        top_menu_frame = self.make_frame()
        top_menu_frame.pack(fill='x', pady =(0,20))
        ticket_option_frame = self.make_frame()
        ticket_option_frame.pack(fill = 'x', side = 'top')
        label_frame = self.make_frame()
        label_frame.pack(fill = 'x', side = 'top')
        ticket_option_label = self.make_label(label_frame, 'Select Ticket Type')
        ticket_option_label.pack(side='left', padx=(20,0), pady=5)
        ticket_options = ['Default', 'Block/White List', 'Blank']
        dropdown_frame = self.make_frame()
        dropdown_frame.pack(fill = 'x', side = 'top')
        ticket_option_dropdown = self.make_dropdown(dropdown_frame, ticket_options, 0)
        ticket_option_dropdown.pack(side = 'left', padx=(20,0))
        self.init_frame = True

    def update(self):
        if self.ticket_type:
            self.ticket_type.main(self.display)
            self.init_frame = True
        else:
            self.select_ticket_type()
        for key,value in self.dropdown_dict.items():
            if self.old_value == value:
                break
            if not value:
                break
            print(f'key: {key}')
            print(f'value: {value}')
            self.old_value = value
        self.display.update()