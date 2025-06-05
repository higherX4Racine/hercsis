#  Copyright (C) 2025 by Higher Expectations for Racine County

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import BaseModel


class EmailAddress(BaseModel):
    r"""One email address belonging to one person.

    Attributes
    ----------
    person: Person
        The owner of the email address
    text: str
        The full email address, `@` and all.
    """
    __tablename__ = "email_address"

    pk: Mapped[int] = mapped_column(primary_key=True)
    person_pk: Mapped[int] = mapped_column(ForeignKey("person.pk"))
    person: Mapped["Person"] = relationship()
    text: Mapped[str]

    def __str__(self) -> str:
        return self.text
