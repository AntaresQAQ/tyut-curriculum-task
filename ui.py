from tkinter import Tk, Entry, Label, ttk, Button, Scrollbar, EventType, messagebox
from typing import Callable
from datatypes import UIConfig, StudentData


class UI:
    def __init__(self):
        self.__window: Tk = Tk()
        self.configures = UIConfig(title="学生信息管理系统", width=500, height=600)
        self.__now_student_id = 0
        self.__load_config()
        self.__create_entrys()
        self.__create__selections()
        self.__create_buttons()
        self.__create_table()

    def __load_config(self) -> None:
        self.__window["width"] = self.configures.width
        self.__window["height"] = self.configures.height
        self.__window.title(self.configures.title)
        self.__window.resizable(0, 0)

    def __create_entrys(self) -> None:
        self.__name_entry: Entry = Entry(self.__window)
        self.__age_entry: Entry = Entry(self.__window)
        self.__major_entry: Entry = Entry(self.__window)
        self.__phone_entry: Entry = Entry(self.__window)
        self.__qq_entry: Entry = Entry(self.__window)

        Label(self.__window, text="姓名").place(x=10, y=10, width=50)
        self.__name_entry.place(x=60, y=10, width=180)
        # Sex is a ComboBox
        Label(self.__window, text="年龄").place(x=10, y=70, width=50)
        self.__age_entry.place(x=60, y=70, width=180)

        Label(self.__window, text="专业").place(x=260, y=10, width=50)
        self.__major_entry.place(x=310, y=10, width=180)
        Label(self.__window, text="电话").place(x=260, y=40, width=50)
        self.__phone_entry.place(x=310, y=40, width=180)
        Label(self.__window, text="QQ").place(x=260, y=70, width=50)
        self.__qq_entry.place(x=310, y=70, width=180)

    def __create__selections(self):
        Label(self.__window, text="性别").place(x=10, y=40, width=50)
        self.__sex_selections: ttk.Combobox = ttk.Combobox(self.__window)
        self.__sex_selections["values"] = ("男", "女", "其他")
        self.__sex_selections["state"] = "readonly"
        self.__sex_selections.current(0)
        self.__sex_selections.place(x=60, y=40, width=180)

    def __create_buttons(self) -> None:
        self.__submit_button: Button = Button(self.__window, text="提交", width=5)
        self.__submit_button.place(x=50, y=120)
        self.__clear_button: Button = Button(self.__window, text="清空", width=5)
        self.__clear_button.bind("<Button-1>", self.__clear_all)
        self.__clear_button.place(x=200, y=120)
        self.__remove_button: Button = Button(self.__window, text="删除", width=5)
        self.__remove_button.place(x=350, y=120)

    def __create_table(self) -> None:
        self.__student_list_table: ttk.Treeview = ttk.Treeview(self.__window)
        self.__student_list_table['show'] = 'headings'
        self.__student_list_table["columns"] = ("id", "name", "age", "sex", "major", "phone", "qq")
        self.__student_list_table["displaycolumns"] = ("name", "age", "sex", "major", "phone", "qq")
        self.__student_list_table.column("name", width=85)
        self.__student_list_table.column("age", width=40)
        self.__student_list_table.column("sex", width=40)
        self.__student_list_table.column("major", width=90)
        self.__student_list_table.column("phone", width=110)
        self.__student_list_table.column("qq", width=110)
        self.__student_list_table.heading("name", text="姓名")
        self.__student_list_table.heading("age", text="年龄")
        self.__student_list_table.heading("sex", text="性别")
        self.__student_list_table.heading("major", text="专业")
        self.__student_list_table.heading("phone", text="电话")
        self.__student_list_table.heading("qq", text="QQ")
        self.__student_list_table.place(x=10, y=180, height=400)

        table_scroll = Scrollbar(self.__window,
                                 orient='vertical',
                                 command=self.__student_list_table.yview)
        table_scroll.place(x=475, y=180, width=15, height=400)
        self.__student_list_table.configure(yscrollcommand=table_scroll.set)

    def __clear_all(self, event: EventType.ButtonPress = None):
        self.__now_student_id = 0
        self.__sex_selections.current(0)
        self.__name_entry.delete(0, "end")
        self.__age_entry.delete(0, "end")
        self.__phone_entry.delete(0, "end")
        self.__major_entry.delete(0, "end")
        self.__qq_entry.delete(0, "end")
        self.__student_list_table.selection_remove(self.__student_list_table.selection())

    def __get_entrys_data(self):
        try:
            name = self.__name_entry.get()
            if len(name) == 0:
                self.show_error_msg("格式错误", "名字不能为空")
                raise ValueError("Name Can Not Be Empty")
            try:
                age = int(self.__age_entry.get())
            except ValueError as e:
                self.show_error_msg("格式错误", "年龄必须为数字")
                raise e
            raw_sex = self.__sex_selections.get()
            if raw_sex == "男":
                sex = "M"
            elif raw_sex == "女":
                sex = "F"
            else:
                sex = "O"
            major = self.__major_entry.get()
            try:
                raw_phone = self.__phone_entry.get()
                if len(raw_phone) != 11: raise ValueError("Phone Number Length Error")
                phone = int(raw_phone)
            except ValueError as e:
                self.show_error_msg("格式错误", "电话号码必须为11位数字")
                raise e
            try:
                qq = int(self.__qq_entry.get())
            except ValueError as e:
                self.show_error_msg("格式错误", "QQ号码必须为数字")
                raise e
            return StudentData(
                id=self.__now_student_id,
                name=name,
                sex=sex,
                age=age,
                major=major,
                phone=phone,
                qq=qq
            )
        except ValueError as ex:
            print(ex)
            return None

    def __update_entrys_data(self, student: StudentData):
        self.__name_entry.delete(0, "end")
        self.__age_entry.delete(0, "end")
        self.__phone_entry.delete(0, "end")
        self.__major_entry.delete(0, "end")
        self.__qq_entry.delete(0, "end")
        self.__now_student_id = student.id
        self.__name_entry.insert(0, student.name)
        self.__age_entry.insert(0, student.age)
        self.__major_entry.insert(0, student.major)
        self.__qq_entry.insert(0, student.qq)
        self.__phone_entry.insert(0, student.phone)
        if student.sex == "M":
            self.__sex_selections.current(0)
        elif student.sex == "F":
            self.__sex_selections.current(1)
        else:
            self.__sex_selections.current(2)

    def show_error_msg(self, title, msg):
        t = messagebox.showerror(title, msg)
        self.__submit_button.grab_release()
        self.__remove_button.grab_release()
        self.__clear_button.grab_release()

    def bind_remove_button(self, callback: Callable[[int], None]):
        def handle(event: EventType.ButtonPress):
            if self.__now_student_id: callback(self.__now_student_id)
            self.__clear_all()

        self.__remove_button.bind("<Button-1>", handle)

    def bind_submit_button(self, callback: Callable[[StudentData], None]):
        def handle(event: EventType.ButtonPress):
            student = self.__get_entrys_data()
            if student: callback(student)
            self.__clear_all()

        self.__submit_button.bind("<Button-1>", handle)

    def bind_table_selection(self, callback: Callable[[int], StudentData]):
        def handle(event: EventType.ButtonRelease):
            selections = self.__student_list_table.selection()
            if len(selections) == 0: return
            item = self.__student_list_table.item(selections[0], "values")
            student = callback(int(item[0]))
            self.__update_entrys_data(student)

        self.__student_list_table.bind("<ButtonRelease-1>", handle)

    def update_table(self, students: [StudentData]):
        for item in self.__student_list_table.get_children():
            self.__student_list_table.delete(item)

        for item in students:
            if item.sex == "M":
                sex = "男"
            elif item.sex == "F":
                sex = "女"
            else:
                sex = "其他"
            self.__student_list_table.insert("", "end", values=[
                item.id,
                item.name,
                item.age,
                sex,
                item.major,
                item.phone,
                item.qq
            ])

    def loop(self):
        self.__window.mainloop()
