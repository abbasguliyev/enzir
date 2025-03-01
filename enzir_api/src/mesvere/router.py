from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from mesvere import crud, schemas, service
from database import get_db

router = APIRouter(
    tags=["Mesvere"]
)

@router.get("/", response_model=list[schemas.MesvereOut])
async def get_all_mesvere(db: Session = Depends(get_db)):
    mesvere = service.get_all_mesvere(db)
    return mesvere

@router.get("/{mesvere_id}", response_model=schemas.MesvereOut)
async def get_mesvere(mesvere_id: int, db: Session = Depends(get_db)):
    mesvere = service.get_mesvere(db, mesvere_id=mesvere_id)
    return mesvere

@router.post("/", response_model=schemas.MesvereOut)
async def create_mesvere(mesvere: schemas.MesvereCreate, db: Session = Depends(get_db)):
    mesvere = service.create_mesvere(db, mesvere)
    return mesvere

@router.put("/{mesvere_id}", response_model=schemas.MesvereOut)
async def update_mesvere(mesvere_id: int, mesvere: schemas.MesvereUpdate, db: Session = Depends(get_db)):
    mesvere = service.update_mesvere(db, mesvere_id=mesvere_id, mesvere_update=mesvere)
    return mesvere

@router.delete("/{mesvere_id}")
async def delete_mesvere(mesvere_id: int, db: Session = Depends(get_db)):
    return service.delete_mesvere(db, mesvere_id=mesvere_id)


@router.get("/mesvere_qeydleri", response_model=list[schemas.MesvereQeydleriOut])
async def get_all_mesvere_qeydleri(db: Session = Depends(get_db)):
    mesvere_qeydleri = service.get_all_mesvere_qeydleri(db)
    return mesvere_qeydleri

@router.get("/mesvere_qeydleri/{mesvere_qeydleri_id}", response_model=schemas.MesvereQeydleriOut)
async def get_mesvere_qeydleri(mesvere_qeydleri_id: int, db: Session = Depends(get_db)):
    mesvere_qeydleri = service.get_mesvere_qeydleri(db, mesvere_qeydleri_id=mesvere_qeydleri_id)
    return mesvere_qeydleri

@router.post("/mesvere_qeydleri", response_model=schemas.MesvereQeydleriOut)
async def create_mesvere_qeydleri(mesvere_qeydleri: schemas.MesvereQeydleriCreate, db: Session = Depends(get_db)):
    mesvere_qeydleri = service.create_mesvere_qeydleri(db, mesvere_qeydleri)
    return mesvere_qeydleri

@router.put("/mesvere_qeydleri/{mesvere_qeydleri_id}", response_model=schemas.MesvereQeydleriOut)
async def update_mesvere_qeydleri(mesvere_qeydleri_id: int, mesvere_qeydleri: schemas.MesvereQeydleriUpdate, db: Session = Depends(get_db)):
    mesvere_qeydleri = service.update_mesvere_qeydleri(db, mesvere_qeydleri_id=mesvere_qeydleri_id, mesvere_qeydleri_update=mesvere_qeydleri)
    return mesvere_qeydleri

@router.delete("/mesvere_qeydleri/{mesvere_qeydleri_id}")
async def delete_mesvere_qeydleri(mesvere_qeydleri_id: int, db: Session = Depends(get_db)):
    return service.delete_mesvere_qeydleri(db, mesvere_qeydleri_id=mesvere_qeydleri_id)
