from dataclasses import dataclass
from enum import Enum


@dataclass
class StudentSex(Enum):
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"


@dataclass
class StudentData:
    id: int
    name: str
    sex: StudentSex
    age: int
    qq: int
    phone: int
    major: str


@dataclass
class UIConfig:
    title: str
    height: int
    width: int
