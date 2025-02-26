from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

from datetime import datetime

group_permissions = Table(
    "group_permissions",
    Base.metadata,
    Column("group_id", Integer, ForeignKey("groups.id")),
    Column("permission_id", Integer, ForeignKey("permissions.id")),
)

user_permissions = Table(
    "user_permissions",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("permission_id", Integer, ForeignKey("permissions.id")),
)

user_groups = Table(
    "user_groups",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("group_id", Integer, ForeignKey("groups.id")),
)

class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    
    groups = relationship("Group", secondary=group_permissions, back_populates="permissions")
    users = relationship("User", secondary=user_permissions, back_populates="permissions")


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)

    permissions = relationship("Permission", secondary=group_permissions, back_populates="groups")
    users = relationship("User", secondary=user_groups, back_populates="groups")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)

    permissions = relationship("Permission", secondary=user_permissions, back_populates="users")
    groups = relationship("Group", secondary=user_groups, back_populates="users")