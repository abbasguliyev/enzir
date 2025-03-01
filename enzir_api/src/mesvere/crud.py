from sqlalchemy.orm import Session
from mesvere.models import Mesvere, MesvereQeydleri
from mesvere.schemas import MesvereCreate, MesvereUpdate, MesvereOut, MesvereQeydleriCreate, MesvereQeydleriUpdate, MesvereQeydleriOut

def create_mesvere(db: Session, mesvere: MesvereCreate):
    db_mesvere = Mesvere(
        basliq = mesvere.basliq,
        tarix = mesvere.tarix
    )
    db.add(db_mesvere)
    db.commit()
    db.refresh(db_mesvere)
    return db_mesvere

def get_all_mesvere(db: Session, offset: int = 0, limit: int = 10):
    return db.query(Mesvere).offset(offset).limit(limit).all()

def get_mesvere_by_id(db: Session, mesvere_id: int):
    return db.query(Mesvere).filter(Mesvere.id==mesvere_id).first()

def update_mesvere(db: Session, mesvere: Mesvere, mesvere_update: MesvereUpdate):
    for var, value in vars(mesvere_update).items():
        if value is not None:
            setattr(mesvere, var, value)
    db.commit()
    db.refresh(mesvere)
    return mesvere

def delete_mesvere(db: Session, mesvere: Mesvere):
    db.delete(mesvere)
    db.commit()

def create_mesvere_qeydleri(db: Session, mesvere_qeydleri: MesvereQeydleriCreate):
    db_mesvere_qeydleri = MesvereQeydleri(
        basliq = mesvere_qeydleri.basliq,
        aciqlama = mesvere_qeydleri.aciqlama,
        bitibmi = mesvere_qeydleri.bitibmi,
        mesvere_id = mesvere_qeydleri.mesvere_id,
        user_id = mesvere_qeydleri.user_id
    )
    db.add(db_mesvere_qeydleri)
    db.commit()
    db.refresh(db_mesvere_qeydleri)
    return db_mesvere_qeydleri

def get_all_mesvere_qeydleri(db: Session, offset: int = 0, limit: int = 10):
    return db.query(MesvereQeydleri).offset(offset).limit(limit).all()

def get_mesvere_qeydleri_by_id(db: Session, mesvere_qeydleri_id: int):
    return db.query(MesvereQeydleri).filter(MesvereQeydleri.id == mesvere_qeydleri_id).first()

def update_mesvere_qeydleri(db: Session, mesvere_qeydleri: MesvereQeydleri, mesvere_qeydleri_update: MesvereQeydleriUpdate):
    for var, value in vars(mesvere_qeydleri_update).items():
        if value is not None:
            setattr(mesvere_qeydleri, var, value)
    db.commit()
    db.refresh(mesvere_qeydleri)
    return mesvere_qeydleri

def delete_mesvere_qeydleri(db: Session, mesvere_qeydleri: MesvereQeydleri):
    db.delete(mesvere_qeydleri)
    db.commit()