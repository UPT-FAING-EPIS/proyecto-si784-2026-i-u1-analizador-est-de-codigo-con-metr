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

        # nuevas métricas estructurales devueltas por analyze_java_code
        nom = int(analysis.get("nom", 0))
        npm = int(analysis.get("npm", 0))
        noa = int(analysis.get("noa", 0))
        cloc = int(analysis.get("cloc", 0))

        # Empaquetar smells y métricas en el payload JSON esperado por el repositorio
        code_smells_payload: Dict[str, Any] = {
            "smells": code_smells,
            "metrics": {"nom": nom, "npm": npm, "noa": noa, "cloc": cloc},
        }

        report = self.repository.create_report(
            user_id=user_id,
            project_name=project_name,
            loc=loc,
            complexity=complexity,
            code_smells=code_smells_payload,
        )

        return report
