#  Copyright (C) 2025 by Higher Expectations for Racine County
r"""All specific institution models will inherit from this base class."""
from sqlalchemy.orm import Mapped


class Institution:
    r"""Common properties of every institution

    All institutions have identity numbers in the databases of the National
    Center for Educational Statistics (NCES). They also have id numbers in
    state databases. These number are rarely the same.

    Attributes
    ----------
    name: str
        A long name for the institution
    nickname: str
        A short name for the institution
    federal_id:
        The institution's ID number in NCES
    state_id:
        The institution's ID number in its state's data systems
    """
    name: Mapped[str]
    nickname: Mapped[str]
    federal_id: Mapped[int]
    state_id: Mapped[int]
