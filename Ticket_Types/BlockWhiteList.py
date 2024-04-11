from Ticket import Ticket
class BlockWhiteList(Ticket):
    def __init__(self) -> None:
        super().__init__()
    

    def closing_comment(self):
        pass

    def main(self, root):
        super().main()