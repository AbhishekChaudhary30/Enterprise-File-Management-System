from typing import Optional

from sqlalchemy import select

from efms.database import session
from efms.database.models import FileRecord
from efms.database.session import DatabaseSession

from efms.database.operation_history import (
    OperationHistory,
)

class FileRepository:
    """
    Repository responsible only for database operations.
    """

    def add(self, record: FileRecord) -> FileRecord:

        session = DatabaseSession.get_session()

        try:
            session.add(record)
            session.commit()
            session.refresh(record)
            return record

        finally:
            session.close()

    def get_all(self) -> list[FileRecord]:

        session = DatabaseSession.get_session()

        try:
            statement = select(FileRecord)

            return list(
                session.scalars(statement).all()
            )

        finally:
            session.close()

    def get_by_path(
        self,
        path: str,
    ) -> Optional[FileRecord]:

        session = DatabaseSession.get_session()

        try:
            statement = (
                select(FileRecord)
                .where(FileRecord.path == path)
            )

            return session.scalars(statement).first()

        finally:
            session.close()

    def exists(
        self,
        path: str,
    ) -> bool:

        return self.get_by_path(path) is not None

    def update(
        self,
        record: FileRecord,
    ) -> FileRecord:

        session = DatabaseSession.get_session()

        try:
            merged = session.merge(record)
            session.commit()
            session.refresh(merged)
            return merged

        finally:
            session.close()

    def delete(
        self,
        record: FileRecord,
    ) -> None:

        session = DatabaseSession.get_session()

        try:
            entity = session.merge(record)
            session.delete(entity)
            session.commit()

        finally:
            session.close()
            
    def add_history(

        self,

        operation: str,

        target: str,

        status: str,

    ):

        session = DatabaseSession.get_session()

        try:

            history = OperationHistory(

                operation=operation,

                target=target,

                status=status,

            )

            session.add(history)

            session.commit()

        finally:

            session.close()
            
    def get_recent_history(
        self,
        limit: int = 10,
    ):

        session = DatabaseSession.get_session()

        try:

            return (
                session.query(OperationHistory)
                .order_by(
                    OperationHistory.created_at.desc()
                )
                .limit(limit)
                .all()
            )

        finally:

            session.close()
            
    def recent_history(
            self,
            limit: int = 20,
        ):

            session = DatabaseSession.get_session()

            try:

                return (

                    session.query(OperationHistory)

                    .order_by(

                        OperationHistory.created_at.desc()

                    )

                    .limit(limit)

                    .all()

                )

            finally:

                session.close()