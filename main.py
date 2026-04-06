from fastapi import FastAPI

app = FastAPI(
    title="SOLV API",
    description="Backend para el sistema de orquestación de laboratorios virtuales",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "estado": "activo",
        "mensaje": "¡Misión exitosa! El backend de SOLV está corriendo perfectamente.",
        "entorno": "Python 3.11-slim"
    }