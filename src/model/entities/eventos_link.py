from sqlalchemy import Column, Integer, String, ForeignKey
from src.model.configs.base import Base

class EventosLink(Base):
    __tablename__ = "eventos_link"  # Nome da tabela deve ser minúsculo

    id = Column(Integer, primary_key=True, autoincrement=True)
    evento_id = Column(Integer, ForeignKey("eventos.id"))
    inscrito_id = Column(Integer, ForeignKey("inscritos.id"))
    link = Column(String, nullable=False)