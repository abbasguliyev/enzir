from sqlalchemy.orm import Session
from auth.models import User, Permission, Group
from auth.schemas import UserCreate, UserUpdate, PermissionCreate, PermissionUpdate, GroupCreate, GroupUpdate

def create_user(db: Session, user: UserCreate, hashed_password: str):
    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        username=user.username,
        password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_all_users(db: Session, offset: int = 0, limit: int = 10):
    return db.query(User).offset(offset).limit(limit).all()

def update_user(db: Session, user: User, user_update: UserUpdate):
    for var, value in vars(user_update).items():
        if value is not None:
            setattr(user, var, value)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user: User):
    db.delete(user)
    db.commit()

def create_permission(db: Session, permission: PermissionCreate):
    db_permission = Permission(
        name=permission.name,
        description=permission.description
    )
    db.add(db_permission)
    db.commit()
    db.refresh(db_permission)
    return db_permission

def get_permission_by_id(db: Session, permission_id: int):
    return db.query(Permission).filter(Permission.id == permission_id).first()

def get_all_permissions(db: Session, offset: int = 0, limit: int = 10):
    return db.query(Permission).offset(offset).limit(limit).all()

def update_permission(db: Session, permission: Permission, permission_update: PermissionUpdate):
    for var, value in vars(permission_update).items():
        if value is not None:
            setattr(permission, var, value)
    db.commit()
    db.refresh(permission)
    return permission

def delete_permission(db: Session, permission: Permission):
    db.delete(permission)
    db.commit()

def create_group(db: Session, group: GroupCreate):
    db_group = Group(
        name=group.name,
        description=group.description,
        permissions=group.permissions
    )
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

def get_group_by_id(db: Session, group_id: int):
    return db.query(Group).filter(Group.id == group_id).first()

def get_all_groups(db: Session, offset: int = 0, limit: int = 10):
    return db.query(Group).offset(offset).limit(limit).all()

def update_group(db: Session, group: Group, group_update: GroupUpdate):
    for var, value in vars(group_update).items():
        if value is not None:
            setattr(group, var, value)
    db.commit()
    db.refresh(group)
    return group

def delete_group(db: Session, group: Group):
    db.delete(group)
    db.commit()