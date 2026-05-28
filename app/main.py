from fastapi import FastAPI
from app.modelo.cliente import Cliente
from app.modelo.factura import Factura
from app.modelo.transaccion import Transaccion

app = FastAPI()

lista_clientes: list[Cliente] = []
lista_facturas: list[Factura] = []
lista_transacciones: list[Transaccion] = []


@app.get("/clientes")
def listar_clientes():
    return {"Clientes": lista_clientes}

@app.post("/clientes")
async def crear_clientes(datos_cliente: Cliente):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    cliente_val.id = len(lista_clientes) + 1
    lista_clientes.append(cliente_val)
    return cliente_val

@app.put("/clientes/{id}")
async def editar_cliente(id: int, datos_cliente: Cliente):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == id:
            cliente_val = Cliente.model_validate
            (datos_cliente.model_dump())
            cliente_val.id = id
            lista_clientes[i] = cliente_val
            return {"mensaje": "Se actualizo el cliente satisfactoriamente.", "cliente": cliente_val}

@app.delete("/clientes/{id}")
async def eliminar_cliente(id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == id:
            lista_clientes.pop(i)
            return {"mensaje": "Se elimino el cliente correctamente.", "cliente": obj_cliente}
    return {"error": "Cliente no encontrado"}


@app.get("/facturas")
def listar_facturas():
    return {"Facturas": lista_facturas}

@app.post("/facturas")
def crear_factura(datos_factura: Factura):
    global next_id_factura
    factura_nueva = datos_factura.copy(update={"id": next_id_factura})
    next_id_factura += 1
    lista_facturas.append(factura_nueva)
    return {"mensaje": "Factura creada", "factura": factura_nueva}

@app.put("/facturas/{id}")
def editar_factura(id: int, datos_factura: Factura):
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == id:
            factura_val = datos_factura.copy(update={"id": id})
            lista_facturas[i] = factura_val
            return {"mensaje": "Se actualizo la factura satisfactoriamente.", "factura": factura_val}
    return {"error": "Factura no encontrada"}

@app.delete("/facturas/{id}")
def eliminar_factura(id: int):
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == id:
            lista_facturas.pop(i)
            return {"mensaje": "Se elimino la factura correctamente.", "factura": obj_factura}
    return {"error": "Factura no encontrada"}

@app.get("/transacciones")
def listar_transacciones():
    return {"Transacciones": lista_transacciones}

@app.post("/transacciones")
def crear_transaccion(datos_transaccion: Transaccion):
    global next_id_transaccion
    transaccion_nueva = datos_transaccion.copy(update={"id": next_id_transaccion})
    next_id_transaccion += 1
    lista_transacciones.append(transaccion_nueva)
    return {"mensaje": "Transaccion creada", "transaccion": transaccion_nueva}

@app.put("/transacciones/{id}")
def editar_transaccion(id: int, datos_transaccion: Transaccion):
    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == id:
            transaccion_val = datos_transaccion.copy(update={"id": id})
            lista_transacciones[i] = transaccion_val
            return {"mensaje": "Se actualizo la transaccion satisfactoriamente.", "transaccion": transaccion_val}
    return {"error": "Transaccion no encontrada"}

@app.delete("/transacciones/{id}")
def eliminar_transaccion(id: int):
    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == id:
            lista_transacciones.pop(i)
            return {"mensaje": "Se elimino la transaccion correctamente.", "transaccion": obj_transaccion}
    return {"error": "Transaccion no encontrada"}