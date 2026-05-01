from typing import Any

from fastapi import APIRouter, Depends, File, Form, UploadFile
from sqlalchemy.orm import Session

from app.negocios.services.analysis_coordinator import AnalysisCoordinator
from app.persistencia.database.dependencies import get_db
from app.persistencia.repositories import AnalysisRepository

router = APIRouter(prefix="/api/analysis", tags=["analysis"])


@router.post("/upload")
async def upload_code_analysis(
    file: UploadFile = File(...),
    user_id: int = Form(...),
    db: Session = Depends(get_db),
) -> dict[str, Any]:
    """Recibe un archivo Java, lo analiza y guarda el reporte en la BD.

    - file: Archivo con código Java.
    - user_id: ID del usuario que sube el análisis (simulado con Form).
    - db: Sesión de base de datos inyectada.

    Retorna el reporte creado en formato JSON.
    """
    # Leer el contenido del archivo
    content = await file.read()
    code_string = content.decode("utf-8")

    # Instanciar repositorio y coordinador
    repository = AnalysisRepository(db)
    coordinator = AnalysisCoordinator(repository)

    # Procesar y guardar el análisis
    # El nombre del proyecto es el nombre del archivo sin extensión
    project_name = file.filename.split(".")[0] if file.filename else "unnamed_project"

    report = coordinator.process_and_save_java_code(
        user_id=user_id, project_name=project_name, code_string=code_string
    )

    # Convertir el reporte a dict para la respuesta JSON
    return {
        "id": report.id,
        "user_id": report.user_id,
        "project_name": report.project_name,
        "analysis_date": report.analysis_date.isoformat(),
        "loc": report.loc,
        "complexity": report.complexity,
        "code_smells": report.code_smells,
    }


@router.get("/history/{user_id}")
async def get_analysis_history(
    user_id: int,
    db: Session = Depends(get_db),
) -> list[dict[str, Any]]:
    """Obtiene el historial de reportes de un usuario en formato lista JSON."""
    repository = AnalysisRepository(db)
    reports = repository.get_reports_by_user(user_id)

    return [
        {
            "id": report.id,
            "user_id": report.user_id,
            "project_name": report.project_name,
            "analysis_date": report.analysis_date.isoformat(),
            "loc": report.loc,
            "complexity": report.complexity,
            "code_smells": report.code_smells,
        }
        for report in reports
    ]
