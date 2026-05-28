from pydantic import BaseModel
from datetime import datetime

class FacturaBase(BaseModel):
    fecha: datetime
    cliente: int
    valortotal: float

class FacturaCrear(FacturaBase):
    pass

class Factura(FacturaBase):
    id: int | None = None
