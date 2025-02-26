from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from auth import schemas, crud, service, security
from database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register", response_model=schemas.UserOut)
async def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user = service.create_user(db, user)
    return user

@router.post("/login", response_model=schemas.Token)
async def login(user_data: schemas.UserLogin, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, user_data.username)
    if not user or not security.verify_password(user_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = security.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users", response_model=list[schemas.UserOut])
async def get_users(db: Session = Depends(get_db)):
    users = service.get_all_users(db)
    return users

@router.get("/users/{user_id}", response_model=schemas.UserOut)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = service.get_user(db, user_id)
    return user

@router.put("/users/{user_id}", response_model=schemas.UserOut)
async def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    user = service.update_user(db, user_id, user)
    return user

@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return service.delete_user(db, user_id)