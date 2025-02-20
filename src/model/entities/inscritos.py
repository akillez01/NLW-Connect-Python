from src.model.configs.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from .eventos import Eventos

class Inscritos(Base):  # Corrigido erro de digitação
    __tablename__ = "inscritos"  # Nome da tabela deve ser minúsculo

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    link = Column(String, nullable=False)
    evento_id = Column(Integer, ForeignKey("eventos.id"))  # Corrigido nome da tabela
