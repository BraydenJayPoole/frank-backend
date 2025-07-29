# References: 4.2. Database Schema (ERD)
import enum
from sqlalchemy import Column, Integer, String, Boolean, Enum
from sqlalchemy.orm import relationship

from app.database import Base
from app.core.security import get_password_hash

class AccountType(str, enum.Enum):
    ASSET = "ASSET"
    LIABILITY = "LIABILITY"
    EQUITY = "EQUITY"
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    currency = Column(String, nullable=False, default="AUD")
    hashed_password = Column(String, nullable=False)

    def set_password(self, password: str):
        """Sets the user's password, storing it as a secure hash."""
        self.hashed_password = get_password_hash(password)


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    type = Column(Enum(AccountType), nullable=False)
    description = Column(String, nullable=True)
    is_bank_account = Column(Boolean, default=False)

    # Relationships (will be defined in other models)
    # transactions = relationship("Transaction", back_populates="account")
