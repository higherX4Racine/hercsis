#  Copyright (C) 2025 by Higher Expectations for Racine County
r"""The base class for all people in the data set"""

from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class Person(BaseModel):
    r"""One individual human being

    Attributes
    ----------
    pk: int
        the primary key for this table.
    full_name: str
        I decided to not faff about with first/last/given/sur-names
    """
    __tablename__ = "person"

    pk: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str]

    def __repr__(self) -> str:
        return f"Person(pk={self.pk}, full_name='{self.full_name}')"

    def __str__(self) -> str:
        return self.full_name
