from pydantic import BaseModel, Field
from enum import Enum

ARQUIVO_ID_DESCRIPTION = "identificador do arquivo"
PROBLEMA_ID_DESCRIPTION = "Identificador do problema associado ao arquivo"


class SecaoSchema(Enum):
    RECURSO = "recursos"
    FONTE = "arquivos_fonte"
    ANEXO = "anexo"
    SOLUCAO = "solucao"


class ArquivoBase(BaseModel):

    nome: str = Field(
        max_length=64,
        description="Nome do arquivo do problema"
    )

    secao: SecaoSchema = Field(
        description="Grupo o qual o arquivo faz parte"
    )

    status: str | None = Field(default=None,
                               description="Tipos de status de veredíto para arquivos de solução"
                               )


class ArquivoWithBody(ArquivoBase):
    corpo: str = Field(
        max_length=250000,
        description="Conteúdo do arquivo"
    )


class ArquivoReadFull(ArquivoWithBody):
    id: int = Field(description=ARQUIVO_ID_DESCRIPTION)
    problema_id: int = Field(
        description=PROBLEMA_ID_DESCRIPTION)


class ArquivoReadSimple(ArquivoBase):
    id: int = Field(description=ARQUIVO_ID_DESCRIPTION)
    problema_id: int = Field(
        description=PROBLEMA_ID_DESCRIPTION)


class ArquivoCreate(ArquivoWithBody):
    pass


class ArquivoCreateSingle(ArquivoWithBody):
    problema_id: int = Field(
        description=PROBLEMA_ID_DESCRIPTION)