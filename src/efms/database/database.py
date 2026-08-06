from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from efms.core.constants import DATABASE_FILE

import os

from efms.core.constants import PROJECT_ROOT

DATABASE_FILE = PROJECT_ROOT / "workspace" / os.getenv(
    "EFMS_DATABASE",
    "efms.db",
)

DATABASE_URL = f"sqlite:///{DATABASE_FILE}"

engine = create_engine(

    DATABASE_URL,

    echo=False,

)

SessionLocal = sessionmaker(

    autocommit=False,

    autoflush=False,

    bind=engine,

)

Base = declarative_base()