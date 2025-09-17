from sqlalchemy import Column, Integer, String, Enum as SQLEnum
from app.models.database_models import Base
import enum

class UserRole(str, enum.Enum):
    HOSPITAL = "hospital"
    REGISTRY_OFFICE = "registry_office"
    POLICE = "police"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(SQLEnum(UserRole))