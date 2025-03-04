from pydantic import BaseModel
from datetime import datetime, date
from src.mesvere.models import Mesvere, MesvereQeydleri

class MesvereBase(BaseModel):
    basliq: str
    tarix: date

class MesvereCreate(MesvereBase):
    pass

class MesvereUpdate(MesvereBase):
    basliq: str | None
    tarix: date | None

class MesvereOut(MesvereBase):
    id: int

    class Config:
        orm_mode = True

class MesvereQeydleriBase(BaseModel):
    basliq: str
    aciqlama: str
    bitibmi: bool

class MesvereQeydleriCreate(MesvereQeydleriBase):
    mesvere_id: int
    user_id: int

class MesvereQeydleriUpdate(MesvereQeydleriBase):
    basliq: str | None
    aciqlama: str | None
    bitibmi: bool | None
    mesvere_id: int | None
    user_id: int | None

class MesvereQeydleriOut(MesvereQeydleriBase):
    mesvere_id: int
    user_id: int

    class Config:
        orm_mode = True
