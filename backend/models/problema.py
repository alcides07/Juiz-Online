from sqlalchemy import Column, Integer, String, CheckConstraint
from sqlalchemy.orm import relationship
from database import Base


class Problema(Base):
    __tablename__ = "problemas"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    nome = Column(
        String(length=64),
        index=True
    )

    nome_arquivo_entrada = Column(
        String(length=64)
    )

    nome_arquivo_saida = Column(
        String(length=64)
    )

    tempo_limite = Column(
        Integer,
        CheckConstraint('memoria_limite >= 250'),
        CheckConstraint('memoria_limite <= 15000'),
    )

    memoria_limite = Column(
        Integer,
        CheckConstraint('memoria_limite >= 4'),
        CheckConstraint('memoria_limite <= 1024'),
    )

    tags = relationship("Tag")
