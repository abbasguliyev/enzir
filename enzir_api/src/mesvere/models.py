from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Table
from sqlalchemy.orm import relationship
from src.database import Base

from datetime import datetime, timezone

class Mesvere(Base):
    __tablename__ = "mesvere"

    id = Column(Integer, primary_key=True, index=True)
    basliq = Column(String)
    tarix = Column(Date, default=datetime.now(timezone.utc))

    mesvere_qeydleri = relationship("MesvereQeydleri", back_populates="mesvere")


class MesvereQeydleri(Base):
    __tablename__ = "mesvere_qeydleri"

    id = Column(Integer, primary_key=True, index=True)
    basliq = Column(String)
    aciqlama = Column(String)
    bitibmi = Column(Boolean, default=False)
    mesvere_id = Column(Integer, ForeignKey("mesvere.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

    mesvere = relationship("Mesvere", back_populates="mesvere_qeydleri")
    user = relationship("User", back_populates="mesvere_qeydleri")
