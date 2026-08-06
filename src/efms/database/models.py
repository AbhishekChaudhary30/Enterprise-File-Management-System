from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from efms.database.database import Base


class FileRecord(Base):

    __tablename__ = "files"

    id = Column(

        Integer,

        primary_key=True,

        index=True,

    )

    name = Column(

        String,

        nullable=False,

    )

    extension = Column(

        String,

        nullable=False,

    )

    path = Column(

        String,

        nullable=False,

        unique=True,

    )

    size = Column(

        Integer,

        nullable=False,

    )

    sha256 = Column(

        String,

        nullable=False,

    )
