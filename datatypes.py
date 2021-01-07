from dataclasses import dataclass


@dataclass
class StudentData:
    id: int
    name: str
    sex: str
    age: int
    qq: int
    phone: int
    major: str


@dataclass
class UIConfig:
    title: str
    height: int
    width: int
