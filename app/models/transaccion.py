from pydantic import BaseModel

class TransaccionBase(BaseModel):
    descripcion: str
    factura: int

class TransaccionCrear(TransaccionBase):
    pass

class Transaccion(TransaccionBase):
    id: int | None = None
