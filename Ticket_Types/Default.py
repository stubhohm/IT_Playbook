from Ticket import Ticket
# Default Ticket type
class Default(Ticket):
    def __init__(self) -> None:
        self.requested_info = {'Caller': '', 'Company': '', 'Issue': '', 'CallBack Number (extension)': ''}
        self.optional_info = {'None': ''}
        super().__init__()
    