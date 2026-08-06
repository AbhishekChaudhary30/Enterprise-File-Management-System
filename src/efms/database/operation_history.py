from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from efms.database.database import Base


class OperationHistory(Base):

    __tablename__ = "operation_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    operation = Column(
        String,
        nullable=False,
    )

    target = Column(
        String,
        nullable=False,
    )

    status = Column(
        String,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )