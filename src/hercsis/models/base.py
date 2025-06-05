#  Copyright (C) 2025 by Higher Expectations for Racine County
r"""the root of the map of table classes"""

from sqlalchemy.orm import DeclarativeBase


class BaseModel(DeclarativeBase):
    r"""Nothing here"""
    pass

database_metadata = BaseModel.metadata
