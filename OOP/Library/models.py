from datetime import datetime
from sqlalchemy.engine.base import Engine
from sqlalchemy import create_engine, Column, Integer, Boolean, ForeignKey, Table, Date, String
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
import sqlite3
from pydantic import EmailStr, ValidationError

DATABASE_URL = "sqlite:///./library.db"
engine: Engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    # Protected
    _name: Mapped[str] = mapped_column(...)
    _email: Mapped[EmailStr] = mapped_column(unique=True)

    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, new_email: EmailStr):
        try:
            validated_email = EmailStr.validate(new_email)
        except ValidationError as e:
            raise ValidationError(f"Invalid email format {new_email}") from e
        self._email = validated_email

    def __init__(self, name: str, email: EmailStr):
        self.name = name
        self.email = email
