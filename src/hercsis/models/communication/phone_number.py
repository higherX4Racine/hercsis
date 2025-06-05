#  Copyright (C) 2025 by Higher Expectations for Racine County

from re import match
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base import BaseModel


class PhoneNumber(BaseModel):
    r"""Details about one phone number that a person might have.

    Attributes
    ----------
    person: Person
        the owner of the phone number
    digits: int
        an integer representation of the phone number
    is_mobile: bool, optional
        whether the phone is not a landline or is
    can_text: bool, optional
        even some mobile phones can't text, right?
    """
    __tablename__ = "phone_number"

    person_pk: Mapped[int] = mapped_column(ForeignKey("person.pk"),
                                           primary_key=True)
    person: Mapped["Person"] = relationship()
    digits: Mapped[int] = mapped_column(primary_key=True)
    is_mobile: Mapped[Optional[bool]]
    can_text: Mapped[Optional[bool]]

    def __str__(self) -> str:
        return (
                "%s (%s) %s-%s" %
                match(r"(\d*)(\d{3})(\d{3})(\d{4})$",
                      str(self.digits)).groups()
        ).strip()
