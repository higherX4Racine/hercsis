#  Copyright (C) 2025 by Higher Expectations for Racine County

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import BaseModel


class PostalAddress(BaseModel):
    r"""A physical address where post is delivered or picked up

    Attributes
    ----------
    person: Person
        the person living/receiving mail at the address
    street: str
        the building, street, apartment, e.g. 221 Baker Street, Apt. B
    municipality: str
        town or city or RFD, etc.
    state: str
        state or province
    code: str
        a postal code, like a ZIP
    """

    __tablename__ = "postal_address"

    pk: Mapped[int] = mapped_column(primary_key=True)
    person_pk: Mapped[int] = mapped_column(ForeignKey("person.pk"))
    person: Mapped["Person"] = relationship()

    street: Mapped[str]
    municipality: Mapped[str]
    state: Mapped[str]
    code: Mapped[str]

    def __str__(self) -> str:
        return f"{self.street}\n{self.municipality}, {self.state} {self.code}"