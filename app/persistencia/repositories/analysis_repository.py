from datetime import datetime
from typing import Any

from sqlalchemy.orm import Session

from app.persistencia.models.models import AnalysisReport


class AnalysisRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_report(
        self,
        *,
        user_id: int,
        project_name: str,
        loc: int,
        complexity: int,
        code_smells: dict[str, Any],
        analysis_date: datetime | None = None,
    ) -> AnalysisReport:
        report = AnalysisReport(
            user_id=user_id,
            project_name=project_name,
            analysis_date=analysis_date or datetime.utcnow(),
            loc=loc,
            complexity=complexity,
            code_smells=code_smells,
        )

        self.db.add(report)
        self.db.commit()
        self.db.refresh(report)
        return report

    def get_reports_by_user(self, user_id: int) -> list[AnalysisReport]:
        return (
            self.db.query(AnalysisReport)
            .filter(AnalysisReport.user_id == user_id)
            .order_by(AnalysisReport.analysis_date.desc())
            .all()
        )
