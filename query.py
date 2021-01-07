import sqlite3

from datatypes import StudentData


class StudentQuery:
    def __init__(self, database_file_name: str):
        self.database_file_name = database_file_name
        self.connect_database()

    def __del__(self):
        self.close_database()

    def connect_database(self) -> None:
        self.__conn = sqlite3.connect(self.database_file_name)
        self.__conn.execute("""
            CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY AUTOINCREMENT ,
                name VARCHAR(255),
                age INTEGER,
                sex VARCHAR(1),
                qq INTEGER,
                phone INTEGER,
                major VARCHAR(255)
            );
        """)
        self.__conn.execute("CREATE INDEX IF NOT EXISTS student_id_index ON students(id);")

    def close_database(self) -> None:
        self.__conn.close()

    def update_student(self, student: StudentData) -> None:
        if student.id == 0:
            self.__conn.execute("INSERT INTO students(name,age,sex,qq,phone,major) VALUES (?,?,?,?,?,?)", (
                student.name,
                student.age,
                student.sex,
                student.qq,
                student.phone,
                student.major
            ))
        else:
            self.__conn.execute("UPDATE students SET name=?,age=?,sex=?,qq=?,phone=?,major=? WHERE id=?", (
                student.name,
                student.age,
                student.sex,
                student.qq,
                student.phone,
                student.major,
                student.id
            ))
        self.__conn.commit()

    def delete_student_by_id(self, student_id: int) -> None:
        self.__conn.execute("DELETE FROM students WHERE id=?", (student_id,))
        self.__conn.commit()

    def find_student_by_id(self, student_id) -> StudentData:
        result = self.__conn.execute(
            "SELECT name,age,sex,qq,phone,major FROM students WHERE id=?", (student_id,)).fetchone()
        return StudentData(
            id=student_id,
            name=result[0],
            age=result[1],
            sex=result[2],
            qq=result[3],
            phone=result[4],
            major=result[5]
        )

    def find_all_students(self) -> [StudentData]:
        result = self.__conn.execute("SELECT id,name,age,sex,qq,phone,major FROM students").fetchall()
        return list(map(lambda item: StudentData(
            id=item[0],
            name=item[1],
            age=item[2],
            sex=item[3],
            qq=item[4],
            phone=item[5],
            major=item[6]
        ), result))

    def execute(self, sql, parameters) -> sqlite3.Cursor:
        return self.__conn.execute(sql, parameters)
