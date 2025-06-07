#  Copyright (C) 2025 by Higher Expectations for Racine County

from typing import Set

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel
from .person import Person


class Team(BaseModel):
    r"""A collection of people
    
    Attributes
    ----------
    name: str
        The verbal/written signifier of this group of people
    members: Set[Person]
        The people who make up the team.
    """

    __tablename__ = "team"

    pk: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    members: Mapped[Set["Person"]] = relationship(
        secondary="team_member"
    )


class TeamMember(BaseModel):
    r"""The association table for team memberships

    Attributes
    ----------
    team: Team
        the team that the person belongs to
    person: Person
        the person whose team membership is being recorded.
    """

    __tablename__ = "team_member"

    person_pk: Mapped[int] = mapped_column(ForeignKey("person.pk"),
                                           primary_key=True)
    team_pk: Mapped[int] = mapped_column(ForeignKey("team.pk"),
                                         primary_key=True)
