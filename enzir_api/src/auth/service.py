from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from auth import models, schemas, crud
from passlib.context import CryptContext
from auth.security import hash_password, verify_password

def create_user(db: Session, user: schemas.UserCreate):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already registered")
    hashed_password = hash_password(user.password)
    return crud.create_user(db=db, user=user, hashed_password=hashed_password)

def get_all_users(db: Session):
    return crud.get_all_users(db)

def get_user(db: Session, user_id: int):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user

def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return crud.update_user(db=db, user=db_user, user_update=user)

def delete_user(db: Session, user_id: int):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    crud.delete_user(db=db, user=db_user)
    return {"message": "User successfully deleted"}

def create_permission(db: Session, permission: schemas.PermissionCreate):
    db_permission = crud.get_permission_by_id(db, permission_id=permission.id)
    if db_permission:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Permission already registered")
    return crud.create_permission(db=db, permission=permission)

def get_all_permissions(db: Session):
    return crud.get_all_permissions(db)

def update_permission(db: Session, permission_id: int, permission: schemas.PermissionUpdate):
    db_permission = crud.get_permission_by_id(db, permission_id=permission_id)
    if not db_permission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Permission not found")
    return crud.update_permission(db=db, permission=db_permission, permission_update=permission)

def delete_permission(db: Session, permission_id: int):
    db_permission = crud.get_permission_by_id(db, permission_id=permission_id)
    if not db_permission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Permission not found")
    crud.delete_permission(db=db, permission=db_permission)
    return {"message": "Permission successfully deleted"}

def create_group(db: Session, group: schemas.GroupCreate):
    db_group = crud.get_group_by_id(db, group_id=group.id)
    if db_group:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Group already registered")
    return crud.create_group(db=db, group=group)

def get_all_groups(db: Session):
    return crud.get_all_groups(db)

def update_group(db: Session, group_id: int, group: schemas.GroupUpdate):
    db_group = crud.get_group_by_id(db, group_id=group_id)
    if not db_group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")
    return crud.update_group(db=db, group=db_group, group_update=group)

def delete_group(db: Session, group_id: int):
    db_group = crud.get_group_by_id(db, group_id=group_id)
    if not db_group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group not found")
    crud.delete_group(db=db, group=db_group)
    return {"message": "Group successfully deleted"}