from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.persistencia.database.database import Base, engine
from app.presentacion.routers.analysis_router import router as analysis_router
from app.presentacion.routers.auth_router import router as auth_router

app = FastAPI(title="Analizador Estático de Código")

app.mount("/static", StaticFiles(directory="app/presentacion/static"), name="static")

# Crear las tablas en la base de datos al iniciar
Base.metadata.create_all(bind=engine)

app.include_router(analysis_router)
app.include_router(auth_router)


@app.get("/")
async def root() -> FileResponse:
    return FileResponse("app/presentacion/static/index.html")


@app.get("/dashboard")
async def dashboard() -> FileResponse:
    return FileResponse("app/presentacion/static/dashboard.html")
