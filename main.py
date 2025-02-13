from fastapi import FastAPI

app = FastAPI()

estado_solenoide = "cerrar"  # Estado inicial

@app.get("/")
def read_root():
    return {"message": "API funcionando correctamente"}

@app.get("/estado")
def get_estado():
    return {"estado": estado_solenoide}

@app.post("/estado/{nuevo_estado}")
def set_estado(nuevo_estado: str):
    global estado_solenoide
    if nuevo_estado in ["abrir", "cerrar"]:
        estado_solenoide = nuevo_estado
        return {"message": f"Estado cambiado a {nuevo_estado}"}
    return {"error": "Estado no válido, usa 'abrir' o 'cerrar'"}
