from typing import Any, Dict

from app.motor_analisis.services import analyze_java_code
from app.persistencia.models.models import AnalysisReport
from app.persistencia.repositories import AnalysisRepository


class AnalysisCoordinator:
    def __init__(self, repository: AnalysisRepository) -> None:
        self.repository = repository

    def process_and_save_java_code(
        self, user_id: int, project_name: str, code_string: str
    ) -> AnalysisReport:
        """Procesa código Java, guarda el resultado y devuelve el reporte creado.

        - Analiza el código usando `analyze_java_code`.
        - Crea y persiste el `AnalysisReport` mediante el repositorio.
        """
        analysis = analyze_java_code(code_string)

        loc = int(analysis.get("loc", 0))
        complexity = int(analysis.get("complexity", 0))
        code_smells = analysis.get("code_smells", [])

        # El repositorio espera un dict para el campo JSON; empaquetamos la lista
        code_smells_payload: Dict[str, Any] = {"smells": code_smells}

        report = self.repository.create_report(
            user_id=user_id,
            project_name=project_name,
            loc=loc,
            complexity=complexity,
            code_smells=code_smells_payload,
        )

        return report
