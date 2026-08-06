from sqlalchemy.orm import Session

from efms.database.database import SessionLocal


class DatabaseSession:

    @staticmethod
    def get_session() -> Session:
        """
        Create a new database session.
        """

        return SessionLocal()