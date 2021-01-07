from query import StudentQuery
from ui import UI
from datatypes import StudentData


class Application:
    def __init__(self):
        self.query = StudentQuery("data.db")
        self.ui = UI()
        self.ui.bind_remove_button(self.__delete_student)
        self.ui.bind_submit_button(self.__update_student)
        self.ui.bind_table_selection(lambda student_id: self.query.find_student_by_id(student_id))

    def __del__(self):
        del self.query
        del self.ui

    def __delete_student(self, student_id):
        self.query.delete_student_by_id(student_id)
        self.__update_table()

    def __update_student(self, student: StudentData):
        self.query.update_student(student)
        self.__update_table()

    def __update_table(self):
        students = self.query.find_all_students()
        self.ui.update_table(students)

    def start(self):
        self.__update_table()
        self.ui.loop()


if __name__ == "__main__":
    app = Application()
    app.start()
    del app
