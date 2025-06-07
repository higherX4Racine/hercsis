#  Copyright (C) 2025 by Higher Expectations for Racine County

from sqlalchemy import select

import pytest

from hercsis.models.person import Person
from hercsis.models.team import Team
from hercsis.models.team import TeamMember


def test_empty_team(db_session_factory):
    with db_session_factory() as session:
        team = Team(name="void")
        session.add(team)

        nuthin = session.scalars(
            select(TeamMember)
            .join(Team)
            .where(Team.name == "void")
        ).all()

        assert nuthin == []


def test_no_duplicate_team_members(db_session_factory, example_persons):
    with db_session_factory() as session:
        team = Team(name="problematic",
                    members=set(example_persons))
        assert len(team.members) == 4
        team.members.add(example_persons[0])
        assert len(team.members) == 4


def test_team(db_session_factory, example_persons):

    with db_session_factory() as session:
        people = session.scalars(select(Person)).all()

        assert len(people) == 0

        team = Team(pk=42,
                    name="Examples!",
                    members=set(example_persons))

        session.add(team)

        assert team in session

        assert len(team.members) == 4

        members = session.scalars(select(TeamMember)).all()

        assert len(members) == 4

        people = session.scalars(
            select(Person, Team)
            .join(Team.members)
            .where(Team.name == "Examples!")
        ).all()

        for person in example_persons:
            assert person in people
