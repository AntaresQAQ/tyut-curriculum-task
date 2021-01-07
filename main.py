from query import StudentQuery
from ui import UI
from datatypes import UIConfig


class Application:
    def __init__(self):
        self.query = StudentQuery("data.db")
        self.UI = UI()


if __name__ == "__main__":
    Application()
