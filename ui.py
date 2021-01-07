from tkinter import Tk, Entry, Label, ttk, Button, Scrollbar

from datatypes import UIConfig


class UI:
    def __init__(self):
        self.__window = Tk()
        self.configures = UIConfig(title="学生信息管理系统", width=500, height=600)
        self.__load_config()
        self.__create_entrys()
        self.__create_buttons()
        self.__create_table()
        self.__window.mainloop()

    def __load_config(self) -> None:
        self.__window["width"] = self.configures.width
        self.__window["height"] = self.configures.height
        self.__window.title(self.configures.title)
        self.__window.resizable(0, 0)

    def __create_entrys(self) -> None:
        Label(self.__window, text="姓名", width=5).place(x=10, y=10)
        self.__name_entry = Entry(self.__window, width=20).place(x=60, y=10)
        Label(self.__window, text="性别", width=5).place(x=10, y=40)
        self.__sex_entry = Entry(self.__window, width=20).place(x=60, y=40)
        Label(self.__window, text="年龄", width=5).place(x=10, y=70)
        self.__age_entry = Entry(self.__window, width=20).place(x=60, y=70)

        Label(self.__window, text="专业", width=5).place(x=250, y=10)
        self.__major_entry = Entry(self.__window, width=20).place(x=300, y=10)
        Label(self.__window, text="电话", width=5).place(x=250, y=40)
        self.__phone_entry = Entry(self.__window, width=20).place(x=300, y=40)
        Label(self.__window, text="QQ", width=5).place(x=250, y=70)
        self.__qq_entry = Entry(self.__window, width=20).place(x=300, y=70)

    def __create_buttons(self) -> None:
        self.__submit_button = Button(self.__window, text="提交", width=5).place(x=50, y=120)
        self.__clear_button = Button(self.__window, text="清空", width=5).place(x=200, y=120)
        self.__remove_button = Button(self.__window, text="删除", width=5).place(x=350, y=120)

    def __create_table(self) -> None:
        self.__student_list = ttk.Treeview(self.__window)
        self.__student_list['show'] = 'headings'
        self.__student_list["columns"] = ("id", "name", "age", "sex", "major", "phone", "qq")
        self.__student_list["displaycolumns"] = ("name", "age", "sex", "major", "phone", "qq")
        self.__student_list.column("name", width=85)
        self.__student_list.column("age", width=40)
        self.__student_list.column("sex", width=40)
        self.__student_list.column("major", width=90)
        self.__student_list.column("phone", width=110)
        self.__student_list.column("qq", width=110)
        self.__student_list.heading("name", text="姓名")
        self.__student_list.heading("age", text="年龄")
        self.__student_list.heading("sex", text="性别")
        self.__student_list.heading("major", text="专业")
        self.__student_list.heading("phone", text="电话")
        self.__student_list.heading("qq", text="QQ")
        self.__student_list.place(x=10, y=180, height=400)

        table_croll = Scrollbar(self.__window, orient='vertical', command=self.__student_list.yview)
        table_croll.place(x=475, y=180, width=15, height=400)
        self.__student_list.configure(yscrollcommand=table_croll)
