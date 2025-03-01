from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from mesvere import models, schemas, crud

def create_mesvere(db: Session, mesvere: schemas.MesvereCreate):
    return crud.create_mesvere(db, mesvere)

def get_all_mesvere(db: Session, offset: int = 0, limit: int = 10):
    return crud.get_all_mesvere(db, offset=offset, limit=limit)

def get_mesvere(db: Session, mesvere_id: int):
    db_mesvere = crud.get_mesvere_by_id(db, mesvere_id)
    if not db_mesvere:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mesvere not found")
    return db_mesvere

def update_mesvere(db: Session, mesvere_id: int, mesvere_update: schemas.MesvereUpdate):
    db_mesvere = crud.get_mesvere_by_id(db, mesvere_id)
    if not db_mesvere:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mesvere not found")
    return crud.update_mesvere(db, mesvere=db_mesvere, mesvere_update=mesvere_update)

def delete_mesvere(db: Session, mesvere_id: int):
    db_mesvere = crud.get_mesvere_by_id(db, mesvere_id)
    if not db_mesvere:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mesvere not found")
    crud.delete_mesvere(db, mesvere=db_mesvere)
    return {"message": "Mesvere successfully deleted"}

def create_mesvere_qeydleri(db: Session, mesvere_qeydleri: schemas.MesvereQeydleriCreate):
    return crud.create_mesvere_qeydleri(db, mesvere_qeydleri=mesvere_qeydleri)

def get_all_mesvere_qeydleri(db: Session, offset: int = 0, limit: int = 10):
    return crud.get_all_mesvere_qeydleri(db, offset=offset, limit=limit)

def get_mesvere_qeydleri(db: Session, mesvere_qeydleri_id: int):
    db_mesvere_qeydleri = crud.get_mesvere_qeydleri_by_id(db, mesvere_qeydleri_id=mesvere_qeydleri_id)
    if not db_mesvere_qeydleri:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MesvereQeydleri not found")
    return db_mesvere_qeydleri

def update_mesvere_qeydleri(db: Session, mesvere_qeydleri_id: int, mesvere_qeydleri_update: schemas.MesvereQeydleriUpdate):
    db_mesvere_qeydleri = crud.get_mesvere_qeydleri_by_id(db, mesvere_qeydleri_id=mesvere_qeydleri_id)
    if not db_mesvere_qeydleri:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MesvereQeydleri not found")
    return crud.update_mesvere_qeydleri(db, mesvere_qeydleri=db_mesvere_qeydleri, mesvere_qeydleri_update=mesvere_qeydleri_update)

def delete_mesvere_qeydleri(db: Session, mesvere_qeydleri_id: int):
    db_mesvere_qeydleri = crud.get_mesvere_qeydleri_by_id(db, mesvere_qeydleri_id=mesvere_qeydleri_id)
    if not db_mesvere_qeydleri:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MesvereQeydleri not found")
    crud.delete_mesvere_qeydleri(db, db_mesvere_qeydleri)
    return {"message": "MesvereQeydleri successfully deleted"}